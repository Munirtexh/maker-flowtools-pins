"""Test « un style d'animation par jour » (20 nov. 2026, consigne de Yaacoub) : chaque soir à 19 h 30, un style
complètement différent (pâte à modeler 3D, low poly années 90, pixel 16-bit, ...), les mêmes deux héros récurrents
(Mochi la chatte et Biscuit le chien), une vraie musique différente chaque jour (music2.py). On compare les vues,
puis on ne garde que le gagnant. Moteur : story.html + couche 3D world3d.js (cfg.world / cfg.look).
Produit styles.json + styles_captions.json ; placement : apply_styles.py."""
import json, os
here = os.path.dirname(os.path.abspath(__file__))
R, CAP, PLACE = {}, {}, {}
PT = [0.2, 1.8, 3.0, 4.8, 6.0, 7.6, 9.6, 11.0, 12.4, 14]

# ---- Jour 1 · sam. 21 nov. · FR · 3D fluide façon film d'animation (la version pâte à modeler saccadée a été refusée par Yaacoub) ----
R['X1_film3d_mariage_FR'] = dict(engine='story.html', world='wedding', look='film', theme='seat', lang='fr', dur=15, music='gm:pizz', seed=401,
  coverAt=4.4, endAt=13.0, cinema=True, previewTimes=PT, accent='#5a1240', a1='#ff7aa8', a2='#ffd27a', brand='Seat & Vow · Maker FlowTools',
  meme='Quand ta belle-mère « ajoute juste quelques invités » 🙃', mhl=[3, 4], memeFs=64,
  chips=[[1.6, 3.15, 'Invités : 143 😳', 620, 470, '#ffc23d'], [3.7, 6.55, 'Table 4 : 15 / 10', 290, 1560, '#ff5d73']],
  bubbles=[[9.25, 11.2, 'On déplace ces 6-là 👉', 180, 760, 46]],
  scenes=[dict(t0=0, t1=3.2, set='none'),
          dict(t0=3.2, t1=6.6, set='none', shake=[1.3, 2.3], mute=[2.35, 3.4]),
          dict(t0=6.6, t1=9.0, set='glow', screen=dict(file='Seat_and_Vow.xlsx', sample='Données d\'exemple', title='Plan de table · vérif', top=330, step=.3,
               rows=[['Table 4', '15 / 10', 'r', 'Trop pleine'], ['Tonton ↔ Tata', 'même table', 'y', 'À séparer'], ['Repas', '143', 'g', 'Comptés ✓']],
               total=['Places libres', 0, 7, '', ' ailleurs'], stamp='On corrige ✓')),
          dict(t0=9.0, t1=11.0, set='none'),
          dict(t0=11.0, t1=13.0, set='none', cap='Plan de table : réglé ✅', hl=[0, 1, 2], capO=dict(top=1480, fs=84), burst=.6)],
  end=dict(name='Seat &amp; Vow', sub='Plan de table Excel · FR / EN<br>Données d\'exemple dans cette vidéo', btn='👉 Lien dans la bio', btn2='📤 Envoie ça aux futurs mariés'))
CAP['X1_film3d_mariage_FR'] = ("Quand ta belle-mère « ajoute juste quelques invités » 🙃\n"
  "Elle en a ajouté combien chez vous ? 👇\nEnvoie ça aux futurs mariés 💍\n"
  "Seat & Vow (Excel) : vous décidez qui s'assoit où ; le classeur compte les places et les repas et signale les tables trop pleines. (Animation, données d'exemple.)\n"
  "👉 Lien dans la bio\n#mariage #plandetable #bellemère #animation3d #mariagequébec #organisationmariage")
PLACE['X1_film3d_mariage_FR'] = 'd23B'

