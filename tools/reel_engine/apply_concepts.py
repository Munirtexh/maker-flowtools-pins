"""Place les 6 concepts (build_concepts.PLACE) et décale les reels qu'ils remplacent (build_concepts.MOVE).
Archive manifest.json et calendar.csv d'abord. Aucune publication ne disparaît."""
import json, os, sys, shutil, csv, io, datetime
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.abspath(os.path.join(here, '..', '..'))
sys.path.insert(0, here); import build_concepts as BC
RAW = 'https://raw.githubusercontent.com/Munirtexh/maker-flowtools-pins/main/'
cap = json.load(open(os.path.join(here, 'concepts_captions.json')))
man_p, cal_p = os.path.join(root, 'ig/manifest.json'), os.path.join(root, 'ig/calendar.csv')
day = datetime.date.today().isoformat()
for p, nm in ((man_p, f'manifest_avant_concepts_{day}.json'), (cal_p, f'calendar_avant_concepts_{day}.csv')):
    a = os.path.join(root, 'ig/archive', nm)
    if not os.path.exists(a): shutil.copy(p, a)
man = json.load(open(man_p)); by = {p['id']: p for p in man}
F = ('type', 'url', 'cover', 'caption', 'needs', 'repeat')
old = {k: {f: by[k][f] for f in F} for k in BC.MOVE}
for src, dst in BC.MOVE.items():  # le reel déplacé prend la place de l'image du créneau cible (l'image part dans l'archive)
    by[dst].update(old[src])
for slot, rid in BC.PLACE.items():
    by[slot].update(type='reel', url=RAW + f'videos/concepts/{rid}.mp4', cover=RAW + f'videos/concepts/{rid}_cover.jpg', caption=cap[rid], needs='', repeat=False)
json.dump(man, open(man_p, 'w'), ensure_ascii=False, indent=1)
raw = open(cal_p, encoding='utf-8-sig', newline='').read(); rows = list(csv.reader(io.StringIO(raw)))
for r in rows[1:]:
    if r and r[0] in by and r[0] in set(BC.PLACE) | set(BC.MOVE.values()):
        p = by[r[0]]; r[2] = p['type']; r[3] = p['url'].split('/main/')[1]; r[4] = ''; r[5] = 'False'; r[6] = p['caption'].replace('\n', ' | ')
out = io.StringIO(); csv.writer(out, lineterminator='\r\n').writerows(rows)
open(cal_p, 'w', encoding='utf-8-sig', newline='').write(out.getvalue())
print('placés', BC.PLACE); print('déplacés', BC.MOVE)
