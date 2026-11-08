"""Série « duo » (8 nov. 2026) : variantes du reel gagnant « Elle : 80 invités. Lui : 40. » (1,3K vues).
Même recette (2 personnages, conflit qui monte, gel + silence, l'ordi règle ça, fin heureuse), nouveau sujet à chaque fois.
Moteur trend.html (format couple, paramétrable). Produit duos.json + duos_captions.json.
PLACE = créneau 19 h 30 -> reel ; MOVE = reel déplacé (ancien créneau -> nouveau créneau 19 h 30 qui contenait une image)."""
import json, os, sys
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)
import build_trends as B
FR, EN = B.FR, B.EN
R, CAP = {}, {}
PT = [0, 1.5, 3, 4.2, 5.5, 7.2, 8.6, 10.4, 12, 13.8]
D = dict(format='couple', dur=15, coverAt=4.6, previewTimes=PT)

# 1 · Seat & Vow FR — Les fiancés ép. 2 : les deux mères veulent la table 1
R['D1_meres_seat_FR'] = dict(D, theme='seat', lang='fr', music='lofi', seed=41,
  end=dict(name='Seat &amp; Vow', sub='Les fiancés · épisode 2<br>Plan de table Excel · FR / EN', btn='👉 Lien dans la bio', btn2='📤 Envoie ça à ta belle-mère 😅'),
  t=dict(FR, l1='Sa mère : table 1. Ta mère : table 1. 😤', hl1=[3, 7], herSays='Ma mère à la table 1 !', himSays='La mienne aussi !', stagger=True, bubFs=44, both=True,
    guestsL='Table 1', **{'from': 4, 'to': 14}, over=10, cnt=dict(suf=' / 10'), names=B.G,
    clash=[['1', 'Table 1'], ['!', '14 pour 10']], l2='14 personnes. 10 places. 😳', hl2=[0, 2],
    l3='OK. On regarde les chiffres.', hl3=[3], l4='Les deux mères à la 1. Les tantes à la 2. 💍', hl4=[1, 2],
    seatsL='Table 1', r1=dict(**{'from': 14, 'to': 10}, of=' / 10'), alertL='Alerte', alertBad='⚠️ table pleine', alertOk='tout rentre ✓',
    ep='Les fiancés · ép. 2', file='Seat_and_Vow.xlsx', brand='Seat & Vow · Maker FlowTools'))
CAP['D1_meres_seat_FR'] = "Sa mère : table 1. Ta mère : table 1. 😤 (Les fiancés, épisode 2)\nChez vous, c'est quelle mère qui gagne ? 👇\nEnvoie ça à ta moitié 💍\nSeat & Vow (Excel) : vous décidez qui s'assoit où, le classeur compte les places de chaque table et vous prévient quand une table déborde.\n👉 Lien dans la bio\n#mariage #plandetable #mariagequébec #fiancée #organisationmariage #mariage2027"

# 2 · Landlord Kit EN — locataire vs proprio
R['D2_tenant_landlord_EN'] = dict(D, theme='landlord', lang='en', music='funk', seed=52,
  end=dict(name='Landlord Kit', sub='Excel · EN / FR · no macros', btn='👉 Link in bio', btn2='📤 Send to a landlord friend'),
  t=dict(EN, l1='Tenant: "I paid!" Landlord: "Did you?" 🤨', hl1=[0, 3], herSays='I paid! 💸', himSays='Did you? 🤨', stagger=True, c1='#7ee0a1', h1='🧢', c2='#ffb86b', h2='🎩',
    guestsL='Received', **{'from': 0, 'to': 600}, cnt=dict(pre='$'), tokens=['💵', '💬', '🧾', '💵', '📱'],
    clash=[['$', '$600'], ['?', 'of $1,100']], l2='$600… of $1,100 😳', hl2=[0, 2],
    l3='No arguing. Just check the sheet.', hl3=[3, 4, 5], l4='Partial. $500 due. No drama. 🤝', hl4=[0, 1, 2],
    seatsL='Unit 202', r1=dict(**{'from': 0, 'to': 600}, pre='$', of=' / $1,100'), alertL='Status', alertBad='❓ unclear', alertOk='Partial ✓',
    fin=['🤝', '💵'], ep='Rent day · ep. 1', file='Landlord_Kit.xlsx', brand='Landlord Kit · Maker FlowTools'))
CAP['D2_tenant_landlord_EN'] = "Tenant: \"I paid!\" Landlord: \"Did you?\" 🤨 (Rent day, ep. 1)\nWho's right here? 👇\nSend this to a landlord friend 🏠\nLandlord Kit (Excel): paid, partial or unpaid for every unit and every month, with the balance due.\n👉 Link in bio\n#landlord #rentalproperty #tenant #propertymanagement #realestateinvesting #excel"

