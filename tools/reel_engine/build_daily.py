"""2e reel quotidien (19 h 30), format 15 s hook / body / fin, langue opposée à celle du jour.
Proposé le 4 nov. 2026 (Yaacoub : « 2 reels par jour, les programmés + les nouveaux »). Produit daily.json + daily_captions.json."""
import json, os, sys
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)
import build_trends as B
NB = ' '
base = {r['id']: r for r in json.load(open(os.path.join(here, 'reels.json')))['reels']}
ex = {r['id']: r for r in json.load(open(os.path.join(here, 'examples', 'examples.json')))['reels']}
D, CAP = {}, {}
def eng(rid, src, hook, hl, callout, music, floats=(), btns=None, emoji=None):
    r = dict(base[src]); r.update(id=rid, trend=True, dur=15, music=music, callout=callout, hook=hook, hl=hl, coverAt=7.5)
    if emoji: r['emoji'] = emoji
    r['floats'] = list(r['floats']) + list(floats)
    r['cta'] = dict(r['cta'])
    if btns: r['cta']['btns'] = btns
    r.pop('slot', None); D[rid] = r
# --- semaine 1 ---
for k, new in (('EXA_tresorier_FR', 'N05_tresorier_FR'), ('EXB_landlord_EN', 'N06_landlord_EN'), ('EXC_seat_FR', 'N07_seat_FR')):
    r = dict(ex[k]); r['id'] = new; r.pop('previewTimes', None); D[new] = r
CAP['N05_tresorier_FR'] = "La banque dit 1 842 $, tes livres 1 597 $ 😳\nÇa t'est déjà arrivé ? 👇\nEnvoie ça au trésorier de ton comité.\nKit Trésorier (Excel) : l'onglet Conciliation ramène l'écart à 0,00 étape par étape.\n💬 Écris KIT en commentaire et je te réponds avec le lien.\n👉 Ou lien dans la bio\n#trésorier #association #clubétudiant #cégep #budget #conciliationbancaire"
CAP['N06_landlord_EN'] = "Landlords, be honest: $980 missing and you don't know who? 😬\nWhat's your system: sticky notes, notebook or spreadsheet? 👇\nSend this to a landlord friend 🏠\nLandlord Kit (Excel): paid, partial or unpaid for every unit, every month.\n👉 Link in bio\n#landlord #rentalproperty #realestateinvesting #propertymanagement #excel #canada"
CAP['N07_seat_FR'] = "POV : ta mère t'envoie SA liste d'invités et tes deux ex sont invités 😬\nC'est qui, ton cas à placer ? 👇\nEnvoie ça à ta témoin 💍\nSeat & Vow (Excel) : tu décides qui s'assoit où, le classeur compte et te prévient.\n👉 Lien dans la bio\n#mariage #plandetable #mariagequébec #organisationmariage #fiancée #mariage2027"
eng('N08_habit_EN', 'H1_EN', 'Missed one day and quit the whole thing?', [1, 2, 5, 6], '2027 goals 👀', 'future',
    floats=[dict(t=5.4, text='Done · minimum · rest ✓', x=80, y=1480, c='y', rot=-6), dict(t=7.0, text='Your year at a glance 📅', x=560, y=1480, c='b', rot=6)],
    btns=['👉 Link in bio', '📤 Send to your gym buddy'], emoji='😩')
CAP['N08_habit_EN'] = "Missed one day and quit the whole thing? 😩\nBe honest, what habit did you drop this year? 👇\nSend this to your accountability buddy 🤝\nRhythm Habit Tracker 2027 (Excel): done, minimum version or planned rest. A missed day stays blank, no guilt.\n👉 Link in bio\n#habittracker #2027goals #newyearresolution #productivity #selfimprovement #excel"
D['N09_artisan_FR'] = dict(id='N09_artisan_FR', engine='trend.html', format='sortChaos', theme='artisan', lang='fr', dur=15, music='tropical', seed=74, coverAt=6.5,
  end=dict(name='Artisan Empire 360°', sub='Excel · FR / EN · sans macros', btn='👉 Lien dans la bio', btn2='📤 Envoie-le à une artisane'),
  t=dict(B.FR, l1='POV: les marchés de Noël commencent', l2a='et tes prix sont au pif 😬', hl2a=[2, 4], l2b='alors le classeur fait le calcul ✨', hl2b=[2, 5],
    items=[B.it('Bougie soja', 'coût 17,85 $', '29,75 $', 'g'), B.it('Savon lavande', 'coût 6,10 $', '10,17 $', 'b'), B.it('Tuque tricotée', 'coût 21,40 $', '35,67 $', 'y'),
           B.it('Carte florale', 'coût 3,20 $', '5,33 $', 'p'), B.it('Tasse en céramique', 'coût 12,60 $', '21,00 $', 'o'), B.it('Sac en tissu', 'coût 9,30 $', '15,50 $', 'k')],
    total=dict(l='Marge visée', v=40, f='pct', c='y'), wtitle='Prix suggéré · marge 40 %', warn='❓ Je demande combien ?', stamp='Tout est compté ✓',
    beats=[dict(text='Matériaux + emballage + frais + ton temps', c='y', x=40, y=640, rot=-4), dict(text='Verdict par marché 🎪', c='g', x=420, y=1560, rot=5),
           dict(text='Alerte de stock bas 🔔', c='r', x=120, y=1100, rot=-4)],
    file='Artisan_Empire_360.xlsx', brand='Artisan Empire 360° · Maker FlowTools'))