# ---- Jour 2 · dim. 22 nov. · EN · low poly années 90 (pages « blocky 3D » à plusieurs millions de vues) ----
R['X2_lowpoly_rentday_EN'] = dict(engine='story.html', world='rentday', look='lowpoly', theme='landlord', lang='en', dur=15, music='gm:synthwave', seed=402,
  coverAt=2.6, endAt=13.0, cinema=True, previewTimes=PT, accent='#0f5a52', a1='#2ee6a6', a2='#5cc8ff', brand='Landlord Kit · Maker FlowTools',
  meme='POV: you own 6 units and it\'s the 1st of the month 😵‍💫', mhl=[3, 4, 9], memeFs=62,
  chips=[[3.4, 6.5, 'Who paid?! 🤯', 330, 1540, '#ffc23d']],
  bubbles=[[2.3, 4.2, "Half now, half Friday? 🙏", 420, 640, 40]],
  scenes=[dict(t0=0, t1=3.2, set='none'),
          dict(t0=3.2, t1=6.6, set='none', shake=[1.6, 2.6], mute=[2.6, 3.4]),
          dict(t0=6.6, t1=8.6, set='glow', screen=dict(file='Landlord_Kit.xlsx', sample='Sample data', title='Rent · December', top=330, step=.26,
               rows=[['Units 1, 2, 4', '$3,350', 'g', 'Paid ✓'], ['Unit 3 · Biscuit', '$550 of $1,100', 'y', 'Partial'], ['Unit 6', '$700 of $1,050', 'y', 'Partial'], ['Unit 5', '$0 of $980', 'r', 'Unpaid']],
               total=['Received', 0, 4600, '$'], stamp='Tracked ✓')),
          dict(t0=8.6, t1=10.4, set='none'),
          dict(t0=10.4, t1=13.0, set='none', cap='Every unit. One sheet. 😌', hl=[0, 1, 3], capO=dict(top=1500, fs=80))],
  end=dict(name='Landlord Kit', sub='Excel · EN / FR · no macros<br>Sample data in this video', btn='👉 Link in bio', btn2='📤 Send this to a landlord friend'))
CAP['X2_lowpoly_rentday_EN'] = ("POV: you own 6 units and it's the 1st of the month 😵‍💫\n"
  "Landlords: how many units do you manage? 👇\nSend this to a landlord friend 🏠\n"
  "Landlord Kit (Excel): paid, partial or unpaid for every unit and every month, in one sheet. (Animated, sample data.)\n"
  "👉 Link in bio\n#landlord #rentalproperty #propertymanagement #lowpoly #realestateinvesting #excel")
PLACE['X2_lowpoly_rentday_EN'] = 'd24B'

# ---- Jour 3 · lun. 23 nov. · FR · pixel 16-bit (rétro jeu vidéo) ----
R['X3_pixel_tresorier_FR'] = dict(engine='story.html', world='meeting', look='pixel', theme='treasurer', lang='fr', dur=15, music='gm:chip', seed=403,
  coverAt=2.2, endAt=13.0, cinema=False, previewTimes=PT, accent='#3a2380', a1='#ffc23d', a2='#b18cff', brand='Kit Trésorier · Maker FlowTools',
  meme='« Qui veut être trésorier ? » Toute la classe : 👀', mhl=[4, 5], memeFs=66,
  chips=[[2.0, 3.25, 'TRÉSORIER 👑', 330, 1540, '#ffc23d'], [3.5, 6.55, '47 reçus 🧾', 360, 1540, '#ff5d73']],
  bubbles=[[1.5, 3.2, 'Moi ?! 😳', 430, 760, 54]],
  scenes=[dict(t0=0, t1=3.3, set='none'),
          dict(t0=3.3, t1=6.6, set='none', shake=[1.4, 2.3], mute=[2.3, 3.3]),
          dict(t0=6.6, t1=9.0, set='glow', screen=dict(file='Kit_Tresorier.xlsx', sample='Données d\'exemple', title='Cotisations · automne', top=330, step=.28,
               rows=[['22 membres', '40 $', 'g', 'Payé ✓'], ['3 membres', '20 $ sur 40 $', 'y', 'Partiel'], ['2 membres', '0 $ sur 40 $', 'r', 'Impayé']],
               total=['Reçu', 0, 940, '', ' $'], stamp='À jour ✓')),
          dict(t0=9.0, t1=10.8, set='none'),
          dict(t0=10.8, t1=13.0, set='none', cap='Meilleur trésorier de l\'histoire 🏅', hl=[0, 1], capO=dict(top=1480, fs=76))],
  end=dict(name='Kit Trésorier', sub='Excel · FR / EN · sans macros<br>Données d\'exemple dans cette vidéo', btn='👉 Lien dans la bio', btn2='💬 Écris KIT en commentaire'))
