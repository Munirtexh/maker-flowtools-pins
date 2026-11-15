"""Style de la semaine du 16 au 22 nov. 2026 : « animaux au travail », façon vidéos IA virales (chiens qui font le café,
chats en tenue, etc.). Animaux humanisés (moteur story.html, option sp=), look ciné (grain, vignette, étalonnage chaud),
une légende mème fixe en haut pendant toute la vidéo, dialogues en bulles, gros plan sur le classeur (données d'exemple).
Produit pets.json + pets_captions.json. Placement : apply_stories.py avec --dir pets (voir PLACE)."""
import json, os
here = os.path.dirname(os.path.abspath(__file__))
R, CAP = {}, {}
PT = [0.2, 1.8, 3.5, 5.0, 7.0, 9.0, 10.5, 12.2, 14]
def reel(lang, theme, music, seed, meme, mhl, scenes, end, brand, accent, a1, a2, memeFs=72):
    return dict(engine='story.html', theme=theme, lang=lang, dur=15, music=music, seed=seed, coverAt=1.0, endAt=13.0, cinema=True,
                meme=meme, mhl=mhl, memeFs=memeFs, accent=accent, a1=a1, a2=a2, previewTimes=PT, brand=brand, end=end, scenes=scenes)
CAT = dict(sp='cat', skin='#f0a35e', muzzle='#fff1df')
DOG = dict(sp='dog', skin='#d9a56b', dark='#8a5a33', muzzle='#fbe9d2')
DOG2 = dict(sp='dog', skin='#f4f1ea', dark='#c49a6c', muzzle='#ffffff')
RAC = dict(sp='raccoon', skin='#9a9aa6', dark='#3a3a46', muzzle='#e9e6e2')
OWL = dict(sp='owl', skin='#8a6a4a', dark='#5a4330', muzzle='#f3e3c8')
HAM = dict(sp='hamster', skin='#e8a35c', muzzle='#fff3e2')
EN_LL = dict(name='Landlord Kit', sub='Excel · EN / FR · no macros<br>Sample data in this video', btn='👉 Link in bio', btn2='📤 Send this to a landlord friend')
FR_LL = dict(name='Kit Propriétaire', sub='Excel · FR / EN · sans macros<br>Données d\'exemple dans cette vidéo', btn='👉 Lien dans la bio', btn2='📤 Envoie ça à un proprio')

# 1 · lun. 16 · EN · le chat proprio
R['P1_cat_landlord_EN'] = reel('en', 'landlord', 'funk', 301, 'POV: your landlord is a cat 🐱', [2, 3, 5], [
  dict(t0=0, t1=3.2, set='cozy', laptop=[330],
       chars=[dict(CAT, x=330, y=1320, s=1, outfit='suit', shirt='#2b2f55', tie='#2ee6a6', glasses=True, pose='think'),
              dict(DOG, x=800, y=1330, s=1, shirt='#5cc8ff', outfit='hoodie', pose='talk', enter=500, says=[[.5, 2.9, 'Rent is paid! 🐶']])]),
  dict(t0=3.2, t1=6.0, set='glow', screen=dict(file='Landlord_Kit.xlsx', sample='Sample data', title='Rent · November', top=330, step=.3,
       rows=[['Unit 1 · Biscuit', '$1,100', 'g', 'Paid ✓'], ['Unit 2 · Max', '$600 of $1,100', 'y', 'Partial'], ['Unit 3 · Luna', '$0 of $980', 'r', 'Unpaid']],
       total=['Received', 0, 1700, '$'], stamp='Partial 🐾')),
  dict(t0=6.0, t1=8.6, set='cozy', laptop=[330], shake=[.2, .7],
       chars=[dict(CAT, x=330, y=1320, s=1, outfit='suit', shirt='#2b2f55', tie='#2ee6a6', glasses=True, pose='angry', says=[[.2, 2.4, '$600 of $1,100. 😼']]),
              dict(DOG, x=800, y=1330, s=1, shirt='#5cc8ff', outfit='hoodie', pose='shock')]),
  dict(t0=8.6, t1=10.8, set='cozy', laptop=[330],
       chars=[dict(CAT, x=330, y=1320, s=1, outfit='suit', shirt='#2b2f55', tie='#2ee6a6', glasses=True, pose='proud'),
              dict(DOG, x=800, y=1330, s=1, shirt='#5cc8ff', outfit='hoodie', pose='sad', says=[[.2, 2.1, "I'll send the rest 🥲"]])],
       emojis=[['🐾', 480, 820, .9]]),
  dict(t0=10.8, t1=13.0, set='cozy', cap='Every landlord needs this cat 😼', hl=[1, 4], capO=dict(top=1500, fs=74), burst=.2,
       chars=[dict(CAT, x=540, y=1330, s=1.1, outfit='suit', shirt='#2b2f55', tie='#2ee6a6', glasses=True, pose='cheer')]),
], EN_LL, 'Landlord Kit · Maker FlowTools', '#0f5a52', '#2ee6a6', '#5cc8ff')
CAP['P1_cat_landlord_EN'] = "POV: your landlord is a cat 🐱\nTag the landlord who checks EVERYTHING 👇\nLandlord Kit (Excel): paid, partial or unpaid for every unit and every month. (Animated, sample data.)\n👉 Link in bio\n#landlord #catsofinstagram #rentalproperty #propertymanagement #funnycats #excel"

