// Couche 3D (three.js) pour story.html — « un style d'animation par jour » (20 nov. 2026, consigne de Yaacoub).
// cfg.world = nom du monde (WORLDS ci-dessous), cfg.look = 'clay' | 'lowpoly' | 'pixel'.
// Le monde est dessiné dans un canvas WebGL derrière les scènes DOM (set:'none' = transparent) ;
// sous-titres, bulles, tableur d'exemple et carte de fin restent en DOM (story.html).
// Tout est déterministe : render(t) place chaque objet à partir de t (pas d'état entre images).
(function () {
  const TH = THREE;
  let R, S, CAM, LOOK, W, cv;
  const cl = (x, a = 0, b = 1) => Math.max(a, Math.min(b, x));
  const ln = (t, a, b) => cl((t - a) / (b - a));
  const eo3 = x => 1 - Math.pow(1 - x, 3);
  const eio3 = x => x < .5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2;
  const sp = (t, t0, k = 1) => { const p = (t - t0) * k; if (p <= 0) return 0; return 1 - Math.exp(-5.2 * p) * Math.cos(10.5 * p); };
  const hash = n => { const x = Math.sin(n * 127.1) * 43758.5453; return x - Math.floor(x); };

  // ---------- matériaux selon le style ----------
  let fpTex = null;
  function fingerprint() { // texture de relief « pâte à modeler » (traces de doigts)
    if (fpTex) return fpTex;
    const c = document.createElement('canvas'); c.width = c.height = 512; const x = c.getContext('2d');
    x.fillStyle = '#808080'; x.fillRect(0, 0, 512, 512);
    for (let k = 0; k < 26; k++) {
      const cx = hash(k) * 512, cy = hash(k + 50) * 512, r0 = 20 + hash(k + 9) * 60;
      for (let r = r0; r < r0 + 70; r += 5) { x.strokeStyle = `rgba(${hash(r + k) > .5 ? 255 : 0},${hash(r + k) > .5 ? 255 : 0},${hash(r + k) > .5 ? 255 : 0},.10)`; x.lineWidth = 2; x.beginPath(); x.arc(cx, cy, r, hash(k + r) * 6, hash(k + r) * 6 + 2.2); x.stroke(); }
    }
    const im = x.getImageData(0, 0, 512, 512); for (let i = 0; i < im.data.length; i += 4) { const n = (hash(i * .37) - .5) * 26; im.data[i] += n; im.data[i + 1] += n; im.data[i + 2] += n; } x.putImageData(im, 0, 0);
    fpTex = new TH.CanvasTexture(c); fpTex.wrapS = fpTex.wrapT = TH.RepeatWrapping; fpTex.repeat.set(2, 2); return fpTex;
  }
  let ppTex = null;
  function paperTex() { if (ppTex) return ppTex; const c = document.createElement('canvas'); c.width = c.height = 256; const x = c.getContext('2d'); x.fillStyle = '#ffffff'; x.fillRect(0, 0, 256, 256);
    for (let i = 0; i < 1400; i++) { const a = hash(i) * 256, b = hash(i + 99) * 256; x.strokeStyle = `rgba(0,0,0,${.025 + hash(i + 7) * .04})`; x.beginPath(); x.moveTo(a, b); x.lineTo(a + (hash(i + 3) - .5) * 14, b + (hash(i + 5) - .5) * 14); x.stroke(); }
    ppTex = new TH.CanvasTexture(c); ppTex.wrapS = ppTex.wrapT = TH.RepeatWrapping; ppTex.colorSpace = TH.SRGBColorSpace; return ppTex; }
  function mat(color, o = {}) {
    if (LOOK === 'clay') return new TH.MeshStandardMaterial({ color, roughness: o.gloss ? .25 : .82, metalness: 0, bumpMap: o.gloss ? null : fingerprint(), bumpScale: .9, emissive: o.em || 0, emissiveIntensity: o.em ? 1 : 0 });
    if (LOOK === 'film') return new TH.MeshPhysicalMaterial({ color, roughness: o.gloss ? .15 : .5, metalness: 0, clearcoat: o.gloss ? 1 : .35, clearcoatRoughness: .3, sheen: .4, sheenRoughness: .6, emissive: o.em || 0, emissiveIntensity: o.em ? 1 : 0 });
    if (LOOK === 'paper') return new TH.MeshLambertMaterial({ color, map: paperTex(), emissive: o.em || 0, emissiveIntensity: o.em ? .8 : 0 });
    if (LOOK === 'stick') return new TH.MeshBasicMaterial({ color: o.em ? o.em : color });
    if (LOOK === 'lowpoly') return new TH.MeshLambertMaterial({ color, flatShading: true, emissive: o.em || 0, emissiveIntensity: o.em ? 1 : 0 });
    return new TH.MeshToonMaterial({ color, emissive: o.em || 0, emissiveIntensity: o.em ? 1 : 0 }); // pixel
  }
  const SEG = () => LOOK === 'lowpoly' ? 7 : LOOK === 'pixel' ? 10 : 32;
  const sph = (r, m) => new TH.Mesh(new TH.SphereGeometry(r, SEG(), Math.max(5, SEG() * .75 | 0)), m);
  const cap = (r, l, m) => new TH.Mesh(new TH.CapsuleGeometry(r, l, LOOK === 'lowpoly' ? 3 : 8, SEG()), m);
  const cyl = (r1, r2, h, m, s) => new TH.Mesh(new TH.CylinderGeometry(r1, r2, h, s || SEG()), m);
  function shadowy(o) { o.traverse(c => { if (c.isMesh) { c.castShadow = true; c.receiveShadow = true; } }); return o; }

  // ---------- personnage « blob » (chat, chien, ou invité) ----------
  function blob(o) {
    const g = new TH.Group(); const s = o.s || 1; const body = mat(o.color); const P = { g, o };
    const torso = cap(.62, .55, body); torso.position.y = 1.05; g.add(torso); P.torso = torso;
    const head = new TH.Group(); head.position.y = 1.55; torso.add(head); P.head = head; head.position.set(0, .45, 0);
    // yeux (gros, brillants : look « dessin animé 3D »)
    const white = mat('#fbf7f0', { gloss: 1 }), black = mat('#16121c', { gloss: 1 });
    P.eyes = [-1, 1].map(k => { const e = new TH.Group(); e.position.set(k * .25, .05, .5); head.add(e);
      const w = sph(.2, white); w.scale.set(1, 1.12, .7); e.add(w); const p = sph(.115, black); p.position.set(0, -.01, .12); e.add(p);
      const h = sph(.04, mat('#ffffff', { em: '#ffffff' })); h.position.set(.05, .06, .21); e.add(h); return e; });
    P.brows = [-1, 1].map(k => { const b = cap(.03, .16, mat(o.dark || '#3a2418')); b.rotation.z = Math.PI / 2; b.position.set(k * .25, .32, .5); head.add(b); return b; });
    const mouthM = mat('#4a1620'); P.smile = new TH.Mesh(new TH.TorusGeometry(.11, .03, 6, 16, Math.PI), mouthM); P.smile.rotation.z = Math.PI; P.smile.position.set(0, -.2, .56); head.add(P.smile);
    P.oh = sph(.09, mouthM); P.oh.scale.set(1, 1.3, .5); P.oh.position.set(0, -.24, .55); head.add(P.oh);
    [-1, 1].forEach(k => { const b = sph(.09, mat('#ff8fa3')); b.scale.set(1, .6, .4); b.position.set(k * .42, -.13, .44); head.add(b); });
    if (o.kind === 'cat') { [-1, 1].forEach(k => { const e = new TH.Mesh(new TH.ConeGeometry(.17, .34, LOOK === 'clay' ? 24 : 5), body); e.position.set(k * .36, .62, 0); e.rotation.z = -k * .35; head.add(e); });
      [-1, 1].forEach(k => [0, 1].forEach(j => { const w = cap(.008, .28, mat('#3a2a22')); w.rotation.z = Math.PI / 2 + k * (j ? .18 : -.05); w.position.set(k * .48, -.15 - j * .06, .42); head.add(w); }));
      const n = sph(.06, mat('#ff7a8a')); n.position.set(0, -.08, .6); head.add(n);
      const tail = cap(.07, .7, body); tail.position.set(.35, .55, -.45); tail.rotation.set(-.6, 0, -.5); g.add(tail); P.tail = tail; }
    if (o.kind === 'dog') { P.ears = [-1, 1].map(k => { const e = sph(.2, mat(o.dark || '#7a4a2a')); e.scale.set(.55, 1.15, .4); e.position.set(k * .55, .2, .05); e.rotation.z = k * .25; head.add(e); return e; });
      const sn = sph(.17, mat(o.muzzle || '#f3e0c8')); sn.scale.set(1.2, .8, .7); sn.position.set(0, -.14, .5); head.add(sn); const n = sph(.07, mat('#1c1416', { gloss: 1 })); n.position.set(0, -.07, .62); head.add(n);
      const tail = cap(.07, .35, body); tail.position.set(0, .55, -.6); tail.rotation.x = -1; g.add(tail); P.tail = tail; }
    if (o.kind === 'guest') { torso.scale.set(1, .78, 1); }
    // bras et jambes
    P.arms = [-1, 1].map(k => { const piv = new TH.Group(); piv.position.set(k * .6, .25, 0); torso.add(piv); const a = cap(.1, .32, body); a.position.y = -.22; piv.add(a); piv.rotation.z = k * .35; return piv; });
    if (o.kind !== 'guest') [-1, 1].forEach(k => { const l = cap(.13, .2, body); l.position.set(k * .26, .2, 0); g.add(l); });
    if (o.veil) { for (let i = 0; i < 11; i++) { const a = -0.15 + i / 10 * (Math.PI + .3); const f = sph(.075, mat(['#ff7aa8', '#fff0f5', '#ffd27a'][i % 3])); f.position.set(Math.cos(a) * .5, .5 + Math.sin(a) * .16, -.05 + Math.sin(a) * .1); head.add(f); }
      const v = cap(.42, .5, new TH.MeshStandardMaterial({ color: '#fff4fb', transparent: true, opacity: .35, roughness: .6 })); v.scale.set(1, 1, .25); v.position.set(0, -.05, -.55); head.add(v); }
    if (o.bow) { const bm = mat(o.bow); [-1, 1].forEach(k => { const w = new TH.Mesh(new TH.ConeGeometry(.12, .2, LOOK === 'clay' ? 16 : 4), bm); w.rotation.z = k * Math.PI / 2; w.position.set(k * .1, .36, .58); torso.add(w); }); const kn = sph(.06, bm); kn.position.set(0, .36, .62); torso.add(kn); }
    g.scale.setScalar(s); shadowy(g); return P;
  }
  // pose/émotion : mood = happy | shock | angry | sad | cheer | point | type | idle
  function pose(P, t, mood, ph = 0) {
    const sq = mood === 'cheer' ? Math.abs(Math.sin(t * 7 + ph)) : 0;
    const bob = mood === 'cheer' ? sq * .28 : Math.sin(t * 3 + ph) * .03;
    P.torso.position.y = 1.05 + bob; const st = 1 + (mood === 'cheer' ? (sq < .15 ? -.12 : .05) : Math.sin(t * 3 + ph) * .02);
    P.torso.scale.y = (P.o.kind === 'guest' ? .78 : 1) * st; P.torso.scale.x = P.torso.scale.z = 1 / Math.sqrt(st);
    const shock = mood === 'shock', ang = mood === 'angry', sad = mood === 'sad';
    P.smile.visible = !shock; P.oh.visible = shock; P.smile.rotation.z = sad || ang ? 0 : Math.PI; P.smile.position.y = sad || ang ? -.28 : -.2;
    P.eyes.forEach(e => e.scale.setScalar(shock ? 1.25 : 1));
    // clignement
    const bl = ((t + ph) % 3.1) < .09 ? .1 : 1; P.eyes.forEach(e => e.scale.y *= bl);
    P.brows.forEach((b, i) => { const k = i ? 1 : -1; b.position.y = shock ? .45 : .32; b.rotation.z = Math.PI / 2 + (ang ? k * .45 : sad ? -k * .35 : 0); });
    P.head.rotation.z = Math.sin(t * 2.1 + ph) * .06 + (sad ? .12 : 0); P.head.rotation.x = sad ? .2 : 0;
    const [L, Rr] = P.arms;
    if (mood === 'cheer' || shock) { L.rotation.z = -2.5 - Math.sin(t * 9 + ph) * .3; Rr.rotation.z = 2.5 + Math.sin(t * 9 + ph) * .3; }
    else if (mood === 'point') { L.rotation.z = -.3; Rr.rotation.z = 1.7; Rr.rotation.x = -.6; }
    else if (mood === 'type') { L.rotation.x = Rr.rotation.x = -1.1 + Math.sin(t * 22) * .15; L.rotation.z = -.2; Rr.rotation.z = .2; }
    else { L.rotation.set(0, 0, -.35 - Math.sin(t * 2 + ph) * .08); Rr.rotation.set(0, 0, .35 + Math.sin(t * 2 + ph) * .08); }
    if (mood !== 'type' && mood !== 'point') { L.rotation.x = 0; Rr.rotation.x = 0; }
    if (P.tail) P.tail.rotation.z = (P.o.kind === 'dog' ? 0 : -.5) + Math.sin(t * (mood === 'cheer' || mood === 'happy' ? 14 : 4) + ph) * (mood === 'cheer' ? .6 : .2);
    if (P.ears) P.ears.forEach((e, i) => e.rotation.z = (i ? .25 : -.25) * (i ? 1 : -1) * -1 + Math.sin(t * 6 + ph + i) * (mood === 'cheer' ? .25 : .05));
  }

  // ---------- décor commun ----------
  function room(o) {
    S.background = new TH.Color(o.bg || '#1d0f24'); S.fog = new TH.Fog(o.bg || '#1d0f24', 14, 34);
    const fl = new TH.Mesh(new TH.CircleGeometry(30, LOOK === 'lowpoly' ? 12 : 64), mat(o.floor || '#7a3d3a')); fl.rotation.x = -Math.PI / 2; fl.receiveShadow = true; S.add(fl);
    const hemi = new TH.HemisphereLight(o.sky || '#ffd9c2', o.ground || '#3a1f40', LOOK === 'clay' || LOOK === 'film' ? .9 : 1.1); S.add(hemi);
    const key = new TH.DirectionalLight('#fff1dc', LOOK === 'clay' || LOOK === 'film' ? 2.2 : 1.6); key.position.set(5, 11, 8); key.castShadow = true; key.shadow.mapSize.set(2048, 2048);
    Object.assign(key.shadow.camera, { left: -12, right: 12, top: 12, bottom: -12, near: 1, far: 40 }); key.shadow.radius = 6; key.shadow.bias = -.0005; S.add(key);
    const rim = new TH.DirectionalLight(o.rim || '#8fb4ff', 1.1); rim.position.set(-6, 6, -8); S.add(rim);
    // guirlande d'ampoules au fond (bokeh chaud)
    for (let i = 0; i < 26; i++) { const b = sph(.09, mat('#ffd27a', { em: '#ffb84d' })); b.position.set(-12 + i * .95, 5.2 + Math.sin(i * .8) * .35, -9); S.add(b); }
  }
  function table(x, z, cloth) { const g = new TH.Group(); const top = cyl(1.25, 1.25, .16, mat(cloth || '#f6c7d6'), LOOK === 'lowpoly' ? 10 : 48); top.position.y = 1.0; g.add(top);
    const leg = cyl(.12, .2, 1, mat('#5a2f3a')); leg.position.y = .5; g.add(leg); const fl = sph(.18, mat('#ff7aa8')); fl.position.y = 1.2; g.add(fl);
    g.position.set(x, 0, z); return shadowy(g); }
  function textSprite(txt, col) { const c = document.createElement('canvas'); c.width = c.height = 256; const x = c.getContext('2d'); const fs = txt.length > 2 ? Math.min(150, 340 / txt.length) : 190;
    x.font = `900 ${fs}px Inter, sans-serif`; x.textAlign = 'center'; x.textBaseline = 'middle'; x.lineWidth = fs / 8; x.strokeStyle = '#000'; x.strokeText(txt, 128, 140); x.fillStyle = col; x.fillText(txt, 128, 140);
    const sp = new TH.Sprite(new TH.SpriteMaterial({ map: new TH.CanvasTexture(c), transparent: true })); return sp; }
  function check(x, y, z) { const g = new TH.Group(); const m = mat('#2ee6a6', { em: '#0d5a40' }); const a = cap(.07, .16, m); a.rotation.z = .8; a.position.set(-.1, -.05, 0); const b = cap(.07, .42, m); b.rotation.z = -.6; b.position.set(.12, .08, 0); g.add(a, b); g.position.set(x, y, z); return shadowy(g); }

  // ---------- caméra ----------
  function camAt(p, l, fov) { CAM.position.set(p[0], p[1], p[2]); CAM.lookAt(l[0], l[1], l[2]); if (fov && CAM.fov !== fov) { CAM.fov = fov; CAM.updateProjectionMatrix(); } }
  function shots(list, t) { // [t0, t1, from{p,l}, to{p,l}, fov]
    const s = list.find(s => t >= s[0] && t < s[1]) || list[list.length - 1]; const k = eio3(ln(t, s[0], s[1]));
    const mix = (a, b) => a.map((v, i) => v + (b[i] - v) * k); camAt(mix(s[2].p, s[3].p), mix(s[2].l, s[3].l), s[4] || 35);
  }

  // ================= MONDES =================
  const WORLDS = {};
  // Mariage : la belle-mère ajoute des invités, la table 4 déborde (tour d'invités), on réorganise, tout est vert.
  WORLDS.wedding = function (cfg) {
    room({ bg: '#1f0d26', floor: '#8a4a52', sky: '#ffd6e4', ground: '#3b1d45', rim: '#9fb6ff' });
    // arche fleurie
    const arch = new TH.Mesh(new TH.TorusGeometry(2.6, .16, LOOK === 'lowpoly' ? 5 : 12, LOOK === 'lowpoly' ? 12 : 40, Math.PI), mat('#f2c6a0')); arch.position.set(0, 0, -6); S.add(shadowy(arch));
    for (let i = 0; i <= 14; i++) { const a = Math.PI * i / 14; const f = sph(.22, mat(['#ff7aa8', '#ffd27a', '#b18cff', '#fff0f5'][i % 4])); f.position.set(Math.cos(a) * 2.6, Math.sin(a) * 2.6, -5.8); S.add(shadowy(f)); }
    const T = [[-3.4, -2.2], [0, -3], [3.4, -2.2], [-3.6, 1.2], [3.6, 1.2], [-6.4, -.4], [6.4, -.4]].map(([x, z]) => ({ x, z, g: table(x, z) }));
    T.forEach(o => S.add(o.g));
    const bride = blob({ kind: 'cat', color: '#f5b46a', dark: '#8a5a2a', veil: 1 }), groom = blob({ kind: 'dog', color: '#b97a4a', dark: '#5a3418', bow: '#ff5d73' });
    bride.g.position.set(-1.1, 0, 3.6); groom.g.position.set(1.1, 0, 3.6); S.add(bride.g, groom.g);
    const COL = ['#5cc8ff', '#ffc23d', '#b18cff', '#2ee6a6', '#ff9f43', '#ff7aa8', '#9ad0ff', '#c7f27a'];
    // invités : 8 par table (7 tables = 56 visibles) + 6 de trop qui s'empilent sur la table 4 (index 1)
    const G = []; let n = 0;
    T.forEach((tb, ti) => { const cnt = ti === 6 ? 0 : 7; for (let k = 0; k < cnt; k++) { const a = k / cnt * Math.PI * 2; G.push({ home: [tb.x + Math.cos(a) * 1.65, 0, tb.z + Math.sin(a) * 1.65], drop: .2 + n * .045, ti }); n++; } });
    const tower = []; for (let k = 0; k < 6; k++) tower.push({ home: [T[1].x + (k % 2 ? .12 : -.12), 1.0 + k * .5, T[1].z + .1], drop: 2.4 + k * .28, ti: 1, extra: k });
    // pendant la réorganisation (9.2-11.4 s), les 6 de trop sautent vers la table vide (index 6) et la table 5
    tower.forEach((g, k) => { const tb = k < 4 ? T[6] : T[5]; const a = (k < 4 ? k / 4 : (k - 4) / 2 + .1) * Math.PI * 2; g.dest = [tb.x + Math.cos(a) * 1.65, 0, tb.z + Math.sin(a) * 1.65]; g.jump = 9.3 + k * .32; });
    G.push(...tower);
    G.forEach((g, i) => { g.P = blob({ kind: 'guest', color: COL[i % COL.length], s: .42 }); S.add(g.P.g); g.ph = i * 1.3; });
    G.forEach(g => window.__ev && window.__ev(g.drop + .5, 'pop'));
    const checks = T.map(tb => { const c = check(tb.x, 2.6, tb.z); c.scale.setScalar(0); S.add(c); return c; });
    const conf = []; for (let i = 0; i < 70; i++) { const c = new TH.Mesh(new TH.BoxGeometry(.12, .2, .03), mat(COL[i % COL.length])); c.visible = false; S.add(c); conf.push(c); }
    const SH = [[0, 3.2, { p: [0, 6.5, 13.5], l: [0, 1.2, 0] }, { p: [0, 5.6, 11.2], l: [0, 1.4, 0] }, 38],
      [3.2, 6.6, { p: [2.2, 3.4, 5.2], l: [0, 2.3, -3] }, { p: [1.4, 3.1, 4.2], l: [0, 2.5, -3] }, 42],
      [6.6, 9.0, { p: [0, 6, 12], l: [0, 1, 0] }, { p: [0, 6, 12], l: [0, 1, 0] }, 38],
      [9.0, 13.2, { p: [-3, 7.5, 14], l: [0, .8, -.5] }, { p: [2, 6.6, 13], l: [0, 1.3, .5] }, 40]];
    return function (t) {
      const frz = t > 5.55 && t < 6.6; const ta = frz ? 5.55 : t; // gel (silence) avant le tableur
      shots(SH, t);
      pose(bride, ta, ta < 2.2 ? 'happy' : ta < 9 ? 'shock' : ta < 11.6 ? 'point' : 'cheer', 0);
      pose(groom, ta, ta < 3 ? 'happy' : ta < 9 ? 'shock' : ta < 11.6 ? 'happy' : 'cheer', 1.7);
      bride.g.rotation.y = ta > 9 && ta < 11.6 ? -.5 : 0; groom.g.rotation.y = ta > 9 && ta < 11.6 ? -.4 : 0;
      G.forEach((g, i) => { const d = ta - g.drop; const P = g.P;
        if (d < 0) { P.g.visible = false; return; } P.g.visible = true;
        let [x, y, z] = g.home;
        if (d < .5) y += 9 * (1 - eo3(d / .5)) * (1 - d / .5) + 0; // chute
        const land = d >= .5 ? Math.exp(-(d - .5) * 6) * Math.abs(Math.sin((d - .5) * 14)) * .5 : 0; y += land;
        if (g.extra != null && ta > 4.2 && ta < 9.3) { x += Math.sin(ta * 5 + g.extra) * .06 * (g.extra + 1); } // la tour vacille
        if (g.dest && ta >= g.jump) { const q = ln(ta, g.jump, g.jump + .7); const e = eio3(q); x = x + (g.dest[0] - x) * e; z = z + (g.dest[2] - z) * e; y = y + (0 - y) * e + Math.sin(q * Math.PI) * 3.2; }
        P.g.position.set(x, y, z); P.g.lookAt(CAM.position.x, y, CAM.position.z);
        const sq = d < .5 ? 1.15 : 1 - land * .4; P.g.scale.set(.42 / Math.sqrt(sq), .42 * sq, .42 / Math.sqrt(sq));
        pose(P, ta, g.extra != null && ta < 9.3 && ta > 3 ? 'shock' : ta > 11.6 ? 'cheer' : 'happy', g.ph); });
      checks.forEach((c, i) => { const ts = 11.0 + i * .12; const p = cl(sp(ta, ts, 1.4), 0, 1.3); c.scale.setScalar(p * 1.2); c.rotation.y = ta * 2; });
      conf.forEach((c, i) => { const ts = 11.6; const p = ta - ts; if (p < 0 || p > 2) { c.visible = false; return; } c.visible = true;
        const a = hash(i) * Math.PI * 2, v = 2 + hash(i + 7) * 4; c.position.set(Math.cos(a) * v * p, 2 + 9 * p - 6 * p * p, 2 + Math.sin(a) * v * p * .6); c.rotation.set(p * 9 + i, p * 7, i); });
    };
  };

  // Jour de loyer : immeuble de 6 logements, pièces qui volent, fenêtres vert / jaune / rouge, tout est suivi la nuit venue.
  WORLDS.rentday = function (cfg) {
    const night = new TH.Color('#140f33'), dusk = new TH.Color('#3b1f5c');
    S.background = dusk.clone(); S.fog = new TH.Fog('#2a1a4f', 30, 70);
    const hemi = new TH.HemisphereLight('#ffc9a8', '#3a2a6a', 1.35); S.add(hemi);
    const key = new TH.DirectionalLight('#ffd6a0', 1.7); key.position.set(-8, 10, 9); key.castShadow = true; key.shadow.mapSize.set(2048, 2048);
    Object.assign(key.shadow.camera, { left: -14, right: 14, top: 14, bottom: -14, near: 1, far: 50 }); S.add(key);
    // sol en collines low poly
    const gg = new TH.PlaneGeometry(60, 60, 24, 24); const pa = gg.attributes.position;
    for (let i = 0; i < pa.count; i++) { const x = pa.getX(i), y = pa.getY(i); const d = Math.hypot(x, y); pa.setZ(i, d < 9 ? 0 : (hash(i) * 1.6 + (d - 9) * .18)); }
    gg.computeVertexNormals(); const gr = new TH.Mesh(gg, mat('#3d7a4a')); gr.rotation.x = -Math.PI / 2; gr.receiveShadow = true; S.add(gr);
    const road = new TH.Mesh(new TH.PlaneGeometry(4, 30), mat('#3a3550')); road.rotation.x = -Math.PI / 2; road.position.set(0, .02, 8); S.add(road);
    // arbres, nuages, lune
    for (let i = 0; i < 16; i++) { const x = (i % 2 ? 1 : -1) * (4.6 + hash(i) * 6), z = -11 + hash(i + 4) * 9; const tr = new TH.Group();
      const c = new TH.Mesh(new TH.ConeGeometry(.9 + hash(i + 2) * .5, 2.6, 6), mat(['#2f8f5a', '#3fa66a', '#28794c'][i % 3])); c.position.y = 2; tr.add(c);
      const st = cyl(.15, .2, .8, mat('#6a4428'), 5); st.position.y = .4; tr.add(st); tr.position.set(x, 0, z); S.add(shadowy(tr)); }
    const clouds = []; for (let i = 0; i < 6; i++) { const g = new TH.Group(); for (let k = 0; k < 3; k++) { const b = new TH.Mesh(new TH.IcosahedronGeometry(.8 + k % 2 * .3, 0), mat('#e9e2ff')); b.position.x = k * .9; g.add(b); } g.position.set(-14 + i * 6, 9 + hash(i) * 2.5, -14 - hash(i + 1) * 4); S.add(g); clouds.push(g); }
    [[-3.9, 4.2], [4.1, 5.0], [-4.6, 1.0]].forEach(([x, z], i) => { const tr = new TH.Group(); const c = new TH.Mesh(new TH.ConeGeometry(1.0, 2.8, 6), mat(['#3fa66a', '#2f8f5a', '#28794c'][i])); c.position.y = 2.1; tr.add(c);
      const st = cyl(.15, .2, .8, mat('#6a4428'), 5); st.position.y = .4; tr.add(st); tr.position.set(x, 0, z); S.add(shadowy(tr)); });
    const moon = new TH.Mesh(new TH.IcosahedronGeometry(1.2, 1), mat('#fff1c2', { em: '#ffe08a' })); moon.position.set(8, 12, -18); S.add(moon);
    // immeuble 3 étages x 2 logements
    const bld = new TH.Group(); const body = new TH.Mesh(new TH.BoxGeometry(6, 7.2, 3.2), mat('#c77a5a')); body.position.y = 3.6; bld.add(body);
    const roof = new TH.Mesh(new TH.ConeGeometry(4.6, 1.8, 4), mat('#5a3a6a')); roof.position.y = 8.1; roof.rotation.y = Math.PI / 4; roof.scale.z = .75; bld.add(roof);
    const door = new TH.Mesh(new TH.BoxGeometry(1.1, 1.6, .1), mat('#4a2a3a')); door.position.set(0, .8, 1.62); bld.add(door);
    bld.position.set(0, 0, -2.2); S.add(shadowy(bld));
    const ST = ['paid', 'paid', 'partial', 'paid', 'unpaid', 'partial']; // ordre : logements 1-6
    const COLS = { paid: '#2ee6a6', partial: '#ffc23d', unpaid: '#ff5d73', off: '#2a2440' };
    const W = []; for (let f = 0; f < 3; f++) for (let k = 0; k < 2; k++) { const i = f * 2 + k; const m = new TH.MeshLambertMaterial({ color: '#2a2440', emissive: '#000000', flatShading: true });
      const w = new TH.Mesh(new TH.BoxGeometry(1.7, 1.3, .12), m); w.position.set(k ? 1.5 : -1.5, 1.0 + f * 2.25 + 1.1, -2.2 + 1.62); S.add(w);
      const fr = new TH.Mesh(new TH.BoxGeometry(1.95, 1.55, .08), mat('#3a2030')); fr.position.copy(w.position); fr.position.z -= .03; S.add(fr);
      const ten = blob({ kind: i === 2 ? 'dog' : 'guest', color: ['#5cc8ff', '#b18cff', '#b97a4a', '#ff9f43', '#9ad0ff', '#ff7aa8'][i], dark: '#5a3418', s: .32 }); ten.g.position.set(w.position.x, w.position.y - .62, w.position.z + .05); S.add(ten.g);
      W.push({ w, m, ten, st: ST[i], at: .9 + i * .32 }); }
    const landlord = blob({ kind: 'cat', color: '#f5b46a', dark: '#8a5a2a' }); landlord.g.position.set(0, 0, 3.4); S.add(landlord.g);
    // presse-papiers
    const clip = new TH.Mesh(new TH.BoxGeometry(.5, .65, .05), mat('#d9c08a')); clip.position.set(.35, -.4, .1); landlord.arms[1].add(clip);
    const coins = W.map((o, i) => { const c = new TH.Mesh(new TH.CylinderGeometry(.22, .22, .06, 10), mat('#ffd23d', { em: '#7a5a00' })); c.rotation.x = Math.PI / 2; c.visible = false; S.add(c); return c; });
    const qs = []; for (let i = 0; i < 7; i++) { const q = textSprite(['?', '!?', '$?', '?'][i % 4], ['#ffffff', '#ffc23d', '#ff5d73', '#5cc8ff'][i % 4]); q.visible = false; S.add(q); qs.push(q); }
    const sign = new TH.Group(); const sb = new TH.Mesh(new TH.BoxGeometry(3.6, 1.0, .15), mat('#1b1440', { em: '#0a0a20' })); sign.add(sb); const ck = check(0, 0, .15); ck.scale.setScalar(1.3); sign.add(ck); sign.position.set(2.9, 1.6, 2.6); sign.scale.setScalar(0); S.add(sign);
    const SH = [[0, 3.2, { p: [0, 4.2, 17.5], l: [0, 4.2, 0] }, { p: [0, 3.9, 14.8], l: [0, 4.2, 0] }, 40],
      [3.2, 6.6, { p: [9, 4.5, 13], l: [0, 3.6, 0] }, { p: [-8, 4.8, 13.5], l: [0, 3.8, 0] }, 40],
      [6.6, 8.6, { p: [0, 4, 16], l: [0, 4, 0] }, { p: [0, 4, 16], l: [0, 4, 0] }, 40],
      [8.6, 13.2, { p: [0, 4.9, 19], l: [0, 5.0, 0] }, { p: [0, 4.6, 16.2], l: [0, 5.0, 0] }, 40]];
    W.forEach(o => window.__ev(o.at, 'ping'));
    return function (t) {
      shots(SH, t);
      const nk = ln(t, 7.8, 9.2); S.background.copy(dusk).lerp(night, nk); S.fog.color.copy(S.background); hemi.intensity = 1.35 - nk * .5; key.intensity = 1.7 - nk * 1.0;
      clouds.forEach((c, i) => c.position.x = -14 + i * 6 + t * .35);
      const stress = t > 2.6 && t < 8.6;
      pose(landlord, t, t < 2.6 ? 'happy' : t < 8.6 ? 'shock' : t < 11 ? 'happy' : 'cheer', 0);
      landlord.g.rotation.y = stress ? Math.sin(t * 5) * .5 : 0;
      W.forEach((o, i) => { const on = t >= o.at; const c = on ? COLS[o.st] : COLS.off;
        const blink = o.st === 'unpaid' && t < 8.6 && Math.floor(t * 4) % 2 ? .35 : 1;
        o.m.color.set(c); o.m.emissive.set(on ? c : '#000'); o.m.emissiveIntensity = (on ? .32 : 0) * blink * (t > 8.6 ? 1.25 : 1);
        o.ten.g.visible = on; pose(o.ten, t, o.st === 'unpaid' ? 'sad' : 'happy', i);
        const cn = coins[i]; const ct = t - o.at;
        if (o.st !== 'unpaid' && ct > 0 && ct < .9) { cn.visible = true; const q = ct / .9; const a = o.w.position, b = new TH.Vector3(0, 1.6, 3.4);
          cn.position.set(a.x + (b.x - a.x) * q, a.y + (b.y - a.y) * q + Math.sin(q * Math.PI) * 2.2, a.z + (b.z - a.z) * q); cn.rotation.z = t * 12; cn.scale.setScalar(o.st === 'partial' ? .65 : 1); }
        else cn.visible = false; });
      qs.forEach((q, i) => { const ts = 3.3 + i * .25; const p = t - ts; if (p < 0 || t > 6.6) { q.visible = false; return; } q.visible = true;
        q.position.set(Math.cos(i * 2.1) * 1.6, 3.4 + p * .9 + i % 2 * .3, 3.4 + Math.sin(i * 2.1) * .6); q.scale.setScalar(cl(p * 4) * 1.1); });
      const sp1 = cl(sp(t, 10.0, 1.3), 0, 1.25); sign.scale.setScalar(sp1); sign.rotation.y = Math.sin(t * 1.5) * .15;
    };
  };

  // Réunion d'asso : « qui veut être trésorier ? », toutes les têtes se tournent vers Biscuit, pluie de reçus, puis bravo.
  WORLDS.meeting = function (cfg) {
    room({ bg: '#10183a', floor: '#3a4a7a', sky: '#cfe0ff', ground: '#22284a', rim: '#ffb86b' });
    const board = new TH.Mesh(new TH.BoxGeometry(7, 3.2, .2), mat('#1f5a48')); board.position.set(0, 3.4, -5.5); S.add(shadowy(board));
    const bf = new TH.Mesh(new TH.BoxGeometry(7.4, 3.6, .1), mat('#8a5a3a')); bf.position.set(0, 3.4, -5.62); S.add(bf);
    const pres = blob({ kind: 'cat', color: '#f5b46a', dark: '#8a5a2a' }); pres.g.position.set(-2.6, 0, -3.8); S.add(pres.g);
    const hero = blob({ kind: 'dog', color: '#b97a4a', dark: '#5a3418' }); hero.g.position.set(0, 0, 1.2); S.add(hero.g);
    const COL = ['#5cc8ff', '#ffc23d', '#b18cff', '#2ee6a6', '#ff9f43', '#ff7aa8', '#9ad0ff', '#c7f27a'];
    const M = []; for (let r = 0; r < 3; r++) for (let c = 0; c < 5; c++) { if (r === 0 && c === 2) continue; const P = blob({ kind: 'guest', color: COL[(r * 5 + c) % 8], s: .55 });
      P.g.position.set(-4.4 + c * 2.2, 0, 1.2 + r * 2.0 - (r === 0 ? 0 : 0)); S.add(P.g); M.push({ P, ph: r * 5 + c }); }
    // desks
    for (let r = 0; r < 3; r++) for (let c = 0; c < 5; c++) { const d = new TH.Mesh(new TH.BoxGeometry(1.5, .12, .8), mat('#c9905a')); d.position.set(-4.4 + c * 2.2, .95, .3 + r * 2.0); S.add(shadowy(d)); }
    const crown = new TH.Group(); const cr = cyl(.32, .28, .26, mat('#ffd23d', { em: '#6a4a00' }), 8); crown.add(cr); for (let k = 0; k < 5; k++) { const sp_ = new TH.Mesh(new TH.ConeGeometry(.07, .22, 4), mat('#ffd23d', { em: '#6a4a00' })); const a = k / 5 * Math.PI * 2; sp_.position.set(Math.cos(a) * .3, .22, Math.sin(a) * .3); crown.add(sp_); }
    hero.head.add(crown); crown.position.set(0, .62, 0);
    const papers = []; for (let i = 0; i < 26; i++) { const p_ = new TH.Mesh(new TH.BoxGeometry(.5, .03, .65), mat(i % 5 ? '#f3efe2' : '#ffe08a')); S.add(shadowy(p_)); papers.push(p_); window.__ev(3.4 + i * .1, i % 3 ? 'tick' : 'pop'); }
    const medal = new TH.Group(); const md = cyl(.22, .22, .06, mat('#ffd23d', { em: '#6a4a00' }), 12); md.rotation.x = Math.PI / 2; medal.add(md); hero.torso.add(medal); medal.position.set(0, .05, .66);
    const SH = [[0, 1.4, { p: [0, 6, 12], l: [0, 1.5, -1] }, { p: [0, 5.4, 10.5], l: [0, 1.5, -1] }, 40],
      [1.4, 3.3, { p: [0, 2.6, 5.6], l: [0, 1.7, 1.2] }, { p: [0, 2.4, 4.8], l: [0, 1.8, 1.2] }, 40],
      [3.3, 6.6, { p: [3.5, 4.2, 7], l: [0, 1.5, 1.2] }, { p: [-3, 4.6, 7.5], l: [0, 1.5, 1.2] }, 42],
      [6.6, 9.0, { p: [0, 6, 12], l: [0, 1.5, -1] }, { p: [0, 6, 12], l: [0, 1.5, -1] }, 40],
      [9.0, 13.2, { p: [0, 7, 14], l: [0, 1.2, 1] }, { p: [0, 4.2, 8.5], l: [0, 1.8, 1.2] }, 40]];
    return function (t) {
      const frz = t > 5.6 && t < 6.6; const ta = frz ? 5.6 : t;
      shots(SH, t);
      pose(pres, ta, ta < 1.2 ? 'point' : ta < 9 ? 'happy' : 'cheer', 0); pres.g.rotation.y = .5;
      pose(hero, ta, ta < 1.3 ? 'happy' : ta < 3.3 ? 'shock' : ta < 9 ? 'sad' : 'cheer', 1);
      crown.visible = ta > 2.0; crown.scale.setScalar(cl(sp(ta, 2.0, 1.4), 0, 1.3)); medal.visible = ta > 10.2; medal.scale.setScalar(cl(sp(ta, 10.2, 1.4), 0, 1.3));
      M.forEach((m, i) => { const turn = ta > 1.0 + (i % 5) * .05; const P = m.P;
        if (turn && ta < 9) P.g.lookAt(hero.g.position.x, 0, hero.g.position.z); else P.g.rotation.set(0, Math.PI, 0);
        if (!turn || ta >= 9) P.g.rotation.y = ta >= 9 ? 0 : Math.PI;
        pose(P, ta, ta >= 9.2 ? 'cheer' : turn && ta < 3.3 ? 'happy' : 'idle', m.ph); });
      papers.forEach((p_, i) => { const ts = 3.4 + i * .1; const d = ta - ts; if (d < 0 || ta > 9) { p_.visible = false; return; } p_.visible = true;
        const a = hash(i) * Math.PI * 2, r = .3 + hash(i + 3) * 1.4; const fall = cl(d / .7); const y = 6 * (1 - fall) + 1.05 + (i % 9) * .035 * fall;
        p_.position.set(hero.g.position.x + Math.cos(a) * r * .8, y, hero.g.position.z - .8 + Math.sin(a) * r * .5); p_.rotation.set(Math.sin(d * 6 + i) * (1 - fall) * .8, i, Math.cos(d * 5 + i) * (1 - fall) * .8); });
    };
  };

  // Bonhommes allumettes sur fond noir (format « stickman », comparaison) : 10 habitudes d'un coup contre 1 petite par jour.
  function stick(col) { const m = new TH.MeshBasicMaterial({ color: col || '#ffffff' }); const g = new TH.Group(); const P = { g };
    const L = (len, r = .07) => { const piv = new TH.Group(); const c = new TH.Mesh(new TH.CapsuleGeometry(r, len, 4, 10), m); c.position.y = -len / 2; piv.add(c); return piv; };
    P.hip = new TH.Group(); P.hip.position.y = 1.9; g.add(P.hip);
    P.spine = L(1.3); P.spine.rotation.z = Math.PI; P.hip.add(P.spine); // vers le haut
    P.head = new TH.Mesh(new TH.SphereGeometry(.36, 20, 14), m); P.head.position.y = -1.3 - .45; P.spine.add(P.head);
    P.sh = new TH.Group(); P.sh.position.y = -1.15; P.spine.add(P.sh);
    P.arm = [0, 1].map(() => { const u = L(.65); P.sh.add(u); const l = L(.6); l.position.y = -.65; u.add(l); u.rotation.z = Math.PI; return [u, l]; });
    P.leg = [0, 1].map(() => { const u = L(.9); P.hip.add(u); const l = L(.85); l.position.y = -.9; u.add(l); return [u, l]; });
    return P; }
  function walk(P, t, speed, lean) { const w = t * speed; P.hip.position.y = 1.9 + Math.abs(Math.sin(w)) * .08; P.hip.rotation.z = -lean;
    P.leg.forEach(([u, l], i) => { const ph = w + i * Math.PI; u.rotation.z = Math.sin(ph) * .6; l.rotation.z = -Math.max(0, Math.sin(ph + 1.2)) * .9; });
    P.arm.forEach(([u, l], i) => { const ph = w + (1 - i) * Math.PI; u.rotation.z = Math.PI + Math.sin(ph) * .7; l.rotation.z = .5 + Math.max(0, Math.sin(ph)) * .4; }); }
  WORLDS.versus = function (cfg) {
    S.background = new TH.Color('#000000');
    const A = stick('#ffffff'), B = stick('#ffffff'); A.g.position.set(-1.6, 0, 0); B.g.position.set(1.6, 0, 0); S.add(A.g, B.g);
    const wm = new TH.MeshBasicMaterial({ color: '#ffffff' });
    const mid = new TH.Mesh(new TH.BoxGeometry(.03, 9, .03), new TH.MeshBasicMaterial({ color: '#555555' })); mid.position.set(0, 3, 0); S.add(mid);
    const dashes = [-1, 1].map(k => { const g = new TH.Group(); for (let i = 0; i < 8; i++) { const d = new TH.Mesh(new TH.BoxGeometry(.5, .04, .04), wm); d.position.x = i * .7; g.add(d); } g.position.set(k * 1.6, 0, 0); S.add(g); return g; });
    // objets que A jongle : haltère, livre, bouteille, tapis...
    const items = []; const IT = ['💪', '📚', '🧘', '💧', '🏃', '🥗', '🛌', '✍️', '🎸', '🇪🇸'];
    IT.forEach((e, i) => { const sp_ = textSprite(e, '#fff'); sp_.scale.setScalar(.85); S.add(sp_); items.push(sp_); });
    const one = textSprite('📖', '#fff'); one.scale.setScalar(.85); S.add(one);
    const zz = textSprite('z', '#ffffff'); S.add(zz); const zz2 = textSprite('z', '#ffffff'); S.add(zz2);
    // escalier de 31 marches (fin)
    const stairs = new TH.Group(); for (let i = 0; i < 31; i++) { const st = new TH.Mesh(new TH.BoxGeometry(.26, .04, .5), wm); st.position.set(-3.9 + i * .22, i * .12, 0); stairs.add(st);
      const rs = new TH.Mesh(new TH.BoxGeometry(.04, .12, .5), wm); rs.position.set(-3.9 + i * .22 - .12, i * .12 - .06, 0); stairs.add(rs); } S.add(stairs);
    const flag = new TH.Group(); const pole = new TH.Mesh(new TH.BoxGeometry(.05, 1.6, .05), wm); pole.position.y = .8; flag.add(pole);
    const fl = new TH.Mesh(new TH.PlaneGeometry(.8, .5), new TH.MeshBasicMaterial({ color: '#2ee6a6', side: TH.DoubleSide })); fl.position.set(.42, 1.35, 0); flag.add(fl); S.add(flag);
    CAM.position.set(0, 3.0, 21); CAM.lookAt(0, 2.5, 0); CAM.fov = 40; CAM.updateProjectionMatrix();
    window.__ev(3.6, 'impact');
    return function (t) {
      const fin = t >= 8.6; stairs.visible = flag.visible = fin; mid.visible = !fin; dashes.forEach(d => d.visible = !fin);
      if (!fin) {
        const zoom = t < 3.2 ? 1 - t * .02 : .94; CAM.position.set(0, 3.0, 21 * zoom); CAM.lookAt(0, 2.5, 0);
        // A : sprint puis effondrement au « jour 4 »
        const fall = ln(t, 3.6, 4.1);
        if (fall <= 0) { walk(A, t, 16, .35); A.g.rotation.z = 0; A.g.position.y = 0; }
        else { walk(A, 3.6, 0, 0); A.g.rotation.z = -Math.PI / 2 * eo3(fall); A.g.position.y = .25 * fall; A.g.position.x = -1.6 + .4 * fall; }
        walk(B, t, 6, .05);
        dashes[0].position.x = -1.6 - 2.5 + ((-(fall > 0 ? 3.6 : t) * 6) % 1 + 1) % 1; dashes[1].position.x = 1.6 - 2.5 + ((-t * 2.2) % 1 + 1) % 1;
        items.forEach((it, i) => { const a = t * 7 + i * .63; let x = -1.6 + Math.cos(a) * .9, y = 5.2 + Math.sin(a) * .7;
          if (fall > 0) { const d = t - 3.6 - i * .03; x = -2.2 + (i - 4.5) * .28; y = Math.max(.3, 4.9 - d * d * 14); }
          it.position.set(x, y, .2); it.visible = true; });
        one.position.set(1.6 + .35, 3.05 + Math.sin(t * 6) * .05, .3); one.visible = true;
        zz.visible = zz2.visible = t > 4.4; const zp = (t * .8) % 1; zz.position.set(-.9 + zp * .5, .9 + zp * 1.2, .2); zz.scale.setScalar(.4 + zp * .4); zz2.position.set(-.6 + ((zp + .5) % 1) * .5, .9 + ((zp + .5) % 1) * 1.2, .2);
      } else {
        const lt = t - 8.6; CAM.position.set(0, 3.2, 22 - lt * .3); CAM.lookAt(0, 2.8, 0);
        const k = cl(lt / 2.6); const step = Math.min(30, Math.floor(k * 30));
        B.g.position.set(-3.9 + step * .22, step * .12 + .02, 0); walk(B, lt, k < 1 ? 9 : 0, .1); B.g.rotation.z = 0;
        if (k >= 1) { pose_cheer(B, t); }
        flag.position.set(-3.9 + 30 * .22 + .5, 30 * .12, 0); flag.scale.setScalar(cl(sp(t, 11.2, 1.3), 0, 1.25)); fl.rotation.y = Math.sin(t * 4) * .3;
        A.g.position.set(-3.0, .25, -1); A.g.rotation.z = -Math.PI / 2; walk(A, 0, 0, 0);
        items.forEach((it, i) => { it.position.set(-3.9 + i * .25, .3, -.7); }); one.position.set(B.g.position.x + .35, B.g.position.y + 3.05, .3);
        zz.visible = zz2.visible = true; const zp = (t * .8) % 1; zz.position.set(-2.4 + zp * .5, .9 + zp * 1.2, .2); zz2.position.set(-2.1 + ((zp + .5) % 1) * .5, .9 + ((zp + .5) % 1) * 1.2, .2);
      }
    };
    function pose_cheer(P, t) { P.arm.forEach(([u, l], i) => { u.rotation.z = Math.PI + (i ? 2.6 : -2.6) + Math.sin(t * 10) * .15; l.rotation.z = 0; }); P.hip.position.y = 1.9 + Math.abs(Math.sin(t * 7)) * .25; }
  };

  // ---------- papier découpé (formes plates extrudées, couches avec ombres) ----------
  function flat(shape, depth, color) { const g = new TH.ExtrudeGeometry(shape, { depth: depth || .1, bevelEnabled: true, bevelThickness: .015, bevelSize: .015, bevelSegments: 1, curveSegments: 24 }); const m = new TH.Mesh(g, mat(color)); m.castShadow = m.receiveShadow = true; return m; }
  const circ = r => { const s_ = new TH.Shape(); s_.absarc(0, 0, r, 0, Math.PI * 2, false); return s_; };
  const ell = (rx, ry) => { const s_ = new TH.Shape(); s_.absellipse(0, 0, rx, ry, 0, Math.PI * 2, false, 0); return s_; };
  const rect = (w, h, r = 0) => { const s_ = new TH.Shape(); if (!r) { s_.moveTo(-w / 2, -h / 2); s_.lineTo(w / 2, -h / 2); s_.lineTo(w / 2, h / 2); s_.lineTo(-w / 2, h / 2); return s_; }
    s_.moveTo(-w / 2 + r, -h / 2); s_.lineTo(w / 2 - r, -h / 2); s_.quadraticCurveTo(w / 2, -h / 2, w / 2, -h / 2 + r); s_.lineTo(w / 2, h / 2 - r); s_.quadraticCurveTo(w / 2, h / 2, w / 2 - r, h / 2); s_.lineTo(-w / 2 + r, h / 2); s_.quadraticCurveTo(-w / 2, h / 2, -w / 2, h / 2 - r); s_.lineTo(-w / 2, -h / 2 + r); s_.quadraticCurveTo(-w / 2, -h / 2, -w / 2 + r, -h / 2); return s_; };
  const tri = (w, h) => { const s_ = new TH.Shape(); s_.moveTo(-w / 2, 0); s_.lineTo(w / 2, 0); s_.lineTo(0, h); return s_; };
  function paperChar(o) { const g = new TH.Group(); const P = { g, o }; const z = (k) => k * .06;
    P.body = new TH.Group(); g.add(P.body); P.body.position.y = 1.1;
    const b = flat(ell(.62, .8), .08, o.color); P.body.add(b);
    if (o.apron) { const a = flat(rect(.75, .7, .12), .04, o.apron); a.position.set(0, -.2, z(2)); P.body.add(a); }
    P.head = new TH.Group(); P.head.position.set(0, .95, z(1)); P.body.add(P.head);
    const h = flat(ell(.62, .52), .08, o.color); P.head.add(h);
    if (o.kind === 'cat') [-1, 1].forEach(k => { const e = flat(tri(.36, .42), .06, o.color); e.position.set(k * .36, .3, -.02); e.rotation.z = -k * .3; P.head.add(e); const ei = flat(tri(.18, .22), .02, '#ff9fb3'); ei.position.set(k * .36, .36, .07); ei.rotation.z = -k * .3; P.head.add(ei); });
    if (o.kind === 'dog') P.ears = [-1, 1].map(k => { const piv = new TH.Group(); piv.position.set(k * .5, .3, .1); const e = flat(ell(.17, .34), .05, o.dark); e.position.y = -.28; piv.add(e); P.head.add(piv); return piv; });
    if (o.kind === 'dog') { const m = flat(ell(.24, .16), .03, o.muzzle || '#f3e0c8'); m.position.set(0, -.18, .1); P.head.add(m); }
    P.eyes = [-1, 1].map(k => { const e = new TH.Group(); e.position.set(k * .22, .04, .1); const w = flat(ell(.13, .15), .02, '#fbf7f0'); const p_ = flat(circ(.075), .02, '#16121c'); p_.position.z = .03; const hl = flat(circ(.025), .01, '#ffffff'); hl.position.set(.03, .04, .055); e.add(w, p_, hl); P.head.add(e); return e; });
    const nose = flat(ell(.06, .045), .02, o.kind === 'cat' ? '#ff7a8a' : '#1c1416'); nose.position.set(0, -.12, .14); P.head.add(nose);
    P.mouth = flat(ell(.09, .05), .01, '#4a1620'); P.mouth.position.set(0, -.27, .13); P.head.add(P.mouth);
    [-1, 1].forEach(k => { const c = flat(circ(.07), .01, '#ff8fa3'); c.position.set(k * .38, -.15, .1); P.head.add(c); });
    P.arms = [-1, 1].map(k => { const piv = new TH.Group(); piv.position.set(k * .5, .3, z(3)); const a = flat(rect(.16, .6, .08), .04, o.color); a.position.y = -.27; piv.add(a); P.body.add(piv); return piv; });
    [-1, 1].forEach(k => { const l = flat(rect(.2, .4, .08), .05, o.dark || o.color); l.position.set(k * .25, .25, -.02); g.add(l); });
    if (o.tail) { P.tail = new TH.Group(); P.tail.position.set(.45, .6, -.1); const t_ = flat(rect(.12, .7, .06), .04, o.color); t_.position.y = .3; P.tail.add(t_); g.add(P.tail); }
    g.scale.setScalar(o.s || 1); return P; }
  function ppose(P, t, mood, ph = 0) { const cheer = mood === 'cheer', shock = mood === 'shock';
    P.body.rotation.z = Math.sin(t * 2.2 + ph) * .04; P.body.position.y = 1.1 + (cheer ? Math.abs(Math.sin(t * 7 + ph)) * .25 : Math.sin(t * 3 + ph) * .02);
    P.head.rotation.z = Math.sin(t * 1.7 + ph) * .07; P.eyes.forEach(e => { e.scale.setScalar(shock ? 1.3 : 1); if (((t + ph) % 3.3) < .09) e.scale.y = .15; });
    P.mouth.scale.set(shock ? .8 : 1.2, shock ? 2.2 : .6, 1);
    const [L, Rr] = P.arms; if (cheer || shock) { L.rotation.z = -2.4 - Math.sin(t * 9 + ph) * .3; Rr.rotation.z = 2.4 + Math.sin(t * 9 + ph) * .3; }
    else if (mood === 'point') { L.rotation.z = -.2; Rr.rotation.z = 1.6; } else if (mood === 'count') { L.rotation.z = -.9 + Math.sin(t * 9) * .2; Rr.rotation.z = .9 - Math.sin(t * 9) * .2; }
    else { L.rotation.z = -.25 - Math.sin(t * 2 + ph) * .1; Rr.rotation.z = .25 + Math.sin(t * 2 + ph) * .1; }
    if (P.tail) P.tail.rotation.z = Math.sin(t * (cheer ? 12 : 3) + ph) * .5; if (P.ears) P.ears.forEach((e, i) => e.rotation.z = Math.sin(t * 5 + i) * .12); }

  // Marché de Noël en papier : savons à 5 $, tout se vend… et elle perd de l'argent ; le vrai coût, puis le bon prix.
  WORLDS.market = function (cfg) {
    S.background = new TH.Color('#10233a');
    const hemi = new TH.HemisphereLight('#fff3e0', '#2a3b5a', 1.2); S.add(hemi);
    const key = new TH.DirectionalLight('#fff0d8', 1.8); key.position.set(-4, 8, 10); key.castShadow = true; key.shadow.mapSize.set(2048, 2048);
    Object.assign(key.shadow.camera, { left: -10, right: 10, top: 12, bottom: -6, near: 1, far: 40 }); key.shadow.radius = 4; S.add(key);
    // couches de collines en papier
    ['#173a52', '#1f4e5e', '#2a6a64', '#357a5a'].forEach((c, i) => { const sh = new TH.Shape(); sh.moveTo(-14, -2); for (let k = 0; k <= 28; k++) { const x = -14 + k; sh.lineTo(x, 2.2 - i * .7 + Math.sin(k * .7 + i * 2) * .5 + Math.sin(k * .23 + i) * .8); } sh.lineTo(14, -2);
      const m = flat(sh, .1, c); m.position.set(0, 1.6 - i * .2, -6 + i * 1.2); S.add(m); });
    for (let i = 0; i < 40; i++) { const st = flat(circ(.05 + hash(i) * .05), .02, '#fff2c4'); st.material.emissive = new TH.Color('#ffe08a'); st.material.emissiveIntensity = .9; st.position.set(-8 + hash(i + 1) * 16, 6 + hash(i + 2) * 6, -7); S.add(st); }
    const moon = flat(circ(.9), .05, '#fff1c2'); moon.material.emissive = new TH.Color('#ffd86a'); moon.material.emissiveIntensity = .7; moon.position.set(3.2, 9.4, -6.5); S.add(moon);
    // fanions
    for (let i = 0; i < 13; i++) { const f = flat(tri(.4, -.5), .02, ['#ff7aa8', '#ffc23d', '#5cc8ff', '#2ee6a6'][i % 4]); f.position.set(-3.6 + i * .6, 6.4 - Math.sin(i / 12 * Math.PI) * .5, .2); f.rotation.x = Math.PI; f.rotation.z = Math.PI; S.add(f); }
    // étal
    const stall = new TH.Group(); const back = flat(rect(6.4, 4, .1), .1, '#7a4a2e'); back.position.set(0, 3, -1.2); stall.add(back);
    for (let i = 0; i < 8; i++) { const a = flat(rect(.8, 1, 0), .08, i % 2 ? '#ff5d73' : '#fff3ea'); a.position.set(-2.8 + i * .8, 5.2, -.6); a.rotation.x = -.3; stall.add(a); }
    const counter = flat(rect(6, 1.5, .08), .25, '#c9905a'); counter.position.set(0, .75, .9); stall.add(counter);
    S.add(stall);
    const soaps = []; for (let i = 0; i < 10; i++) { const so = flat(rect(.42, .3, .07), .18, ['#ffb3c8', '#c7f27a', '#b18cff', '#ffd27a', '#9ad0ff'][i % 5]); so.position.set(-2.3 + (i % 5) * 1.15, 1.62 + Math.floor(i / 5) * .36, 1.0 + Math.floor(i / 5) * -.05); S.add(so); soaps.push(so); }
    const tag = new TH.Group(); const tb = flat(rect(1.15, .72, .12), .04, '#fff3d6'); tb.position.x = -.0; tag.add(tb); tag.position.set(-2.1, 3.75, -.3); S.add(tag);
    const t5 = textSprite('5 $', '#ff5d73'); t5.scale.setScalar(.95); t5.position.set(0, 0, .14); tag.add(t5); const t12 = textSprite('12 $', '#1f9e6e'); t12.scale.setScalar(.95); t12.position.set(0, 0, .14); tag.add(t12);
    const seller = paperChar({ kind: 'cat', color: '#f5b46a', dark: '#c27a3a', apron: '#5cc8ff', tail: 1 }); seller.g.position.set(-.9, 1.0, -.2); S.add(seller.g);
    const helper = paperChar({ kind: 'dog', color: '#b97a4a', dark: '#6a3e20', muzzle: '#f3e0c8', apron: '#ffc23d', tail: 1, s: .9 }); helper.g.position.set(1.0, 1.0, -.3); S.add(helper.g);
    const CUST = ['#ff9f43', '#b18cff', '#2ee6a6', '#ff7aa8', '#5cc8ff', '#c7f27a'];
    const cust = CUST.map((c, i) => { const P = paperChar({ kind: i % 2 ? 'cat' : 'dog', color: c, dark: '#3a2a4a', s: .85 }); S.add(P.g); return { P, i }; });
    const coins = []; for (let i = 0; i < 6; i++) { const c = flat(circ(.16), .05, '#ffd23d'); c.material.emissive = new TH.Color('#7a5a00'); c.material.emissiveIntensity = .4; S.add(c); coins.push(c); }
    const SH = [[0, 3.3, { p: [0, 3.3, 15], l: [0, 2.8, 0] }, { p: [0, 3.2, 13], l: [0, 2.8, 0] }, 40],
      [3.3, 6.6, { p: [-1.4, 3.0, 7.5], l: [-.7, 2.6, 0] }, { p: [-1.0, 2.9, 6.6], l: [-.7, 2.7, 0] }, 40],
      [6.6, 9.0, { p: [0, 3.3, 14], l: [0, 2.8, 0] }, { p: [0, 3.3, 14], l: [0, 2.8, 0] }, 40],
      [9.0, 13.2, { p: [-1.3, 3.5, 9.0], l: [-1.2, 3.1, 0] }, { p: [0, 3.2, 13.5], l: [0, 2.8, 0] }, 40]];
    soaps.forEach((so, i) => window.__ev(.8 + i * .2, 'pop'));
    return function (t) {
      const frz = t > 5.6 && t < 6.6; const ta = frz ? 5.6 : t; shots(SH, t);
      ppose(seller, ta, ta < 3.3 ? 'cheer' : ta < 6.6 ? (ta < 4.2 ? 'count' : 'shock') : ta < 11 ? 'point' : 'cheer', 0);
      ppose(helper, ta, ta < 3.3 ? 'happy' : ta < 6.6 ? 'shock' : 'cheer', 1.4);
      soaps.forEach((so, i) => { const sold = .8 + i * .2; const back_ = 9.4 + i * .1; const gone = ta > sold && ta < back_; const p = gone ? 0 : ta >= back_ ? cl(sp(ta, back_, 1.5), 0, 1.2) : 1; so.scale.setScalar(Math.max(.001, p)); });
      cust.forEach(({ P, i }) => { const ts = .2 + i * .33; const x0 = 8 + i * 1.1; const x1 = -2.6 + i * 1.05; const p = eo3(ln(ta, ts, ts + .9)); const leave = ln(ta, 3.0 + i * .08, 3.9 + i * .08);
        P.g.position.set(x0 + (x1 - x0) * p - leave * 12, .0, 2.4 + (i % 2) * .5); ppose(P, ta, p > .9 && leave === 0 ? 'cheer' : 'happy', i); P.g.visible = ta < 9 || ta > 10.6;
        if (ta > 10.6) { const q = eo3(ln(ta, 10.6 + i * .12, 11.3 + i * .12)); P.g.position.set(8 + i - q * (10.6 - i * 1.05), 0, 2.4 + (i % 2) * .5); ppose(P, ta, 'happy', i); } });
      coins.forEach((c, i) => { const ts = 4.0 + i * .12; const p = ln(ta, ts, ts + .4); c.visible = ta > ts && ta < 6.6; c.position.set(-1.6 + i * .32, 1.6 + Math.sin(p * Math.PI) * .8, 1.3); c.rotation.y = ta * 6; });
      const flip = ln(ta, 9.2, 9.7); const sx = Math.max(.02, Math.abs(Math.cos(flip * Math.PI))); tag.scale.x = sx; t5.visible = flip < .5; t12.visible = flip >= .5; tag.rotation.z = Math.sin(ta * 2) * .05;
    };
  };

  // ---------- plan technique (« blueprint ») : traits clairs sur fond bleu, faces cachées ----------
  const BP_BG = '#0b3566', BP_LINE = '#d6ecff';
  function blueprint(root) { const list = []; root.traverse(o => { if (o.isMesh && !o.userData.noBP) list.push(o); });
    list.forEach(m => { const lc = m.userData.lc || BP_LINE;
      m.material = new TH.MeshBasicMaterial({ color: BP_BG, polygonOffset: true, polygonOffsetFactor: 1, polygonOffsetUnits: 1 }); m.castShadow = m.receiveShadow = false;
      const e = new TH.LineSegments(new TH.EdgesGeometry(m.geometry, 28), new TH.LineBasicMaterial({ color: lc })); e.userData.noBP = 1; m.add(e);
      const hull = new TH.Mesh(m.geometry, new TH.MeshBasicMaterial({ color: lc, side: TH.BackSide })); hull.scale.setScalar(m.geometry.type === 'SphereGeometry' && m.geometry.parameters.radius < .3 ? 1.22 : 1.06); hull.userData.noBP = 1; m.add(hull);
      m.userData.edge = e; m.userData.hull = hull; }); }
  function setLine(m, col) { if (m.userData.edge) { m.userData.edge.material.color.set(col); m.userData.hull.material.color.set(col); } }
  WORLDS.floorplan = function (cfg) {
    S.background = new TH.Color(BP_BG);
    const grid = new TH.GridHelper(40, 80, '#3f7fc0', '#1f5a96'); grid.position.y = .001; S.add(grid);
    const g2 = new TH.GridHelper(40, 16, '#6fa8dc', '#6fa8dc'); g2.position.y = .002; S.add(g2);
    const world = new TH.Group(); S.add(world);
    // murs de la salle
    [[0, -7.4, 9.2, .25], [0, 5.4, 9.2, .25], [-4.6, -1, .25, 12.8], [4.6, -1, .25, 12.8]].forEach(([x, z, w, d]) => { const m = new TH.Mesh(new TH.BoxGeometry(w, .6, d), mat('#fff')); m.position.set(x, .3, z); world.add(m); });
    const TB = [[-2.2, -5], [2.2, -5], [-2.2, -1], [2.2, -1], [-2.2, 3], [2.2, 3]].map(([x, z], i) => { const m = new TH.Mesh(new TH.CylinderGeometry(1.0, 1.0, .25, 28), mat('#fff')); m.position.set(x, .4, z); world.add(m);
      const lab = textSprite('T' + (i + 1), '#d6ecff'); lab.position.set(x, 1.2, z); lab.scale.setScalar(1.1); S.add(lab); return { m, x, z, lab }; });
    const seats = []; TB.forEach((tb, ti) => { const n = ti === 4 ? 12 : 8; for (let k = 0; k < n; k++) { const a = k / n * Math.PI * 2; const r = ti === 4 ? 1.6 : 1.45;
      const g = new TH.Mesh(new TH.SphereGeometry(.22, 14, 10), mat('#fff')); g.position.set(tb.x + Math.cos(a) * r, .3, tb.z + Math.sin(a) * r); world.add(g); seats.push({ g, ti, k, home: g.position.clone() }); } });
    // couple qui fait le plan (dessiné au trait)
    const bride = blob({ kind: 'cat', color: '#fff', veil: 0 }), groom = blob({ kind: 'dog', color: '#fff', bow: '#fff' });
    bride.g.position.set(-1.2, 0, 6.6); groom.g.position.set(1.2, 0, 6.6); bride.g.scale.setScalar(.9); groom.g.scale.setScalar(.9); world.add(bride.g, groom.g);
    blueprint(world);
    // conflit : oncle (T2) et tante (T2) côte à côte ; T5 = 12/10
    const uncle = seats.find(s_ => s_.ti === 1 && s_.k === 2), aunt = seats.find(s_ => s_.ti === 1 && s_.k === 3);
    const link = new TH.Line(new TH.BufferGeometry().setFromPoints([uncle.home, aunt.home]), new TH.LineDashedMaterial({ color: '#ff5d73', dashSize: .15, gapSize: .1 })); link.computeLineDistances(); link.position.y = .6; S.add(link);
    const extra = seats.filter(s_ => s_.ti === 4 && s_.k >= 10);
    // déplacements décidés par le couple : la tante vers T6, 2 invités de T5 vers T3 et T6
    const ring = (tb, a) => [TB[tb].x + Math.cos(a) * 1.45, .3, TB[tb].z + Math.sin(a) * 1.45]; const moves = [[aunt, ring(5, Math.PI / 8)], [extra[0], ring(3, Math.PI * 9 / 8)], [extra[1], ring(2, Math.PI * 3 / 8)]];
    const checks = TB.map(tb => { const c = textSprite('✓', '#2ee6a6'); c.position.set(tb.x + .9, 1.6, tb.z - .6); S.add(c); return c; });
    const SH = [[0, 3.4, { p: [0, 25, 8], l: [0, 0, -.6] }, { p: [0, 22.5, 7.4], l: [0, 0, -.6] }, 42],
      [3.4, 6.6, { p: [2.2, 10, -1.2], l: [2.2, 0, -5] }, { p: [-2.2, 10, 6.6], l: [-2.2, 0, 2.8] }, 42],
      [6.6, 9.0, { p: [0, 22.5, 7.4], l: [0, 0, -.6] }, { p: [0, 22.5, 7.4], l: [0, 0, -.6] }, 42],
      [9.0, 13.2, { p: [0, 21, 7.2], l: [0, 0, -.6] }, { p: [0, 23.5, 7.8], l: [0, 0, -.6] }, 42]];
    TB.forEach((tb, i) => window.__ev(.2 + i * .25, 'tick')); window.__ev(3.6, 'alert');
    return function (t) {
      const frz = t > 5.6 && t < 6.6; const ta = frz ? 5.6 : t; shots(SH, t);
      TB.forEach((tb, i) => { const p = cl(sp(ta, .2 + i * .25, 1.3), 0, 1.15); tb.m.scale.set(Math.max(.01, p), 1, Math.max(.01, p)); tb.lab.visible = p > .5;
        setLine(tb.m, i === 4 && ta > 3.4 && ta < 10.8 ? (Math.floor(ta * 4) % 2 ? '#ff5d73' : '#ffb3bd') : ta > 11 ? '#2ee6a6' : BP_LINE); });
      seats.forEach((s_, i) => { const ts = .8 + i * .025; const p = cl(sp(ta, ts, 1.5), 0, 1.2); s_.g.scale.setScalar(Math.max(.01, p)); s_.g.position.copy(s_.home);
        const red = (s_ === uncle || s_ === aunt) && ta > 3.4 && ta < 10.2;
        setLine(s_.g, red ? '#ff5d73' : ta > 11 ? '#2ee6a6' : BP_LINE); });
      moves.forEach(([s_, d], j) => { const ts = 9.3 + j * .35; const q = eio3(ln(ta, ts, ts + .8)); if (q > 0) { s_.g.position.set(s_.home.x + (d[0] - s_.home.x) * q, .3 + Math.sin(q * Math.PI) * 1.6, s_.home.z + (d[2] - s_.home.z) * q); } });
      link.visible = ta > 3.4 && ta < 9.4 && Math.floor(ta * 5) % 2 === 0;
      pose(bride, ta, ta < 3.4 ? 'happy' : ta < 9 ? 'shock' : ta < 11 ? 'point' : 'cheer', 0); pose(groom, ta, ta < 3.4 ? 'happy' : ta < 9 ? 'shock' : 'cheer', 1.3);
      checks.forEach((c, i) => { const p = cl(sp(ta, 11.0 + i * .1, 1.4), 0, 1.2); c.scale.setScalar(p * 1.1); c.visible = p > 0; });
    };
  };

  // ---------- silhouettes à l'encre devant un ciel dégradé ----------
  function silhouette(root) { root.traverse(o => { if (o.isMesh && !o.userData.glow && !o.userData.sky) { o.material = new TH.MeshBasicMaterial({ color: '#07040c' }); o.castShadow = o.receiveShadow = false; } }); }
  WORLDS.porch = function (cfg) {
    const skyU = { top: { value: new TH.Color('#2a1250') }, bot: { value: new TH.Color('#ff8a4c') } };
    const sky = new TH.Mesh(new TH.PlaneGeometry(80, 60), new TH.ShaderMaterial({ uniforms: skyU, depthWrite: false,
      vertexShader: 'varying float vy; void main(){ vy = uv.y; gl_Position = projectionMatrix * modelViewMatrix * vec4(position,1.0); }',
      fragmentShader: 'uniform vec3 top; uniform vec3 bot; varying float vy; void main(){ gl_FragColor = vec4(mix(bot, top, smoothstep(0.30, 0.75, vy)), 1.0); }' }));
    sky.position.set(0, 10, -30); sky.userData.sky = 1; S.add(sky);
    const sun = new TH.Mesh(new TH.CircleGeometry(4.2, 64), new TH.MeshBasicMaterial({ color: '#ffd27a' })); sun.userData.glow = 1; sun.position.set(-1.5, 4.5, -25); S.add(sun);
    const moon = new TH.Mesh(new TH.CircleGeometry(1.6, 48), new TH.MeshBasicMaterial({ color: '#fff4d6' })); moon.userData.glow = 1; moon.position.set(4.5, 15, -25); S.add(moon);
    const stars = []; for (let i = 0; i < 60; i++) { const st = new TH.Mesh(new TH.CircleGeometry(.05 + hash(i) * .06, 6), new TH.MeshBasicMaterial({ color: '#ffffff', transparent: true })); st.userData.glow = 1; st.position.set(-14 + hash(i + 1) * 28, 8 + hash(i + 2) * 16, -24); S.add(st); stars.push(st); }
    const W = new TH.Group(); S.add(W);
    const ground = new TH.Mesh(new TH.PlaneGeometry(80, 30), mat('#000')); ground.rotation.x = -Math.PI / 2; W.add(ground);
    
    // maison à droite
    const house = new TH.Group(); const hb = new TH.Mesh(new TH.BoxGeometry(5, 4.2, 4), mat('#000')); hb.position.y = 2.1; house.add(hb);
    const rf = new TH.Mesh(new TH.ConeGeometry(3.9, 2.4, 4), mat('#000')); rf.position.y = 5.4; rf.rotation.y = Math.PI / 4; house.add(rf);
    const ch = new TH.Mesh(new TH.BoxGeometry(.6, 1.6, .6), mat('#000')); ch.position.set(1.3, 5.6, 0); house.add(ch);
    house.position.set(4.6, 0, -4); W.add(house);
    const wins = []; [[-1.2, 1.4], [1.2, 1.4], [-1.2, 3.1], [1.2, 3.1]].forEach(([x, y], i) => { const w = new TH.Mesh(new TH.PlaneGeometry(.95, .85), new TH.MeshBasicMaterial({ color: '#ffcf6a' })); w.userData.glow = 1; w.position.set(4.6 + x, y, -1.98); S.add(w); wins.push(w); });
    // deux arbres + hamac
    const tree = (x) => { const g = new TH.Group(); const tr = new TH.Mesh(new TH.CylinderGeometry(.18, .3, 4.2, 8), mat('#000')); tr.position.y = 2.1; g.add(tr);
      for (let k = 0; k < 5; k++) { const b = new TH.Mesh(new TH.SphereGeometry(.75 + hash(x + k) * .35, 12, 10), mat('#000')); b.position.set((hash(k + x * 3) - .5) * 1.6, 4.5 + hash(k + 9) * .9, 0); g.add(b); } g.position.set(x, 0, -1); W.add(g); };
    tree(-4.3); tree(.1);
    const ham = new TH.Mesh(new TH.TorusGeometry(2.3, .09, 6, 24, Math.PI), mat('#000')); ham.rotation.z = Math.PI; ham.position.set(-2.1, 2.9, -1); ham.scale.y = .35; W.add(ham);
    const cat = blob({ kind: 'cat', color: '#000' }); W.add(cat.g);
    const phone = new TH.Mesh(new TH.PlaneGeometry(.32, .5), new TH.MeshBasicMaterial({ color: '#9fe7ff' })); phone.userData.glow = 1; S.add(phone);
    const dog = blob({ kind: 'dog', color: '#000', s: .45 }); dog.g.position.set(4.6 + 1.2, .9, -1.9); W.add(dog.g);
    silhouette(W); silhouette(cat.g);
    CAM.position.set(0, 3.2, 13); CAM.lookAt(0, 3.4, -2);
    const C1 = [new TH.Color('#3a1a6a'), new TH.Color('#ff7a3c')], C2 = [new TH.Color('#0a0b2a'), new TH.Color('#5a42a8')], C3 = [new TH.Color('#2b3a8a'), new TH.Color('#ffb37a')];
    const SH = [[0, 3.3, { p: [0, 1.1, 15], l: [-.6, 3.0, -2] }, { p: [-.8, 1.0, 12.5], l: [-1.2, 2.9, -2] }, 40],
      [3.3, 6.6, { p: [-2.0, 1.0, 8.5], l: [-1.6, 2.4, -1] }, { p: [-1.6, .9, 7.6], l: [-1.4, 2.2, -1] }, 40],
      [6.6, 9.0, { p: [0, 1.1, 15], l: [0, 3, -2] }, { p: [0, 1.1, 15], l: [0, 3, -2] }, 40],
      [9.0, 13.2, { p: [.4, 1.2, 16.5], l: [0, 3.1, -2] }, { p: [-.6, 1.0, 13], l: [-1.0, 3.0, -2] }, 40]];
    [3.4, 3.8, 4.2].forEach(a => window.__ev(a, 'ping'));
    return function (t) { shots(SH, t);
      const night = ln(t, 1.8, 3.4), dawn = ln(t, 9.0, 10.6);
      const top = C1[0].clone().lerp(C2[0], night).lerp(C3[0], dawn), bot = C1[1].clone().lerp(C2[1], night).lerp(C3[1], dawn);
      skyU.top.value.copy(top); skyU.bot.value.copy(bot);
      sun.position.y = 4.5 - night * 9 + dawn * 7.5; sun.material.color.set(dawn > 0 ? '#ffe2a0' : '#ffd27a'); moon.visible = night > .3 && dawn < .6;
      stars.forEach((st, i) => { st.material.opacity = night * (1 - dawn) * (.5 + .5 * Math.sin(t * 3 + i)); });
      wins.forEach((w, i) => { w.visible = t > 2.2 + i * .15 && t < 10.2; });
      // chat : dans le hamac (balance) -> saute en bas avec le téléphone -> retour au hamac
      const out = t > 3.3 && t < 9.0;
      if (!out) { const sw = Math.sin(t * 1.4) * .12; cat.g.position.set(-2.1 + sw, 2.0, -1); cat.g.rotation.set(0, 0, -1.25 + sw * .3); pose(cat, t, t > 11 ? 'happy' : 'idle', 0); }
      else { const j = eo3(ln(t, 3.3, 3.8)); cat.g.position.set(-2.1 + j * .4, 2.0 * (1 - j) + Math.sin(j * Math.PI) * 1.0, -1 + j * 2.5); cat.g.rotation.set(0, 0, -1.25 * (1 - j)); pose(cat, t, 'shock', 0); }
      const hand = new TH.Vector3(); cat.arms[1].children[0].getWorldPosition(hand); phone.position.copy(hand); phone.position.z += .25; phone.position.y += .1;
      phone.visible = t > 2.6 && t < 9.0; phone.material.color.set(Math.floor(t * 8) % 2 && t < 6.6 ? '#ffffff' : '#9fe7ff'); phone.rotation.z = t < 6.6 ? Math.sin(t * 40) * .15 : 0;
      dog.g.visible = t > 3.0 && t < 10.2; pose(dog, t, 'happy', 2);
    };
  };

  // ---------- installation ----------
  window.initWorld = function (cfg) {
    LOOK = cfg.look || 'clay';
    const pix = LOOK === 'pixel';
    cv = document.createElement('canvas'); cv.style.cssText = 'position:absolute;left:0;top:0;width:1080px;height:1920px;z-index:0' + (pix ? ';image-rendering:pixelated' : '');
    const stage = document.getElementById('stage'); stage.insertBefore(cv, stage.firstChild);
    R = new TH.WebGLRenderer({ canvas: cv, antialias: !pix, preserveDrawingBuffer: true });
    R.setPixelRatio(1); R.setSize(pix ? 216 : 1080, pix ? 384 : 1920, false);
    R.shadowMap.enabled = LOOK !== 'stick' && LOOK !== 'blueprint' && LOOK !== 'silhouette'; R.shadowMap.type = LOOK === 'clay' || LOOK === 'film' || LOOK === 'paper' ? TH.PCFSoftShadowMap : TH.BasicShadowMap;
    R.toneMapping = TH.ACESFilmicToneMapping; R.toneMappingExposure = LOOK === 'clay' ? 1.05 : LOOK === 'film' ? 1.1 : 1.15; R.outputColorSpace = TH.SRGBColorSpace;
    S = new TH.Scene(); CAM = new TH.PerspectiveCamera(38, 1080 / 1920, .1, 100);
    window.__ev = (t, type) => ev(t, type);
    W = WORLDS[cfg.world](cfg);
    // stop-motion : la pâte à modeler bouge à 12 images/s (saccade typique), le reste à 30
    on(t => { const ta = LOOK === 'clay' || LOOK === 'cardboard' ? Math.floor(t * 12) / 12 : t; if (t >= (cfg.endAt || 99)) return; W(ta);
      if (LOOK === 'clay') { const j = Math.floor(t * 12); CAM.position.x += (hash(j) - .5) * .015; CAM.position.y += (hash(j + 3) - .5) * .015; }
      R.render(S, CAM); });
  };
})();
