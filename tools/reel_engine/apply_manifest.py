"""Points the calendar slots in SLOTS to the new animated reels (url, cover, caption) and rewrites ig/calendar.csv.
Run after render.js. Keeps every entry, time and id; only url/cover/caption of the listed slots change."""
import json, csv, os, sys, shutil
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.join(here, '..', '..')
sys.path.insert(0, here)
from build_configs import SLOTS
RAW = 'https://raw.githubusercontent.com/Munirtexh/maker-flowtools-pins/main/'
caps = json.load(open(os.path.join(here, 'captions.json')))
mp = os.path.join(root, 'ig', 'manifest.json'); man = json.load(open(mp))
os.makedirs(os.path.join(root, 'ig', 'covers', 'anim'), exist_ok=True)
n = 0
for e in man:
    if e['id'] not in SLOTS: continue
    cid, lg = SLOTS[e['id']]; rid = f'{cid}_{lg.upper()}'
    vid = os.path.join(root, 'videos', 'anim', rid + '.mp4'); cov = os.path.join(root, 'videos', 'anim', rid + '_cover.jpg')
    assert os.path.exists(vid), vid
    if os.path.exists(cov): shutil.move(cov, os.path.join(root, 'ig', 'covers', 'anim', rid + '.jpg'))
    e['type'] = 'reel'; e['url'] = RAW + f'videos/anim/{rid}.mp4'; e['cover'] = RAW + f'ig/covers/anim/{rid}.jpg'
    e['caption'] = caps[e['id']]; n += 1
json.dump(man, open(mp, 'w'), ensure_ascii=False, indent=1)
with open(os.path.join(root, 'ig', 'calendar.csv'), 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.writer(f); w.writerow(['id', 'date_heure_Montreal', 'format', 'fichier', 'necessite_P5', 'reprise', 'legende'])
    for e in man:
        w.writerow([e['id'], e['local'], e['type'], e['url'].replace(RAW, ''), e.get('needs', ''), e.get('repeat', False), e['caption'].replace('\n', ' | ')])
print(n, 'slots updated;', len(man), 'entries kept')
