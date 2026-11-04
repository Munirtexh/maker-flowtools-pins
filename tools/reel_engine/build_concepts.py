"""6 concepts issus de la recherche virale du 4 nov. 2026 (doc « Recherche virale »), demandés par Yaacoub
pour la semaine du 4 au 8 nov. Moteur trend.html (formats splitReal, guess, yearGrid, couple, sign + sortChaos).
Produit concepts.json + concepts_captions.json ; PLACE = créneau du manifest -> reel."""
import json, os, sys
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)
import build_trends as B
FR, EN, it = B.FR, B.EN, B.it
R, CAP = {}, {}
PT = [0, 1.5, 3, 4.5, 6, 7.5, 9, 10.5, 12, 13.8]
# 1 · POV 1er du mois (témoin) — Kit Propriétaire EN
R['K1_pov_landlord_EN'] = dict(format='sortChaos', theme='landlord', lang='en', dur=15, music='pop', seed=57, coverAt=6.8,
  end=dict(name='Landlord Kit', sub='Excel · EN / FR · no macros', btn='👉 Link in bio', btn2='📤 Send to a landlord friend'),
  t=dict(EN, l1="POV: it's the 1st and 6 tenants text you at once", l2a="and you can't tell who paid 😬", hl2a=[3, 5], l2b='so the spreadsheet sorts it ✨', hl2b=[2, 4],
    items=[it('Unit 101', '$1,250', 'Paid ✓', 'g'), it('Unit 102', '$600 of $1,100', 'Partial', 'y'), it('Unit 201', '$1,325', 'Paid ✓', 'g'),
           it('Unit 202', '$0 of $980', 'Unpaid', 'r'), it('Unit 301', '$1,150', 'Paid ✓', 'g'), it('Unit 302', '$1,050', 'Paid ✓', 'g')],
    decoys=['💬', '📱', '💬', '🧾', '❓', '📱', '💬', '📌'],
    total=dict(l='Received this month', v=5375, f='cur0', c='g'), wtitle='Rent · November', warn='📱 6 new messages', stamp='All tracked ✓', emoji='😵‍💫',
    beats=[dict(text='Paid · partial · unpaid at a glance', c='y', x=40, y=640, rot=-4), dict(text='Repairs tracked too 🔧', c='b', x=440, y=1560, rot=5),
           dict(text='Lease-end reminders 🔔', c='g', x=120, y=1110, rot=-4)],
    file='Landlord_Kit.xlsx', brand='Landlord Kit · Maker FlowTools'))
CAP['K1_pov_landlord_EN'] = "POV: it's the 1st and 6 tenants text you at once 😵‍💫\nHow do you track who paid? Be honest 👇\nSend this to a landlord friend 🏠\nLandlord Kit (Excel): paid, partial or unpaid for every unit, plus repairs and lease-end reminders.\n👉 Link in bio\n#landlord #rentalproperty #realestateinvesting #propertymanagement #excel #canada"
# 2 · Attente vs réalité — Kit Trésorier FR
R['K2_attente_tresorier_FR'] = dict(format='splitReal', theme='treasurer', lang='fr', dur=15, music='funk', seed=62, coverAt=3.6,
  end=dict(name='Kit Trésorier', sub='Excel · FR / EN · sans macros', btn='💬 Écris KIT en commentaire', btn2='👉 ou lien dans la bio'),
  t=dict(FR, l1="Devenir trésorier de l'asso 😅", hl1=[2], left='Ce que je pensais', right='La réalité',
    calmTitle='Petit budget 🙂', calm=[('Cotisations', '400 $'), ('Pizza AG', '120 $'), ('Reste', '280 $')],
    msgs=["T'as reçu mon virement ?", 'Il manque 245 $ 😬', "C'est qui qui a pas payé ?", 'Le reçu de la pizza ??', "J'ai payé en cash !", 'Le rapport pour l\'AG ?', 'On a combien ???'],
    gapChip='⚠️ Écart : 245 $', v2='La réalité, version 2.0 :', hlv2=[3],
    items=[it('Alex M.', '40 $', 'Payé ✓', 'g'), it('Jade L.', '20 $ sur 40 $', 'Partiel', 'y'), it('Sam K.', '0 $ sur 40 $', 'Impayé', 'r'),
           it('Noah P.', '40 $', 'Payé ✓', 'g'), it('Léa R.', '40 $', 'Payé ✓', 'g'), it('Omar B.', '40 $', 'Payé ✓', 'g')],
    ecartL='Écart banque ↔ livres', ecart=245, copyChip='📋 Rappel prêt à copier', eq='Attente = réalité', hleq=[0, 2], stamp='Tout balance ✓',
    wtitle="Cotisations · session d'automne", file='Kit_Tresorier.xlsx', brand='Kit Trésorier · Maker FlowTools'))