# 2 · mar. 17 · FR · le raton laveur trésorier
R['P2_raton_tresorier_FR'] = reel('fr', 'treasurer', 'pop', 302, 'Quand le raton laveur devient trésorier de l\'asso 🦝', [3, 4, 7], [
  dict(t0=0, t1=3.0, set='meeting',
       chars=[dict(OWL, x=260, y=1330, s=1, outfit='suit', shirt='#3b2c4f', tie='#ffc23d', pose='talk', says=[[.4, 2.8, 'On a combien ? 🦉']]),
              dict(RAC, x=790, y=1330, s=1, shirt='#ffc23d', pose='stress')],
       emojis=[['🧾', 640, 700, .5], ['🧾', 900, 760, .8], ['🧾', 760, 600, 1.1]]),
  dict(t0=3.0, t1=5.6, set='night', laptop=[540], shake=[.5, 1.4],
       notifs=[[.15, 'Banque', 'Solde : 2 480,00 $'], [.5, 'Livres', 'Total : 2 355,00 $ 😳'], [.85, 'Comité', 'L\'AG est demain !']],
       chars=[dict(RAC, x=540, y=1330, s=1, shirt='#ffc23d', pose='type')]),
  dict(t0=5.6, t1=8.6, set='glow', screen=dict(file='Kit_Tresorier.xlsx', sample='Données d\'exemple', title='Conciliation · octobre', top=330, step=.3,
       rows=[['Solde banque', '2 480,00 $', 'b', 'Relevé'], ['Livres', '2 355,00 $', 'y', 'À vérifier'], ['Dépôt non inscrit', '125,00 $', 'g', 'Trouvé ✓']],
       total=['Écart', 125, 0, '', ' $', 2], stamp='Écart : 0,00 $')),
  dict(t0=8.6, t1=13.0, set='meeting', cap='Meilleur trésorier. Vraiment. 🦝', hl=[0, 1], capO=dict(top=1500, fs=74), burst=1.8,
       chars=[dict(RAC, x=330, y=1330, s=1.05, shirt='#ffc23d', pose='proud', poses=[[1.8, 'cheer']], says=[[.2, 1.8, 'Écart : 0,00 $ 😎']]),
              dict(OWL, x=810, y=1330, s=1, outfit='suit', shirt='#3b2c4f', tie='#ffc23d', pose='shock', poses=[[1.8, 'clap']])]),
], dict(name='Kit Trésorier', sub='Excel · FR / EN · sans macros<br>Données d\'exemple dans cette vidéo', btn='👉 Lien dans la bio', btn2='💬 Écris KIT en commentaire'),
  'Kit Trésorier · Maker FlowTools', '#3a2380', '#ffc23d', '#b18cff', memeFs=66)