CAP['N09_artisan_FR'] = "POV : les marchés de Noël commencent et tes prix sont au pif 😬\nComment tu fixes tes prix, honnêtement ? 👇\nEnvoie ça à une artisane avant son prochain marché 🎪\nArtisan Empire 360° (Excel) : matériaux, emballage, frais et ton temps, puis un prix suggéré.\n👉 Lien dans la bio\n#artisan #faitmain #marchédenoël #créatrice #etsyquébec #petiteentreprise"
r = dict(ex['EXC_seat_FR']); r = json.loads(json.dumps(r)); r.update(id='N10_seat_EN', lang='en', seed=49, music='pop'); r.pop('previewTimes', None)
r['end'] = dict(name='Seat &amp; Vow', sub='Wedding seating planner<br>Excel · EN / FR', btn='👉 Link in bio', btn2='📤 Send to your maid of honor')
r['t'] = dict(B.EN, l1='POV: your mom sends you HER guest list', l2a='and both of your exes are invited 😬', hl2a=[2, 4], l2b='so the spreadsheet warns me ✨', hl2b=[2, 3],
  guests=B.G, clash=['Jake', 'Tyler'], warn='⚠️ Conflict!', stamp='Kept apart ✓',
  beats=[dict(text='🍽️ Meals counted for the caterer', c='y', x=50, y=600, rot=-5), dict(text='🪧 Table cards ready to print', c='b', x=360, y=1600, rot=5),
         dict(text='🇨🇦 EN / FR in one cell', c='p', x=160, y=1110, rot=-4)], file='Seat_and_Vow.xlsx', brand='Seat & Vow · Maker FlowTools')
D['N10_seat_EN'] = r
CAP['N10_seat_EN'] = "POV: your mom sends you HER guest list and both of your exes are invited 😬\nWho's the guest you can't seat? 👇\nSend this to your maid of honor 💍\nSeat & Vow (Excel): you decide who sits where, the workbook counts and warns you.\n👉 Link in bio\n#weddingplanning #seatingchart #wedding #bride2027 #engaged #weddingtips"
eng('N11_landlord_FR', 'L3_FR', f'Un bail finit dans 45{NB}jours. Tu l\'avais vu ?', [3, 4], 'Proprios 👀', 'funk',
    floats=[dict(t=5.6, text='Échéances en couleur 🟢🟡🔴', x=80, y=1480, c='y', rot=-6), dict(t=7.2, text='Rappel avant la fin ✓', x=560, y=640, c='g', rot=6)],
    btns=['👉 Lien dans la bio', '📤 Envoie-le à un proprio'], emoji='😳')
CAP['N11_landlord_FR'] = "Un bail finit dans 45 jours. Tu l'avais vu ? 😳\nTu suis tes baux comment, toi ? 👇\nEnvoie ça à un proprio 🏠\nKit Propriétaire (Excel) : chaque bail avec sa date de fin et un rappel avant l'échéance.\n👉 Lien dans la bio\n#propriétaire #immobilier #plex #québec #bail #excel"
# créneau du soir (local Montréal) -> reel
EVENING = {'2026-11-05': 'N05_tresorier_FR', '2026-11-06': 'N06_landlord_EN', '2026-11-07': 'N07_seat_FR', '2026-11-08': 'N08_habit_EN',
           '2026-11-09': 'N09_artisan_FR', '2026-11-10': 'N10_seat_EN', '2026-11-11': 'N11_landlord_FR'}
if __name__ == '__main__':
    reels = list(D.values())
    for r in reels: r.setdefault('previewTimes', [0, 1.7, 4, 6.5, 9, 11.5, 13.5])
    json.dump({'reels': reels}, open(os.path.join(here, 'daily.json'), 'w'), ensure_ascii=False, indent=1)
    json.dump(CAP, open(os.path.join(here, 'daily_captions.json'), 'w'), ensure_ascii=False, indent=1)
    print(len(reels), 'reels', sorted(CAP) == sorted(D))