# 3 · Kit Trésorier FR — la présidente vs le trésorier
R['D3_presidente_tresorier_FR'] = dict(D, theme='treasurer', lang='fr', music='pop', seed=63,
  end=dict(name='Kit Trésorier', sub='Excel · FR / EN · sans macros', btn='👉 Lien dans la bio', btn2='💬 Écris KIT en commentaire'),
  t=dict(FR, l1='« On a combien ? » Le trésorier : 😅', hl1=[4], herSays='On a combien ? 👀', himSays='Euh… 2\u00a0310\u00a0$ ?', stagger=True, c1='#ffd166', h1='👑', c2='#b39dff', h2='🎓',
    guestsL='Banque', **{'from': 0, 'to': 2310}, cnt=dict(suf=' $'), tokens=['🧾', '💳', '🧁', '🧾', '💵'],
    clash=[['🏦', '2\u00a0310\u00a0$'], ['📒', '2\u00a0185\u00a0$']], l2='Banque : 2\u00a0310\u00a0$. Livres : 2\u00a0185\u00a0$ 😳', hl2=[2, 5],
    l3='Ligne par ligne, on retrouve l\'écart.', hl3=[4, 5], l4='Écart : 0,00\u00a0$. L\'AG peut commencer. 🎉', hl4=[2],
    seatsL='Écart', r1=dict(**{'from': 125, 'to': 0}, dec=2, suf=' $'), alertL='Conciliation', alertBad='⚠️ à vérifier', alertOk='équilibrée ✓',
    fin=['🎉', '✅'], ep='Le comité · ép. 1', file='Kit_Tresorier.xlsx', brand='Kit Trésorier · Maker FlowTools'))
CAP['D3_presidente_tresorier_FR'] = "La présidente : « On a combien ? » Le trésorier : 😅 (Le comité, épisode 1)\nIdentifie le trésorier de ton asso 👇\nKit Trésorier (Excel) : l'onglet Conciliation compare la banque et les livres et t'aide à ramener l'écart à 0,00 $.\n💬 Écris KIT en commentaire et je te réponds avec le lien.\n👉 Ou lien dans la bio\n#trésorier #association #clubétudiant #cégep #comité #budget"

# 4 · Rhythm Habit Tracker EN — moi du 1er janvier vs moi du 15 janvier
R['D4_jan1_habit_EN'] = dict(D, theme='habit', lang='en', music='future', seed=74,
  end=dict(name='Rhythm Habit Tracker 2027', sub='Excel · EN / FR · no macros', btn='👉 Link in bio', btn2='📤 Send to your accountability buddy'),
  t=dict(EN, l1='Me on Jan 1 vs me on Jan 15 🫠', hl1=[2, 3, 6, 7], herSays='365 days! 💪', himSays='Missed one day… 😩', stagger=True, c1='#ffe066', h1='🎉', c2='#8fb3ff', h2='💤',
    guestsL='Streak', **{'from': 14, 'to': 0}, cnt=dict(suf=' days'), tokens=['✓', '✓', '🔥', '✓', '⭐'],
    clash=[['✗', 'Jan 15'], ['🗑️', 'quit?']], l2='One missed day and you quit EVERYTHING? 😩', hl2=[4, 5],
    l3='A missed day stays blank. That\'s it.', hl3=[1, 2, 4], l4='Jan 16: back on track. 💪', hl4=[2, 3, 4],
    seatsL='January', r1=dict(**{'from': 0, 'to': 15}, of=' / 16 ✓'), alertL='Jan 15', alertBad='❌ failed', alertOk='blank · no guilt ✓',
    fin=['💪', '⭐'], ep='New year, same me · ep. 1', file='Rhythm_Habit_Tracker_2027.xlsx', brand='Rhythm Habit Tracker 2027 · Maker FlowTools'))
CAP['D4_jan1_habit_EN'] = "Me on Jan 1 vs me on Jan 15 🫠\nBe honest: how long did your last resolution last? 👇\nSend this to your accountability buddy 🤝\nRhythm Habit Tracker 2027 (Excel): done, minimum version or planned rest. A missed day stays blank, no guilt.\n👉 Link in bio\n#habittracker #2027goals #newyearresolution #productivity #selfimprovement #excel"

