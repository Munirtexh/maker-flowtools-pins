"""Série « duo », lot 2 (8 nov. 2026) : remplace les vieilles vidéos fond blanc de 12 h 30 (délégation de Yaacoub).
Mêmes produits et même langue que la vidéo remplacée, sujet neuf. Produit duos2.json + duos2_captions.json. PLACE = créneau -> reel."""
import json, os, sys
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)
import build_trends as B
from build_duos import D
FR, EN = B.FR, B.EN
R, CAP = {}, {}
LL = dict(end=dict(name='Landlord Kit', sub='Excel · EN / FR · no macros', btn='👉 Link in bio', btn2='📤 Send to a landlord friend'))
LF = dict(end=dict(name='Kit Propriétaire', sub='Excel · FR / EN · sans macros', btn='👉 Lien dans la bio', btn2='📤 Envoie ça à un proprio'))

R['E1_partner_landlord_EN'] = dict(D, theme='landlord', lang='en', music='pop', seed=111, **LL,
  t=dict(EN, l1='"Both buildings make money, right?" 😎', hl1=[3, 4], herSays='Both make money? 🤑', himSays='Obviously. 😎', stagger=True, c1='#ffb86b', h1='🧢', c2='#7ee0a1', h2='🎩',
    guestsL='Expenses', **{'from': 0, 'to': 4340}, over=4200, cnt=dict(pre='$'), tokens=['🧾', '🔧', '💡', '🧾', '🏚️'],
    clash=[['B', 'Building B'], ['−', '−$140/mo']], l2='Building B costs more than it brings 😳', hl2=[0, 1, 2],
    l3='At least now we know.', hl3=[3], l4='Fix Building B before it costs more. 🏢', hl4=[0, 1, 2],
    seatsL='Building A', r1=dict(**{'from': 0, 'to': 1120}, pre='+$', of='/mo'), alertL='Building B', alertBad='❓ no idea', alertOk='−$140 spotted ✓',
    fin=['🏢', '📊'], ep='Rent day · ep. 2', file='Landlord_Kit.xlsx', brand='Landlord Kit · Maker FlowTools'))
CAP['E1_partner_landlord_EN'] = "Partner: \"Both buildings make money, right?\" Me: 😎 (Rent day, ep. 2)\nDo you know which of your units actually pays? 👇\nSend this to your co-owner 🏢\nLandlord Kit (Excel): occupancy, collection, expenses and result for each property, from your own numbers.\n👉 Link in bio\n#landlord #rentalproperty #realestateinvesting #propertymanagement #cashflow #excel"

R['E2_reparation_landlord_FR'] = dict(D, theme='landlord', lang='fr', music='funk', seed=122, **LF,
  t=dict(FR, l1='« Ma réparation, c\'est pour quand ? » 🥶', hl1=[1, 2], herSays='Ma fournaise ?! 🥶', himSays='Euh… bientôt ?', stagger=True, c1='#7ee0a1', h1='🧢', c2='#ffb86b', h2='🎩',
    guestsL='Jours ouverts', **{'from': 0, 'to': 23}, over=14, cnt=dict(suf=' j'), tokens=['🥶', '📱', '🛠️', '❄️', '💬'],
    clash=[['🛠️', 'fournaise'], ['📅', '23 jours']], l2='23 jours. Une fournaise. En novembre. 😳', hl2=[0, 1, 3],
    l3='Chaque demande suivie au même endroit.', hl3=[1, 2], l4='Planifiée jeudi. Locataire au chaud. 🔥', hl4=[0, 1, 3, 4],
    seatsL='Fournaise · jours', r1=dict(**{'from': 0, 'to': 23}, suf=' j'), alertL='Priorité', alertBad='⚠️ oubliée', alertOk='haute · planifiée ✓',
    fin=['🔥', '🛠️'], ep='Jour de loyer · ép. 1', file='Kit_Proprietaire.xlsx', brand='Kit Propriétaire · Maker FlowTools'))