CAP['K2_attente_tresorier_FR'] = "Devenir trésorier de l'asso : ce que je pensais vs la réalité 😅\nIdentifie le trésorier de ton comité 👇\nKit Trésorier (Excel) : payé, partiel ou impayé se met à jour seul, la conciliation ramène l'écart à 0,00 $ et un rappel est prêt à copier.\n💬 Écris KIT en commentaire et je te réponds avec le lien.\n👉 Ou lien dans la bio\n#trésorier #association #clubétudiant #cégep #vieétudiante #budget"
# 3 · 365 cases — Rhythm Habit Tracker EN (boucle, pas d'écran de fin)
R['K3_365_habit_EN'] = dict(format='yearGrid', theme='habit', lang='en', dur=15, loop=True, music='future', seed=91, coverAt=9.6,
  t=dict(EN, l1='Watch your 2027 fill up.', hl1=[3, 4], months=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    legend=['Done', 'Minimum', 'Rest'], noGuilt='Missed days stay blank. No guilt.', stats=[('done', 287), ('minimum', 41), ('rest', 22)],
    banner='Rhythm Habit Tracker 2027 · link in bio', brand='Rhythm Habit Tracker 2027 · Maker FlowTools · sample data'))
CAP['K3_365_habit_EN'] = "Watch your 2027 fill up 📅\nWhat's the ONE habit you're starting in 2027? 👇\nSend this to your accountability buddy 🤝\nRhythm Habit Tracker 2027 (Excel): done, minimum version or planned rest. A missed day stays blank, no guilt.\n👉 Link in bio\n#habittracker #2027goals #newyearresolution #productivity #selfimprovement #excel"
# 4 · Les fiancés, épisode 1 — Seat & Vow FR
R['K4_fiances_seat_FR'] = dict(format='couple', theme='seat', lang='fr', dur=15, music='lofi', seed=33, coverAt=4.6,
  end=dict(name='Seat &amp; Vow', sub='Les fiancés · épisode 1<br>Plan de table Excel · FR / EN', btn='👉 Lien dans la bio', btn2='📤 Identifie ta moitié'),
  t=dict(FR, l1='Elle : 80 invités. Lui : 40. 😤', hl1=[1, 4], herSays='80 !', himSays='40.', guestsL='Invités', **{'from': 40, 'to': 80},
    names=B.G, clash=['Tante Lise', 'Oncle Marc'], l2='Et ta tante ne doit PAS voir mon oncle', hl2=[2, 7],
    l3='Bon. On fait ça proprement.', hl3=[3], l4='Toujours fâchés. Mais le plan est fait. 💍', hl4=[5, 6],
    seatsL='Places', alertL='Lise ↔ Marc', alertBad='⚠️ même table', alertOk='séparés ✓', ep='Les fiancés · ép. 1',
    file='Seat_and_Vow.xlsx', brand='Seat & Vow · Maker FlowTools'))
