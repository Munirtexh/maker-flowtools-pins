"""Remplace les posts image de 19 h 30 par les nouveaux reels quotidiens (build_daily.EVENING).
Archive manifest.json et calendar.csv avant (une seule fois par jour)."""
import json, os, sys, shutil, csv, io, datetime
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.abspath(os.path.join(here, '..', '..'))
sys.path.insert(0, here); import build_daily as BD
RAW = 'https://raw.githubusercontent.com/Munirtexh/maker-flowtools-pins/main/'
cap = json.load(open(os.path.join(here, 'daily_captions.json')))
man_p, cal_p = os.path.join(root, 'ig/manifest.json'), os.path.join(root, 'ig/calendar.csv')
day = datetime.date.today().isoformat()
for p, ext in ((man_p, 'json'), (cal_p, 'csv')):
    a = os.path.join(root, 'ig/archive', f"{'manifest' if ext == 'json' else 'calendar'}_avant_reels_19h30_{day}.{ext}")
    if not os.path.exists(a): shutil.copy(p, a)
man = json.load(open(man_p)); byd = {}
for p in man:
    if p['local'].endswith('19:30'): byd[p['local'][:10]] = p
done = {}
for d, rid in BD.EVENING.items():
    p = byd[d]; mp4 = f'videos/daily/{rid}.mp4'
    if not os.path.exists(os.path.join(root, mp4)): print('manque', mp4); continue
    p.update(type='reel', url=RAW + mp4, cover=RAW + f'videos/daily/{rid}_cover.jpg', caption=cap[rid], needs='', repeat=False)
    done[p['id']] = (mp4, cap[rid])
json.dump(man, open(man_p, 'w'), ensure_ascii=False, indent=1)
raw = open(cal_p, encoding='utf-8-sig', newline='').read()
rows = list(csv.reader(io.StringIO(raw)))
for r in rows[1:]:
    if r and r[0] in done:
        r[2], r[3], r[4], r[5], r[6] = 'reel', done[r[0]][0], '', 'False', done[r[0]][1].replace('\n', ' | ')
out = io.StringIO(); csv.writer(out, lineterminator='\r\n').writerows(rows)
open(cal_p, 'w', encoding='utf-8-sig', newline='').write(out.getvalue())
print('remplacés', sorted(done))