CAP['X3_pixel_tresorier_FR'] = ("« Qui veut être trésorier ? » Toute la classe : 👀\n"
  "Identifie celui qu'on a nommé trésorier sans lui demander 👇\n"
  "Kit Trésorier (Excel) : qui a payé, qui a payé à moitié, qui n'a rien payé, et le total reçu. (Animation, données d'exemple.)\n"
  "💬 Écris KIT en commentaire et je te réponds avec le lien.\n👉 Ou lien dans la bio\n#trésorier #association #clubétudiant #pixelart #cégep #budget")
PLACE['X3_pixel_tresorier_FR'] = 'd25B'

# ---- Jour 4 · mar. 24 nov. · EN · bonhommes allumettes sur fond noir (format comparaison, pages à 100 M+ de vues) ----
R['X4_stickman_habit_EN'] = dict(engine='story.html', world='versus', look='stick', theme='habit', lang='en', dur=15, music='gm:keys', seed=404,
  coverAt=4.4, endAt=13.0, cinema=False, previewTimes=PT, accent='#0b4a33', a1='#4dffb5', a2='#ffd166', brand='Rhythm Habit Tracker 2027 · Maker FlowTools',
  meme='10 new habits on Jan 1 vs. 1 tiny habit a day', mhl=[0, 1, 7, 8], memeFs=64,
  chips=[[0.4, 3.5, 'DAY 1', 470, 380, '#ffffff'], [3.5, 6.4, 'DAY 4', 470, 380, '#ff5d73'], [9.0, 12.9, 'DAY 31', 450, 380, '#2ee6a6']],
  bubbles=[[1.0, 3.3, 'I\'ll do it ALL 💪', 70, 1240, 40], [1.5, 3.3, 'Just 10 min 📖', 640, 1240, 40]],
  scenes=[dict(t0=0, t1=3.5, set='none'),
          dict(t0=3.5, t1=6.4, set='none', shake=[.05, .4]),
          dict(t0=6.4, t1=8.6, set='glow', screen=dict(file='Rhythm_Habit_Tracker_2027.xlsx', sample='Sample data', title='January 2027 · read', top=330, step=.28,
               rows=[['Jan 14', 'Done', 'g', '✓'], ['Jan 15', 'missed', '#8f9bc0', 'blank · no guilt'], ['Jan 16', 'Minimum version', 'y', '5 min']],
               total=['January', 0, 27, '', ' / 31 days'], stamp='Keep going')),
          dict(t0=8.6, t1=10.8, set='none'),
          dict(t0=10.8, t1=13.0, set='none', cap='Small beats perfect. 🏁', hl=[0, 2], capO=dict(top=1500, fs=84))],
  end=dict(name='Rhythm Habit Tracker 2027', sub='Excel · EN / FR · no macros<br>Sample data in this video', btn='👉 Link in bio', btn2='📤 Send this to your 2027 buddy'))
CAP['X4_stickman_habit_EN'] = ("10 new habits on Jan 1 vs. 1 tiny habit a day 🏁\n"
  "Be honest: which one were you in January? 👇\nSend this to your 2027 buddy 🤝\n"
  "Rhythm Habit Tracker 2027 (Excel): done, minimum version or planned rest. A missed day stays blank, no guilt. (Animated, sample data.)\n"
  "👉 Link in bio\n#habittracker #newyearsresolutions #2027goals #stickman #productivity #excel")
PLACE['X4_stickman_habit_EN'] = 'd26B'