CAP['P2_raton_tresorier_FR'] = "Quand le raton laveur devient trésorier de l'asso 🦝\nIdentifie le trésorier de ton comité 👇\nKit Trésorier (Excel) : la conciliation compare la banque et les livres et t'aide à ramener l'écart à 0,00 $. (Animation, données d'exemple.)\n💬 Écris KIT en commentaire et je te réponds avec le lien.\n👉 Ou lien dans la bio\n#trésorier #association #ratonlaveur #clubétudiant #comité #budget"

# 3 · mer. 18 · EN · « Goodbye 2026 me, hello 2027 me » (tendance du moment), chiens
D26 = dict(DOG, shirt='#7a7f99', outfit='hoodie'); D27 = dict(DOG, shirt='#4dffb5')
R['P3_2027_habit_EN'] = reel('en', 'habit', 'future', 303, '2026 me saying goodbye to 2027 me 🥹', [0, 1, 6, 7], [
  dict(t0=0, t1=3.2, set='city',
       chars=[dict(D26, x=300, y=1330, s=1, pose='sad', says=[[.3, 3.0, "Don't quit in January 🥺"]], bubFs=40),
              dict(D27, x=780, y=1330, s=1, pose='proud')]),
  dict(t0=3.2, t1=5.4, set='city',
       chars=[dict(D26, x=300, y=1330, s=1, pose='sad'), dict(D27, x=780, y=1330, s=1, pose='talk', says=[[.2, 2.1, "I've got a plan. 📅"]])]),
  dict(t0=5.4, t1=8.4, set='glow', screen=dict(file='Rhythm_Habit_Tracker_2027.xlsx', sample='Sample data', title='January 2027 · run', top=330, step=.3,
       rows=[['Jan 14', 'Done', 'g', '✓'], ['Jan 15', 'missed', '#8f9bc0', 'blank · no guilt'], ['Jan 16', 'Minimum version', 'y', '10 min']],
       total=['January', 0, 27, '', ' / 31 days'], stamp='Keep going')),
  dict(t0=8.4, t1=9.2, set='black', card='December 31, 2027…', cardC='#4dffb5', mute=[0, .75]),
  dict(t0=9.2, t1=13.0, set='city', cap='We made it 🐶🏅', hl=[1, 2], capO=dict(top=1500, fs=80), burst=.3,
       chars=[dict(D26, x=300, y=1330, s=1, pose='clap'), dict(D27, x=780, y=1330, s=1.05, pose='cheer', rprop='🏅')]),
], dict(name='Rhythm Habit Tracker 2027', sub='Excel · EN / FR · no macros<br>Sample data in this video', btn='👉 Link in bio', btn2='📤 Send this to your 2027 buddy'),
  'Rhythm Habit Tracker 2027 · Maker FlowTools', '#0b4a33', '#4dffb5', '#ffd166')
CAP['P3_2027_habit_EN'] = "2026 me saying goodbye to 2027 me 🥹\nWhat's the ONE habit 2027 you is keeping? 👇\nSend this to your 2027 buddy 🤝\nRhythm Habit Tracker 2027 (Excel): done, minimum version or planned rest. A missed day stays blank, no guilt. (Animated, sample data.)\n👉 Link in bio\n#goodbye2026 #hello2027 #habittracker #newyearresolution #dogsofinstagram #excel"