CAP['K4_fiances_seat_FR'] = "Elle : 80 invités. Lui : 40. 😤 (Les fiancés, épisode 1)\nVous êtes plutôt team 80 ou team 40 ? 👇\nIdentifie ta moitié 💍\nSeat & Vow (Excel) : vous décidez qui s'assoit où, le classeur compte les places et vous prévient quand deux invités doivent être séparés.\n👉 Lien dans la bio\n#mariage #plandetable #mariagequébec #fiancée #organisationmariage #mariage2027"
# 5 · Devinette du prix — Artisan Empire 360° EN
R['K5_guess_artisan_EN'] = dict(format='guess', theme='artisan', lang='en', dur=15, music='tropical', seed=77, coverAt=10.6,
  end=dict(name='Artisan Empire 360°', sub='Excel · EN / FR · no macros', btn='👉 Link in bio', btn2='📤 Send to a maker friend'),
  t=dict(EN, l1='This candle: what would you charge?', hl1=[4, 5, 6], sub='Guess in the comments 👇', label='SOY CANDLE', label2='lavender · 8 oz',
    costs=[('Soy wax', 6.40), ('Wick', .45), ('Jar', 3.90), ('Fragrance', 2.10), ('Packaging', 1.60), ('Etsy fees', 1.30), ('Your time (20 min)', 2.10)],
    totalL='Real cost', margin='For a 40% margin…', hlm=[2], price='$29.75', ask='What did you guess? 👇', hla=[3],
    file='Artisan_Empire_360.xlsx', brand='Artisan Empire 360° · Maker FlowTools'))
CAP['K5_guess_artisan_EN'] = "This candle: what would you charge? 🕯️ Guess before the end 👇\nReal cost $17.85 once you count wax, jar, fees AND your time.\nSend this to a maker friend before their next craft fair 🎪\nArtisan Empire 360° (Excel): materials, packaging, fees and your time, then a suggested price.\n👉 Link in bio\n#handmadebusiness #craftfair #etsyseller #candlemaking #smallbusiness #pricing"
# 6 · Ceci est ton signe — Seat & Vow FR (7 s, boucle)
R['K6_signe_seat_FR'] = dict(format='sign', theme='seat', lang='fr', dur=7, loop=True, music='pop', seed=29, coverAt=4.2, previewTimes=[0, 1.5, 3, 4.2, 5.5, 6.9],
  t=dict(FR, l1='Ceci est ton signe de faire ton plan de table AVANT les fêtes', hl1=[7, 8, 9], guests=B.G, seated='Placés',
    banner='Seat & Vow · lien dans la bio', brand=''))
CAP['K6_signe_seat_FR'] = "Ceci est ton signe de faire ton plan de table AVANT les fêtes 🎄💍\nEnvoie ça à la personne qui se marie en 2027 👇\nSeat & Vow (Excel) : tu places tes invités, le classeur compte les places et signale les invités à séparer.\n👉 Lien dans la bio\n#mariage #plandetable #fiançailles #mariagequébec #mariage2027 #organisationmariage"
# créneaux : concepts d'ici dimanche ; les reels prévus cette semaine passent la semaine prochaine
PLACE = {'d06B': 'K1_pov_landlord_EN', 'd07B': 'K2_attente_tresorier_FR', 'd08B': 'K3_365_habit_EN', 'd09B': 'K4_fiances_seat_FR',
         'd10B': 'K5_guess_artisan_EN', 'd10A': 'K6_signe_seat_FR'}
MOVE = {'d07B': 'd15B', 'd08B': 'd14B', 'd09B': 'd17B', 'd10B': 'd16B', 'd10A': 'd19B'}  # ancien créneau -> nouveau (19 h 30, langue opposée)
if __name__ == '__main__':
    reels = []
    for rid, r in R.items():
        r = dict(r); r.update(id=rid, engine='trend.html'); r.setdefault('previewTimes', PT); reels.append(r)
    json.dump({'reels': reels}, open(os.path.join(here, 'concepts.json'), 'w'), ensure_ascii=False, indent=1)
    json.dump(CAP, open(os.path.join(here, 'concepts_captions.json'), 'w'), ensure_ascii=False, indent=1)
    print(len(reels), 'concepts')