# ---- Jour 5 · mer. 25 nov. · FR · papier découpé (couches de papier, ombres douces, mouvement fluide) ----
R['X5_papier_savons_FR'] = dict(engine='story.html', world='market', look='paper', theme='artisan', lang='fr', dur=15, music='gm:marimba', seed=405,
  coverAt=2.2, endAt=13.0, cinema=False, previewTimes=PT, accent='#6a2a10', a1='#ffb347', a2='#ffd700', brand='Artisan Empire 360° · Maker FlowTools',
  meme='Elle vend ses savons 5 $. Tout part en 3 secondes 😍', mhl=[4, 5, 8], memeFs=64,
  chips=[[2.6, 3.3, 'TOUT VENDU 🎉', 330, 1540, '#2ee6a6'], [4.4, 6.55, 'Profit : −2,40 $ par savon 😳', 120, 1540, '#ff5d73']],
  bubbles=[[9.6, 11.0, '👈 Nouveau prix', 520, 640, 46]],
  scenes=[dict(t0=0, t1=3.3, set='none'),
          dict(t0=3.3, t1=6.6, set='none', shake=[1.2, 2.2], mute=[2.3, 3.3]),
          dict(t0=6.6, t1=9.0, set='glow', screen=dict(file='Artisan_Empire_360.xlsx', sample='Données d\'exemple', title='Savon artisanal · vrai coût', top=300, step=.26,
               rows=[['Matières', '3,10 $', 'b', 'Huiles, soude'], ['Emballage', '1,20 $', 'b', 'Boîte'], ['Frais du marché', '0,90 $', 'y', 'Par savon'], ['Ton temps', '2,20 $', 'k', '10 min']],
               total=['Vrai coût', 0, 7.4, '', ' $', 2], stamp='Prix suggéré : 12 $')),
          dict(t0=9.0, t1=11.0, set='none'),
          dict(t0=11.0, t1=13.0, set='none', cap='Bon prix. Vraie paie. 🧼', hl=[0, 1, 2, 3], capO=dict(top=1500, fs=84))],
  end=dict(name='Artisan Empire 360°', sub='Excel · FR / EN · sans macros<br>Données d\'exemple dans cette vidéo', btn='👉 Lien dans la bio', btn2='📤 Envoie ça à une artisane'))
CAP['X5_papier_savons_FR'] = ("Elle vend ses savons 5 $. Tout part en 3 secondes 😍… et elle perd de l'argent 😳\n"
  "Artisans : vous comptez votre temps dans votre prix ? 👇\nEnvoie ça à une artisane avant son prochain marché de Noël 🎄\n"
  "Artisan Empire 360° (Excel) : matières, emballage, frais et ton temps, puis un prix suggéré. (Animation, données d'exemple.)\n"
  "👉 Lien dans la bio\n#artisan #faitmain #marchédenoël #savonartisanal #petitecommerce #prix")
PLACE['X5_papier_savons_FR'] = 'd27B'

# ---- Jour 6 · jeu. 26 nov. · EN · plan technique « blueprint » (traits clairs sur fond bleu) ----
R['X6_blueprint_seating_EN'] = dict(engine='story.html', world='floorplan', look='blueprint', theme='seat', lang='en', dur=15, music='gm:swing', seed=406,
  coverAt=4.4, endAt=13.0, cinema=False, previewTimes=PT, accent='#0b3566', a1='#5cc8ff', a2='#2ee6a6', brand='Seat & Vow · Maker FlowTools',
  meme='Planning your wedding seating like an architect 📐', mhl=[4, 5, 7], memeFs=64,
  chips=[[3.6, 5.0, 'KEEP APART ⚠️', 330, 1540, '#ff5d73'], [5.0, 6.55, 'T5 · 12 / 10', 380, 1540, '#ffc23d']],
  bubbles=[[9.3, 11.0, 'We move these 3 ✏️', 560, 1420, 42]],
  scenes=[dict(t0=0, t1=3.4, set='none'),
          dict(t0=3.4, t1=6.6, set='none', mute=[2.2, 3.2]),
          dict(t0=6.6, t1=9.0, set='glow', screen=dict(file='Seat_and_Vow.xlsx', sample='Sample data', title='Seating · check', top=330, step=.28,
               rows=[['Uncle Rick ↔ Aunt Pam', 'same table', 'r', 'Keep apart'], ['Table 5', '12 / 10', 'y', 'Too full'], ['Meals', '50', 'g', 'Counted ✓']],
               total=['Seated', 0, 50, '', ' / 50'], stamp='Plan it ✓')),
          dict(t0=9.0, t1=11.0, set='none'),
          dict(t0=11.0, t1=13.0, set='none', cap='Engineered. Not stressed. 📐', hl=[0, 2], capO=dict(top=1500, fs=80))],
  end=dict(name='Seat &amp; Vow', sub='Excel seating planner · EN / FR<br>Sample data in this video', btn='👉 Link in bio', btn2='📤 Tag your other half'))