# 4 · jeu. 19 · FR · chiens ET chats au même mariage
BRIDE = dict(CAT, skin='#f4f1ea', muzzle='#ffffff', outfit='dress', shirt='#ffffff', pants='#f3eefe', hat='veil')
GROOM = dict(DOG, outfit='suit', shirt='#20263f', tie='#ff7aa8')
R['P4_chiens_chats_seat_FR'] = reel('fr', 'seat', 'lofi', 304, 'Les chiens ET les chats au même mariage ? 🐱🐶', [1, 4, 5], [
  dict(t0=0, t1=3.0, set='hall',
       chars=[dict(DOG2, x=220, y=1340, s=.95, shirt='#5cc8ff', pose='laugh', haha=[[.2, 3]], hahaTxt='WOUF'),
              dict(CAT, x=540, y=1330, s=1, outfit='dress', shirt='#b18cff', pants='#5b3c8a', glasses=True, pose='stress'),
              dict(CAT, skin='#3a3a46', muzzle='#9a9aa6', x=870, y=1340, s=.95, shirt='#ff7aa8', pose='angry', haha=[[.4, 3]], hahaTxt='CHHH')]),
  dict(t0=3.0, t1=5.4, set='night', laptop=[540],
       notifs=[[.15, 'Mamie Chat', 'PAS près des chiens 😾'], [.5, 'Oncle Rex', 'On arrive à 4 de plus 🐶'], [.85, 'Traiteur', 'Combien de croquettes ?']],
       chars=[dict(CAT, x=540, y=1330, s=1, outfit='dress', shirt='#b18cff', pants='#5b3c8a', glasses=True, pose='type')]),
  dict(t0=5.4, t1=8.6, set='glow', screen=dict(file='Seat_and_Vow.xlsx', sample='Données d\'exemple', title='Plan de table · vérif', top=330, step=.3,
       rows=[['Table 1 · chats', '8 / 8', 'g', 'Pleine ✓'], ['Table 2 · chiens', '12 / 10', 'r', 'Trop pleine'], ['Mamie ↔ Rex', 'même table', 'y', 'À séparer']],
       total=['Placés', 0, 64, '', ' / 64'], stamp='On corrige ✓')),
  dict(t0=8.6, t1=13.0, set='hall', cap='Mariage parfait. Zéro bagarre. 💍', hl=[0, 1, 2, 3], capO=dict(top=1480, fs=68), burst=.4,
       chars=[dict(BRIDE, x=360, y=1330, s=1.05, pose='cheer'), dict(GROOM, x=730, y=1330, s=1.05, pose='cheer')]),
], dict(name='Seat &amp; Vow', sub='Plan de table Excel · FR / EN<br>Données d\'exemple dans cette vidéo', btn='👉 Lien dans la bio', btn2='📤 Identifie ta moitié'),
  'Seat & Vow · Maker FlowTools', '#5a1240', '#ff7aa8', '#ffd27a', memeFs=70)
CAP['P4_chiens_chats_seat_FR'] = "Les chiens ET les chats au même mariage ? 🐱🐶\nVous êtes team chat ou team chien ? 👇\nIdentifie ta moitié 💍\nSeat & Vow (Excel) : vous décidez qui s'assoit où, le classeur compte les places et signale les tables trop pleines et les invités à séparer. (Animation, données d'exemple.)\n👉 Lien dans la bio\n#mariage #plandetable #chat #chien #mariagequébec #organisationmariage"