CAP['E2_reparation_landlord_FR'] = "Le locataire : « Ma réparation, c'est pour quand ? » 🥶 (Jour de loyer, épisode 1)\nTu suis tes demandes de réparation comment, toi ? 👇\nEnvoie ça à un proprio 🏠\nKit Propriétaire (Excel) : chaque demande avec priorité, statut, entrepreneur, coût et nombre de jours ouverts.\n👉 Lien dans la bio\n#propriétaire #immobilier #plex #québec #locataire #excel"

R['E3_ex_seat_EN'] = dict(D, theme='seat', lang='en', music='lofi', seed=133,
  end=dict(name='Seat &amp; Vow', sub='The fiancés · episode 2<br>Excel seating planner · EN / FR', btn='👉 Link in bio', btn2='📤 Tag your other half'),
  t=dict(EN, l1='Him: "My ex is coming." Her: 😐', hl1=[0, 2, 3], herSays='Your EX?! 😐', himSays='…and her new boyfriend.', stagger=True, bubFs=42, both=True,
    guestsL='Table 4', **{'from': 3, 'to': 8}, cnt=dict(suf=' / 8'), names=B.G,
    clash=[['😬', 'the ex'], ['😐', 'the bride']], l2='Same table. Table 4. 😳', hl2=[0, 1],
    l3='The workbook flags it. You move them.', hl3=[1, 2], l4='Table 4 and table 9. Peace. 💍', hl4=[0, 1, 2, 3, 4],
    seatsL='Table 4', r1=dict(**{'from': 8, 'to': 7}, of=' / 8'), alertL='Keep apart', alertBad='⚠️ same table', alertOk='separated ✓',
    ep='The fiancés · ep. 2', file='Seat_and_Vow.xlsx', brand='Seat & Vow · Maker FlowTools'))
CAP['E3_ex_seat_EN'] = "Him: \"My ex is coming.\" Her: 😐 (The fiancés, ep. 2)\nWould you invite your ex to your wedding? 👇\nTag your other half 💍\nSeat & Vow (Excel): you decide who sits where, the workbook flags two guests who must not share a table.\n👉 Link in bio\n#weddingplanning #seatingchart #wedding #bride2027 #engaged #weddingtips"

R['E4_shoebox_landlord_EN'] = dict(D, theme='landlord', lang='en', music='tropical', seed=144, **LL,
  t=dict(EN, l1='Accountant: "Rent records?" Me: 📦', hl1=[0, 1, 2], herSays='Rent records, please 📋', himSays='Here… a shoebox 📦', stagger=True, c1='#b39dff', h1='🎓', c2='#7ee0a1', h2='🎩',
    guestsL='Receipts', **{'from': 0, 'to': 214}, tokens=['🧾', '🧾', '📝', '💵', '🧾'],
    clash=[['📦', 'shoebox'], ['📅', 'due Friday']], l2='214 receipts. In a shoebox. 😳', hl2=[0, 4],
    l3='Every unit, every month, one file.', hl3=[0, 1, 5], l4='Sent before Friday. Accountant happy. 📊', hl4=[0, 1, 4],
    seatsL='Rent received', r1=dict(**{'from': 0, 'to': 31800}, pre='$', of=''), alertL='Unpaid', alertBad='❓ somewhere', alertOk='$980 · Unit 202 ✓',
    fin=['📊', '✅'], ep='Rent day · ep. 3', file='Landlord_Kit.xlsx', brand='Landlord Kit · Maker FlowTools'))
CAP['E4_shoebox_landlord_EN'] = "Accountant: \"Send me your rent records.\" Me: 📦 (Rent day, ep. 3)\nWhere are YOUR rent records right now? 👇\nSend this to a landlord friend before tax season 🏠\nLandlord Kit (Excel): rent received and unpaid for every unit and month, on one dashboard.\n👉 Link in bio\n#landlord #rentalproperty #taxseason #propertymanagement #realestateinvesting #excel"

