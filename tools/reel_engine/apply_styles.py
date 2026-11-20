"""Place les reels « un style par jour » (build_styles.py) à leur créneau de 19 h 30 (PLACE), seulement si la vidéo
existe dans videos/styles/. Archive manifest.json et calendar.csv avant (ig/archive/*_avant_styles_<date>_<heure>.*).
Usage : python3 apply_styles.py [id ...]   (sans id : tous ceux qui sont rendus)"""
import json, os, sys, shutil, csv, io, datetime, build_styles as B
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.abspath(os.path.join(here, '..', '..'))
RAW = 'https://raw.githubusercontent.com/Munirtexh/maker-flowtools-pins/main/'
ids = sys.argv[1:] or [k for k in B.PLACE if os.path.exists(os.path.join(root, 'videos/styles', k + '.mp4'))]
man_p, cal_p = os.path.join(root, 'ig/manifest.json'), os.path.join(root, 'ig/calendar.csv')
st = datetime.datetime.now().strftime('%Y-%m-%d_%H%M')
for p, nm in ((man_p, f'manifest_avant_styles_{st}.json'), (cal_p, f'calendar_avant_styles_{st}.csv')):
    shutil.copy(p, os.path.join(root, 'ig/archive', nm))
man = json.load(open(man_p)); by = {p['id']: p for p in man}; touched = set()
for rid in ids:
    slot = B.PLACE[rid]
    by[slot].update(type='reel', url=RAW + f'videos/styles/{rid}.mp4', cover=RAW + f'videos/styles/{rid}_cover.jpg', caption=B.CAP[rid], needs='', repeat=False); touched.add(slot)
json.dump(man, open(man_p, 'w'), ensure_ascii=False, indent=1)
raw = open(cal_p, encoding='utf-8-sig', newline='').read(); rows = list(csv.reader(io.StringIO(raw)))
for r in rows[1:]:
    if r and r[0] in touched:
        p = by[r[0]]; r[2] = p['type']; r[3] = p['url'].split('/main/')[1]; r[4] = ''; r[5] = 'False'; r[6] = p['caption'].replace('\n', ' | ')
out = io.StringIO(); csv.writer(out, lineterminator='\r\n').writerows(rows)
open(cal_p, 'w', encoding='utf-8-sig', newline='').write(out.getvalue())
print('placés', {i: B.PLACE[i] for i in ids})
