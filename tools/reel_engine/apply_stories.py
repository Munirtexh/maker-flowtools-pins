"""Place des reels « histoire » : python3 apply_stories.py S1_factory_landlord_EN=d12B [...] [--move d12B:d26B ...]
--move déplace d'abord le reel du créneau source vers un créneau cible (qui contient une image, gardée dans l'archive).
Archive manifest.json et calendar.csv avant (ig/archive/*_avant_stories_<date>_<heure>.*)."""
import json, os, sys, shutil, csv, io, datetime
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.abspath(os.path.join(here, '..', '..'))
RAW = 'https://raw.githubusercontent.com/Munirtexh/maker-flowtools-pins/main/'
cap = json.load(open(os.path.join(here, 'stories_captions.json')))
args = sys.argv[1:]; mv = [a.split(':') for a in args[args.index('--move') + 1:]] if '--move' in args else []
pl = [a.split('=') for a in (args[:args.index('--move')] if '--move' in args else args)]
man_p, cal_p = os.path.join(root, 'ig/manifest.json'), os.path.join(root, 'ig/calendar.csv')
st = datetime.datetime.now().strftime('%Y-%m-%d_%H%M')
for p, nm in ((man_p, f'manifest_avant_stories_{st}.json'), (cal_p, f'calendar_avant_stories_{st}.csv')):
    shutil.copy(p, os.path.join(root, 'ig/archive', nm))
man = json.load(open(man_p)); by = {p['id']: p for p in man}
F = ('type', 'url', 'cover', 'caption', 'needs', 'repeat'); touched = set()
old = {a: {f: by[a][f] for f in F} for a, b in mv}
for a, b in mv:
    assert by[b]['type'] == 'image', f'{b} n\'est pas une image'
    by[b].update(old[a]); touched.add(b)
for rid, slot in pl:
    by[slot].update(type='reel', url=RAW + f'videos/stories/{rid}.mp4', cover=RAW + f'videos/stories/{rid}_cover.jpg', caption=cap[rid], needs='', repeat=False); touched.add(slot)
json.dump(man, open(man_p, 'w'), ensure_ascii=False, indent=1)
raw = open(cal_p, encoding='utf-8-sig', newline='').read(); rows = list(csv.reader(io.StringIO(raw)))
for r in rows[1:]:
    if r and r[0] in touched:
        p = by[r[0]]; r[2] = p['type']; r[3] = p['url'].split('/main/')[1]; r[4] = ''; r[5] = 'False'; r[6] = p['caption'].replace('\n', ' | ')
out = io.StringIO(); csv.writer(out, lineterminator='\r\n').writerows(rows)
open(cal_p, 'w', encoding='utf-8-sig', newline='').write(out.getvalue())
print('placés', pl, 'déplacés', mv)