# 5 · Artisan Empire FR — la cliente vs l'artisane (savon)
R['D5_cliente_artisan_FR'] = dict(D, theme='artisan', lang='fr', music='tropical', seed=85,
  end=dict(name='Artisan Empire 360°', sub='Excel · FR / EN · sans macros', btn='👉 Lien dans la bio', btn2='📤 Envoie ça à une artisane'),
  t=dict(FR, l1='« 12 $ pour un savon ?! » 😤', hl1=[1, 2, 4], herSays='12 $ ?! 😳', himSays='Ben oui.', stagger=True, c1='#7fe3e0', h1='👒', c2='#ff9ecb', h2='🧶',
    guestsL='Coût réel', **{'from': 0, 'to': 7.2}, cnt=dict(dec=2, suf=' $'), tokens=['🧼', '🌿', '📦', '⏱️', '🏷️'],
    clash=[['🧼', 'matériaux'], ['⏱️', 'ton temps']], l2='Huiles, emballage, frais ET ton temps : 7,20\u00a0$ 😳', hl2=[3, 4, 6],
    l3='Le classeur fait le calcul.', hl3=[1, 4], l4='12\u00a0$, c\'est juste le bon prix. 🧼', hl4=[2, 3, 4],
    seatsL='Coût réel', r1=dict(**{'from': 0, 'to': 7.2}, dec=2, suf=' $'), alertL='Prix suggéré', alertBad='? ', alertOk='12,00 $ ✓',
    fin=['🧼', '✨'], ep='Au marché · ép. 1', file='Artisan_Empire_360.xlsx', brand='Artisan Empire 360° · Maker FlowTools'))
CAP['D5_cliente_artisan_FR'] = "La cliente : « 12 $ pour un savon ?! » L'artisane : 😤 (Au marché, épisode 1)\nToi, tu aurais demandé combien ? 👇\nEnvoie ça à une artisane avant son marché de Noël 🎄\nArtisan Empire 360° (Excel) : matériaux, emballage, frais et ton temps, puis un prix suggéré.\n👉 Lien dans la bio\n#artisan #faitmain #savonartisanal #marchédenoël #etsyquébec #petiteentreprise"

# 6 · Seat & Vow EN — The fiancés ep. 1 : sa mère invite toute l'église
R['D6_church_seat_EN'] = dict(D, theme='seat', lang='en', music='lofi', seed=96,
  end=dict(name='Seat &amp; Vow', sub='The fiancés · episode 1<br>Excel seating planner · EN / FR', btn='👉 Link in bio', btn2='📤 Tag your other half'),
  t=dict(EN, l1='Her mom: "Invite the whole church." Him: 😳', hl1=[0, 1, 4, 5], herSays='The whole church! ⛪', himSays='The venue fits 150.', stagger=True, bubFs=44, both=True,
    guestsL='Guests', **{'from': 90, 'to': 182}, over=150, names=B.G,
    clash=[['⛪', '182 guests'], ['🪑', '150 seats']], l2='182 guests. 150 seats. 😳', hl2=[0, 2],
    l3='Okay. Let\'s count properly.', hl3=[1, 3], l4='150 seats. Everyone fits. Even the choir. 💍', hl4=[0, 1, 5],
    seatsL='Seats', r1=dict(**{'from': 182, 'to': 150}, of=' / 150'), alertL='Alert', alertBad='⚠️ 3 tables full', alertOk='all good ✓',
    ep='The fiancés · ep. 1', file='Seat_and_Vow.xlsx', brand='Seat & Vow · Maker FlowTools'))
CAP['D6_church_seat_EN'] = "Her mom: \"Invite the whole church.\" Him: 😳 (The fiancés, ep. 1)\nTeam big wedding or team small wedding? 👇\nTag your other half 💍\nSeat & Vow (Excel): you decide who sits where, the workbook counts the seats at every table and warns you when one is over.\n👉 Link in bio\n#weddingplanning #seatingchart #wedding #bride2027 #engaged #weddingtips"

PLACE = {'d11B': 'D1_meres_seat_FR', 'd12B': 'D2_tenant_landlord_EN', 'd13B': 'D3_presidente_tresorier_FR',
         'd14B': 'D4_jan1_habit_EN', 'd15B': 'D5_cliente_artisan_FR', 'd16B': 'D6_church_seat_EN'}
MOVE = {'d11B': 'd21B', 'd12B': 'd18B', 'd13B': 'd23B', 'd14B': 'd20B', 'd15B': 'd25B', 'd16B': 'd22B'}  # même langue (FR = jours impairs à 19 h 30)
if __name__ == '__main__':
    reels = []
    for rid, r in R.items():
        r = dict(r); r.update(id=rid, engine='trend.html'); reels.append(r)
    json.dump({'reels': reels}, open(os.path.join(here, 'duos.json'), 'w'), ensure_ascii=False, indent=1)
    json.dump(CAP, open(os.path.join(here, 'duos_captions.json'), 'w'), ensure_ascii=False, indent=1)
    print(len(reels), 'duos')