# 5 · ven. 20 · EN · deux chiens tiennent une boutique de bougies (clin d'œil à « two dogs making coffee »)
R['P5_dogs_candles_artisan_EN'] = reel('en', 'artisan', 'tropical', 305, 'Two dogs running a candle shop 🐶🕯️', [0, 1, 4, 5], [
  dict(t0=0, t1=2.8, set='shop',
       chars=[dict(DOG, x=300, y=1320, s=1, outfit='apron', shirt='#ff9f43', pose='work', rprop='🕯️'),
              dict(DOG2, x=780, y=1320, s=1, outfit='apron', shirt='#5cc8ff', pose='talk', says=[[.4, 2.6, "Let's sell them for $5! 🐶"]], bubFs=40)]),
  dict(t0=2.8, t1=5.0, set='shop',
       chars=[dict(DOG, x=300, y=1320, s=1, outfit='apron', shirt='#ff9f43', pose='think', says=[[.2, 2.1, 'Wait… what do they cost us?']], bubFs=38),
              dict(DOG2, x=780, y=1320, s=1, outfit='apron', shirt='#5cc8ff', pose='idle')]),
  dict(t0=5.0, t1=8.4, set='glow', screen=dict(file='Artisan_Empire_360.xlsx', sample='Sample data', title='Soy candle 9 oz · real cost', top=300, step=.28,
       rows=[['Wax + wick', '$5.80', 'b', 'Materials'], ['Jar + lid', '$3.60', 'b', 'Materials'], ['Scent', '$2.40', 'b', 'Materials'], ['Box + fees', '$2.90', 'y', 'Selling'], ['Your time', '$2.50', 'k', '15 min']],
       total=['Real cost', 0, 17.2, '$', '', 2], stamp='Not $5 😳')),
  dict(t0=8.4, t1=10.6, set='shop', shake=[.1, .6],
       chars=[dict(DOG, x=300, y=1320, s=1, outfit='apron', shirt='#ff9f43', pose='proud'),
              dict(DOG2, x=780, y=1320, s=1, outfit='apron', shirt='#5cc8ff', pose='shock', says=[[.1, 2.1, 'We were LOSING money?! 😱']], bubFs=38)]),
  dict(t0=10.6, t1=13.0, set='shop', cap='New price: $28.70 🕯️', hl=[2], capO=dict(top=1480, fs=84), burst=.2,
       chars=[dict(DOG, x=300, y=1320, s=1, outfit='apron', shirt='#ff9f43', pose='cheer'), dict(DOG2, x=780, y=1320, s=1, outfit='apron', shirt='#5cc8ff', pose='cheer')]),
], dict(name='Artisan Empire 360°', sub='Excel · EN / FR · no macros<br>Sample data in this video', btn='👉 Link in bio', btn2='📤 Send this to a maker friend'),
  'Artisan Empire 360° · Maker FlowTools', '#6a2a10', '#ffb347', '#ffd700')
CAP['P5_dogs_candles_artisan_EN'] = "Two dogs running a candle shop 🐶🕯️\nMakers: be honest, did you ever price at $5? 👇\nSend this to a maker friend before their next market 🎪\nArtisan Empire 360° (Excel): materials, packaging, fees and your time, then a suggested price. (Animated, sample data.)\n👉 Link in bio\n#handmadebusiness #candlemaking #dogsofinstagram #smallbusiness #etsyseller #pricing"

# 6 · sam. 21 · FR · le hamster proprio de 6 logements
R['P6_hamster_landlord_FR'] = reel('fr', 'landlord', 'funk', 306, 'Le hamster proprio de 6 logements 🐹', [1, 2, 4, 5], [
  dict(t0=0, t1=3.4, set='night', laptop=[540], shake=[.8, 2.4],
       notifs=[[.2, 'Logement 1', 'Le loyer est parti !'], [.55, 'Logement 4', 'L\'évier coule 💧'], [.9, 'Logement 6', 'Je peux payer la moitié ?'], [1.25, 'Logement 2', 'C\'est quand le bail finit ?']],
       chars=[dict(HAM, x=540, y=1330, s=1, shirt='#5cc8ff', pose='stress')]),
  dict(t0=3.4, t1=7.0, set='glow', screen=dict(file='Kit_Proprietaire.xlsx', sample='Données d\'exemple', title='Loyers · novembre', top=280, step=.26,
       rows=[['Logement 1', '1 150 $', 'g', 'Payé ✓'], ['Logement 2', '1 250 $', 'g', 'Payé ✓'], ['Logement 4', '600 $ / 1 100 $', 'y', 'Partiel'], ['Logement 6', '0 $ / 980 $', 'r', 'Impayé'], ['Évier · log. 4', 'priorité haute', 'b', 'Planifié']],
       total=['Reçu', 0, 3000, '', ' $'], stamp='Tout est suivi')),
  dict(t0=7.0, t1=7.8, set='black', card='La nuit suivante…', cardC='#2ee6a6', mute=[0, .75]),
  dict(t0=7.8, t1=13.0, set='cozy', cap='Fini, les nuits blanches 😴🐹', hl=[2, 3], capO=dict(top=1480, fs=80),
       chars=[dict(HAM, x=540, y=1330, s=1.05, shirt='#5cc8ff', pose='proud', rprop='☕', poses=[[2.4, 'cheer']])], emojis=[['💤', 700, 640, .6], ['💤', 780, 560, 1.0]]),
], FR_LL, 'Kit Propriétaire · Maker FlowTools', '#0f5a52', '#2ee6a6', '#5cc8ff')
CAP['P6_hamster_landlord_FR'] = "Le hamster proprio de 6 logements 🐹\nToi, c'est combien de textos de locataires par mois ? 👇\nEnvoie ça à un proprio qui ne dort plus 🏠\nKit Propriétaire (Excel) : payé, partiel ou impayé pour chaque logement, et les réparations suivies au même endroit. (Animation, données d'exemple.)\n👉 Lien dans la bio\n#propriétaire #immobilier #plex #québec #hamster #excel"

