// Render animated reels: node render.js reels.json outDir [id1,id2,...] [--workers 3] [--preview]
// Each reel = engine.html + config -> 30 fps JPEG frames -> ffmpeg (H.264 1080x1920) + audio.py soundtrack.
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path'), { spawn, execFileSync } = require('child_process');

const args = process.argv.slice(2);
const cfgFile = args[0], outDir = args[1];
const only = args[2] && !args[2].startsWith('--') ? args[2].split(',') : null;
const wi = args.indexOf('--workers'); const WORKERS = wi > 0 ? +args[wi + 1] : 3;
const PREVIEW = args.includes('--preview');
const FPS = 30;
const engine = 'file://' + path.resolve(__dirname, 'engine.html');
let reels = JSON.parse(fs.readFileSync(cfgFile, 'utf8')).reels;
if (only) reels = reels.filter(r => only.includes(r.id));
fs.mkdirSync(outDir, { recursive: true });

async function one(browser, cfg) {
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  await page.goto(engine);
  await page.evaluate(() => document.fonts.ready);
  const info = await page.evaluate(c => init(c), cfg);
  const base = path.join(outDir, cfg.id);
  if (PREVIEW) {
    for (const t of cfg.previewTimes || [1.2, 2.4, 4.5, 7, 9.5, 12.5]) {
      await page.evaluate(t => render(t), t);
      await page.screenshot({ path: `${base}_t${t}.jpg`, type: 'jpeg', quality: 80 });
    }
    await page.close(); return;
  }
  const evf = base + '.events.json', wav = base + '.wav';
  fs.writeFileSync(evf, JSON.stringify(info.events));
  execFileSync('python3', [path.join(__dirname, 'audio.py'), evf, wav, String(info.dur), cfg.theme]);
  const ff = spawn('ffmpeg', ['-v', 'error', '-y', '-f', 'image2pipe', '-framerate', String(FPS), '-i', '-', '-i', wav,
    '-c:v', 'libx264', '-preset', 'medium', '-crf', '21', '-pix_fmt', 'yuv420p', '-profile:v', 'high',
    '-c:a', 'aac', '-b:a', '160k', '-shortest', '-movflags', '+faststart', base + '.mp4']);
  const done = new Promise((res, rej) => ff.on('close', c => c ? rej(new Error('ffmpeg ' + c)) : res()));
  const N = Math.round(info.dur * FPS);
  for (let i = 0; i < N; i++) {
    await page.evaluate(t => render(t), i / FPS);
    const buf = await page.screenshot({ type: 'jpeg', quality: 92 });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    if (cfg.coverAt && Math.abs(i / FPS - cfg.coverAt) < 0.5 / FPS) fs.writeFileSync(base + '_cover.jpg', buf);
  }
  ff.stdin.end(); await done;
  fs.unlinkSync(evf); fs.unlinkSync(wav);
  await page.close();
  console.log('ok', cfg.id);
}

(async () => {
  const browser = await chromium.launch();
  const q = [...reels];
  await Promise.all(Array.from({ length: Math.min(WORKERS, q.length) }, async () => {
    while (q.length) { const c = q.shift(); try { await one(browser, c); } catch (e) { console.error('FAIL', c.id, e.message); } }
  }));
  await browser.close();
})();
