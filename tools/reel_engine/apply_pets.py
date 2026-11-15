"""Semaine du 16 au 22 nov. 2026 : nouveau style « animaux au travail » (build_pets.py) aux créneaux de 19 h 30,
une vidéo gardée par ancien style à 12 h 30 (E2 duo, N10 quotidien, TR07 tendance, T1 animé), images remises jeu.-sam. 12 h 30.
Les autres reels de la semaine sortent du calendrier (gardés dans ig/archive/*_avant_pets_*). Usage : python3 apply_pets.py"""
import json, os, shutil, csv, io, datetime, build_pets
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.abspath(os.path.join(here, '..', '..'))
RAW = 'https://raw.githubusercontent.com/Munirtexh/maker-flowtools-pins/main/'
man_p, cal_p = os.path.join(root, 'ig/manifest.json'), os.path.join(root, 'ig/calendar.csv')
st = datetime.datetime.now().strftime('%Y-%m-%d_%H%M')
for p, nm in ((man_p, f'manifest_avant_pets_{st}.json'), (cal_p, f'calendar_avant_pets_{st}.csv')):
    shutil.copy(p, os.path.join(root, 'ig/archive', nm))
man = json.load(open(man_p)); by = {p['id']: p for p in man}
F = ('type', 'url', 'cover', 'caption', 'needs', 'repeat'); touched = set()
old19 = {f: by['d18B'][f] for f in F}                       # N10_seat_EN (style « quotidien ») → d19A
src = {p['id']: p for p in json.load(open(os.path.join(root, 'ig/archive/manifest_avant_reels_19h30_2026-11-04.json')))}
by['d19A'].update(old19); touched.add('d19A')
for dst, s in (('d21A', 'd21B'), ('d22A', 'd22B'), ('d23A', 'd23B')):   # images d'origine, même langue que le créneau
    by[dst].update({f: src[s][f] for f in F}); touched.add(dst)
for rid, slot in build_pets.PLACE.items():
    by[slot].update(type='reel', url=RAW + f'videos/pets/{rid}.mp4', cover=RAW + f'videos/pets/{rid}_cover.jpg',
                    caption=build_pets.CAP[rid], needs='', repeat=False); touched.add(slot)
json.dump(man, open(man_p, 'w'), ensure_ascii=False, indent=1)
raw = open(cal_p, encoding='utf-8-sig', newline='').read(); rows = list(csv.reader(io.StringIO(raw)))
for r in rows[1:]:
    if r and r[0] in touched:
        p = by[r[0]]; r[2] = p['type']; r[3] = p['url'].split('/main/')[1]; r[4] = ''; r[5] = 'False'; r[6] = p['caption'].replace('\n', ' | ')
out = io.StringIO(); csv.writer(out, lineterminator='\r\n').writerows(rows)
open(cal_p, 'w', encoding='utf-8-sig', newline='').write(out.getvalue())
print('modifiés', sorted(touched))
