"""Place un lot de reels duo (module build_duosN.PLACE) à la place des vieilles vidéos fond blanc de 12 h 30.
Usage : python3 apply_duos2.py build_duos2   — archive manifest.json et calendar.csv d'abord (l'ancienne vidéo reste dans l'archive)."""
import json, os, sys, shutil, csv, io, datetime, importlib
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.abspath(os.path.join(here, '..', '..'))
sys.path.insert(0, here); mod = sys.argv[1] if len(sys.argv) > 1 else 'build_duos2'; BC = importlib.import_module(mod)
RAW = 'https://raw.githubusercontent.com/Munirtexh/maker-flowtools-pins/main/'
cap = json.load(open(os.path.join(here, mod.replace('build_', '') + '_captions.json')))
man_p, cal_p = os.path.join(root, 'ig/manifest.json'), os.path.join(root, 'ig/calendar.csv')
day = datetime.date.today().isoformat()
for p, nm in ((man_p, f'manifest_avant_{mod}_{day}.json'), (cal_p, f'calendar_avant_{mod}_{day}.csv')):
    a = os.path.join(root, 'ig/archive', nm)
    if not os.path.exists(a): shutil.copy(p, a)
man = json.load(open(man_p)); by = {p['id']: p for p in man}
for slot, rid in BC.PLACE.items():
    by[slot].update(type='reel', url=RAW + f'videos/duos/{rid}.mp4', cover=RAW + f'videos/duos/{rid}_cover.jpg', caption=cap[rid], needs='', repeat=False)
json.dump(man, open(man_p, 'w'), ensure_ascii=False, indent=1)
raw = open(cal_p, encoding='utf-8-sig', newline='').read(); rows = list(csv.reader(io.StringIO(raw)))
for r in rows[1:]:
    if r and r[0] in BC.PLACE:
        p = by[r[0]]; r[2] = p['type']; r[3] = p['url'].split('/main/')[1]; r[4] = ''; r[5] = 'False'; r[6] = p['caption'].replace('\n', ' | ')
out = io.StringIO(); csv.writer(out, lineterminator='\r\n').writerows(rows)
open(cal_p, 'w', encoding='utf-8-sig', newline='').write(out.getvalue())
print('placés', BC.PLACE)