R['E5_traiteur_seat_FR'] = dict(D, theme='seat', lang='fr', music='future', seed=155,
  end=dict(name='Seat &amp; Vow', sub='Les fiancés · épisode 3<br>Plan de table Excel · FR / EN', btn='👉 Lien dans la bio', btn2='📤 Identifie ta moitié'),
  t=dict(FR, l1='Le traiteur : « Combien de végés ? » Eux : 🫠', hl1=[4, 5], herSays='Combien de végés ?! 🥗', himSays='Euh… dix ?', stagger=True, both=True,
    guestsL='Invités', **{'from': 0, 'to': 128}, tokens=['🥗', '🐟', '🍗', '🥗', '🍰'],
    clash=[['🥗', 'végé ?'], ['⏰', 'demain 9 h']], l2='128 invités. Réponse demain 9 h. 😳', hl2=[0, 3, 4],
    l3='Le classeur compte les repas.', hl3=[1, 3, 4], l4='Chiffres envoyés. Traiteur content. 🍽️', hl4=[0, 3],
    seatsL='Repas', r1=dict(**{'from': 0, 'to': 128}, of=' / 128'), alertL='Végé', alertBad='❓', alertOk='17 ✓',
    fin=['🍽️', '💍'], ep='Les fiancés · ép. 3', file='Seat_and_Vow.xlsx', brand='Seat & Vow · Maker FlowTools'))
CAP['E5_traiteur_seat_FR'] = "Le traiteur : « Combien de végés ? » Eux : 🫠 (Les fiancés, épisode 3)\nChez vous, c'est qui qui gère le traiteur ? 👇\nIdentifie ta moitié 💍\nSeat & Vow (Excel) : à mesure que vous placez vos invités, le classeur compte les repas pour le traiteur.\n👉 Lien dans la bio\n#mariage #plandetable #mariagequébec #traiteur #organisationmariage #mariage2027"

R['E6_bilingual_landlord_EN'] = dict(D, theme='landlord', lang='en', music='lofi', seed=166, **LL,
  t=dict(EN, l1='New tenant only texts in French. Me: 😳', hl1=[3, 4, 5], herSays='Le loyer est payé ! 🇫🇷', himSays='…huh? 😳', stagger=True, c1='#8fb3ff', h1='🥖', c2='#7ee0a1', h2='🎩',
    guestsL='Understood', **{'from': 100, 'to': 12}, cnt=dict(suf='%'), tokens=['💬', '🇫🇷', '💬', '📱', '❓'],
    clash=[['🇫🇷', 'reçu ?'], ['🇬🇧', 'receipt?']], l2='Receipts, notices, all in French? 😳', hl2=[3, 4],
    l3='One cell. The whole file switches.', hl3=[0, 1, 4], l4='Bilingual tenant. Bilingual file. 🇨🇦', hl4=[0, 2],
    seatsL='Language', r1=dict(txt=['English', 'Français ✓']), alertL='Receipt', alertBad='❓ English only', alertOk='en français ✓',
    fin=['🇨🇦', '🤝'], ep='Rent day · ep. 4', file='Landlord_Kit.xlsx', brand='Landlord Kit · Maker FlowTools'))
CAP['E6_bilingual_landlord_EN'] = "New tenant only texts in French. Me: 😳 (Rent day, ep. 4)\nEver had a tenant who speaks another language? 👇\nSend this to a landlord in Canada 🇨🇦\nLandlord Kit (Excel): switch the whole workbook between English and French in one cell.\n👉 Link in bio\n#landlord #canada #bilingual #rentalproperty #propertymanagement #excel"

PLACE = {'d11A': 'E1_partner_landlord_EN', 'd18A': 'E2_reparation_landlord_FR', 'd19A': 'E3_ex_seat_EN',
         'd21A': 'E4_shoebox_landlord_EN', 'd22A': 'E5_traiteur_seat_FR', 'd25A': 'E6_bilingual_landlord_EN'}
if __name__ == '__main__':
    reels = [dict(r, id=k, engine='trend.html') for k, r in R.items()]
    json.dump({'reels': reels}, open(os.path.join(here, 'duos2.json'), 'w'), ensure_ascii=False, indent=1)
    json.dump(CAP, open(os.path.join(here, 'duos2_captions.json'), 'w'), ensure_ascii=False, indent=1)
    print(len(reels), 'duos2')