# 7 · dim. 22 · EN · deux chiens qui préparent leur plan de table
DB = dict(DOG2, outfit='dress', shirt='#ffffff', pants='#f3eefe', hat='veil'); DG = dict(DOG, outfit='suit', shirt='#20263f', tie='#ff7aa8')
R['P7_dog_wedding_seat_EN'] = reel('en', 'seat', 'pop', 307, 'Two dogs planning their wedding seating chart 🐶💍', [0, 1, 4, 5], [
  dict(t0=0, t1=3.0, set='cozy', laptop=[540],
       chars=[dict(DB, x=300, y=1320, s=1, pose='angry', says=[[.3, 2.8, "The cat can't sit near the squirrel 😤"]], bubFs=36),
              dict(DG, x=790, y=1320, s=1, pose='shock')]),
  dict(t0=3.0, t1=5.4, set='cozy', laptop=[540],
       chars=[dict(DB, x=300, y=1320, s=1, pose='laugh'), dict(DG, x=790, y=1320, s=1, pose='stress', says=[[.2, 2.2, 'Your mom invited 40 MORE?! 😳']], bubFs=36)]),
  dict(t0=5.4, t1=8.6, set='glow', screen=dict(file='Seat_and_Vow.xlsx', sample='Sample data', title='Seating · check', top=330, step=.3,
       rows=[['Cat ↔ Squirrel', 'same table', 'r', 'Keep apart'], ['Table 5', '12 / 10', 'y', 'Too full'], ['Meals', '120', 'g', 'Counted ✓']],
       total=['Seated', 0, 120, '', ' / 120'], stamp='All fixed 🐾')),
  dict(t0=8.6, t1=13.0, set='hall', cap='Best wedding ever 🐾💍', hl=[0, 1], capO=dict(top=1480, fs=84), burst=.3,
       chars=[dict(DB, x=360, y=1330, s=1.05, pose='cheer'), dict(DG, x=730, y=1330, s=1.05, pose='cheer')]),
], dict(name='Seat &amp; Vow', sub='Excel seating planner · EN / FR<br>Sample data in this video', btn='👉 Link in bio', btn2='📤 Tag your other half'),
  'Seat & Vow · Maker FlowTools', '#5a1240', '#ff7aa8', '#ffd27a', memeFs=68)
CAP['P7_dog_wedding_seat_EN'] = "Two dogs planning their wedding seating chart 🐶💍\nWho's the \"cat and squirrel\" at YOUR wedding? 👇\nTag your other half 💍\nSeat & Vow (Excel): you decide who sits where, the workbook counts seats and meals and flags guests to keep apart. (Animated, sample data.)\n👉 Link in bio\n#weddingplanning #seatingchart #dogsofinstagram #wedding2027 #engaged #weddingtips"

PLACE = {'P1_cat_landlord_EN': 'd18B', 'P2_raton_tresorier_FR': 'd19B', 'P3_2027_habit_EN': 'd20B', 'P4_chiens_chats_seat_FR': 'd21B',
         'P5_dogs_candles_artisan_EN': 'd22B', 'P6_hamster_landlord_FR': 'd23B', 'P7_dog_wedding_seat_EN': 'd24B'}
if __name__ == '__main__':
    reels = [dict(r, id=k) for k, r in R.items()]
    json.dump({'reels': reels}, open(os.path.join(here, 'pets.json'), 'w'), ensure_ascii=False, indent=1)
    json.dump(CAP, open(os.path.join(here, 'pets_captions.json'), 'w'), ensure_ascii=False, indent=1)
    print(len(reels), 'pets')