CAP['X6_blueprint_seating_EN'] = ("Planning your wedding seating like an architect 📐\n"
  "Who's the uncle you'd seat farthest away? 👇\nTag your other half 💍\n"
  "Seat & Vow (Excel): you decide who sits where; the workbook counts seats and meals and flags full tables and guests to keep apart. (Animated, sample data.)\n"
  "👉 Link in bio\n#weddingplanning #seatingchart #wedding2027 #blueprint #engaged #weddingtips")
PLACE['X6_blueprint_seating_EN'] = 'd28B'

# ---- Jour 7 · ven. 27 nov. · FR · silhouettes à l'encre devant un ciel qui passe du coucher de soleil à la nuit puis à l'aube ----
R['X7_silhouette_proprio_FR'] = dict(engine='story.html', world='porch', look='silhouette', theme='landlord', lang='fr', dur=15, music='gm:uke', seed=407,
  coverAt=4.0, endAt=13.0, cinema=True, previewTimes=PT, accent='#0f5a52', a1='#2ee6a6', a2='#5cc8ff', brand='Kit Propriétaire · Maker FlowTools',
  meme='Proprio, 23 h 58. Le locataire : « petite question… » 📱', mhl=[0, 1, 2], memeFs=62,
  scenes=[dict(t0=0, t1=3.3, set='none'),
          dict(t0=3.3, t1=6.6, set='none', notifs=[[.1, 'Logement 2', 'Le chauffe-eau fait un drôle de bruit 😬'], [.5, 'Logement 5', 'Je peux payer le 15 ?'], [.9, 'Logement 3', 'Le robinet coule encore 💧']], shake=[1.4, 2.2], mute=[2.4, 3.3]),
          dict(t0=6.6, t1=9.0, set='glow', screen=dict(file='Kit_Proprietaire.xlsx', sample='Données d\'exemple', title='Suivi · novembre', top=300, step=.26,
               rows=[['Chauffe-eau · log. 2', 'priorité haute', 'r', 'Planifié'], ['Robinet · log. 3', 'normal', 'y', 'À faire'], ['Loyer · log. 5', '0 $ / 950 $', 'y', 'En retard'], ['Loyers · log. 1-4, 6', '5 900 $', 'g', 'Payés ✓']],
               total=['Reçu', 0, 5900, '', ' $'], stamp='Tout est noté ✓')),
          dict(t0=9.0, t1=10.8, set='none'),
          dict(t0=10.8, t1=13.0, set='none', cap='Une feuille. Des nuits tranquilles. 🌙', hl=[1, 4], capO=dict(top=1500, fs=76))],
  end=dict(name='Kit Propriétaire', sub='Excel · FR / EN · sans macros<br>Données d\'exemple dans cette vidéo', btn='👉 Lien dans la bio', btn2='📤 Envoie ça à un proprio'))
CAP['X7_silhouette_proprio_FR'] = ("Proprio, 23 h 58. Le locataire : « petite question… » 📱\n"
  "Proprios : c'est quoi le texto le plus tard que vous avez reçu ? 👇\nEnvoie ça à un proprio qui ne dort plus 🏠\n"
  "Kit Propriétaire (Excel) : les loyers (payé, partiel, en retard) et les réparations au même endroit. (Animation, données d'exemple.)\n"
  "👉 Lien dans la bio\n#propriétaire #immobilier #plex #québec #locataire #excel")
PLACE['X7_silhouette_proprio_FR'] = 'd29B'

if __name__ == '__main__':
    json.dump({'reels': [dict(r, id=k) for k, r in R.items()]}, open(os.path.join(here, 'styles.json'), 'w'), ensure_ascii=False, indent=1)
    json.dump(CAP, open(os.path.join(here, 'styles_captions.json'), 'w'), ensure_ascii=False, indent=1)
    print(len(R), 'styles')
