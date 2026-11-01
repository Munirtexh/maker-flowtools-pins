"""Builds reels.json (animation configs) + captions for the Nov-Dec 2026 animated reels.
Run: python3 build_configs.py  -> writes reels.json next to this file.
Each concept has fr/en texts; SLOTS maps a manifest id to (concept, lang)."""
import json, os

P = {  # product-level settings
 'landlord': dict(tag={'fr': 'Kit Propriétaire', 'en': 'Landlord Kit'}, file={'fr': 'Kit_Proprietaire.xlsx', 'en': 'Landlord_Kit.xlsx'},
   tabs={'fr': ['Tableau de bord', 'Loyers', 'Dépenses', 'Réparations', 'Baux'], 'en': ['Dashboard', 'Rent', 'Expenses', 'Repairs', 'Leases']},
   name={'fr': 'Kit<br>Propriétaire', 'en': 'Landlord<br>Kit'}, listing='4601215754',
   tags={'fr': '#propriétaire #immobilier #excel #québec', 'en': '#landlord #rentalproperty #excel #canada'}),
 'treasurer': dict(tag={'fr': 'Kit Trésorier', 'en': 'Treasurer Kit'}, file={'fr': 'Kit_Tresorier.xlsx', 'en': 'Treasurer_Kit.xlsx'},
   tabs={'fr': ['Tableau de bord', 'Cotisations', 'Budget', 'Conciliation', 'Rapport'], 'en': ['Dashboard', 'Dues', 'Budget', 'Reconcile', 'Report']},
   name={'fr': 'Kit<br>Trésorier', 'en': 'Treasurer<br>Kit'}, listing='4604205273',
   tags={'fr': '#trésorier #association #clubétudiant #budget', 'en': '#treasurer #studentclub #nonprofit #budget'}),
 'seat': dict(tag={'fr': 'Seat & Vow', 'en': 'Seat & Vow'}, file={'fr': 'Seat_and_Vow.xlsx', 'en': 'Seat_and_Vow.xlsx'},
   tabs={'fr': ['Invités', 'Tables', 'Alertes', 'Traiteur'], 'en': ['Guests', 'Tables', 'Alerts', 'Caterer']},
   name={'fr': 'Seat<br>&amp; Vow', 'en': 'Seat<br>&amp; Vow'}, listing='4599884340',
   tags={'fr': '#mariage #planDeTable #organisationmariage #mariageQuébec', 'en': '#weddingplanning #seatingchart #wedding #bride2027'}),
 'habit': dict(tag={'fr': 'Rhythm 2027', 'en': 'Rhythm 2027'}, file={'fr': 'Rhythm_Habit_Tracker_2027.xlsx', 'en': 'Rhythm_Habit_Tracker_2027.xlsx'},
   tabs={'fr': ['Habitudes', 'Janvier', 'Année', 'Tableau de bord'], 'en': ['Habits', 'January', 'Year', 'Dashboard']},
   name={'fr': 'Rhythm Habit<br>Tracker 2027', 'en': 'Rhythm Habit<br>Tracker 2027'}, listing='4596451684',
   tags={'fr': '#habitudes #2027 #excel #organisation', 'en': '#habittracker #2027goals #excel #productivity'}),
 'artisan': dict(tag={'fr': 'Artisan Empire 360°', 'en': 'Artisan Empire 360°'}, file={'fr': 'Artisan_Empire_360.xlsx', 'en': 'Artisan_Empire_360.xlsx'},
   tabs={'fr': ['Produits', 'Ventes', 'Événements', 'Tableau de bord'], 'en': ['Products', 'Sales', 'Events', 'Dashboard']},
   name={'fr': 'Artisan<br>Empire 360°', 'en': 'Artisan<br>Empire 360°'}, listing='4594885787',
   tags={'fr': '#artisan #faitmain #créateur #excel', 'en': '#handmadebusiness #etsyseller #maker #excel'}),
}

def L(fr, en): return {'fr': fr, 'en': en}

C = {}
C['A1'] = dict(p='artisan', tabOn=0, emoji='🧮',
  hook=L('Combien il vous reste vraiment par produit ?', 'What do you really keep on each product?'), hl=L([3, 4], [3, 4]),
  wtitle=L('Prix suggéré · Bougie soja 200 g', 'Suggested price · Soy candle 7 oz'),
  widget=L(dict(type='calc', lines=[dict(l='Matériaux', v=6.4, i='🕯️'), dict(l='Emballage', v=1.1, i='📦', c='y'), dict(l='Frais de vente', v=2.35, i='🧾', c='b'), dict(l='Votre temps', v=8, i='⏱️', c='p')], total='Coût total', margin='Marge visée', pct=40, result='Prix suggéré'),
           dict(type='calc', lines=[dict(l='Materials', v=6.4, i='🕯️'), dict(l='Packaging', v=1.1, i='📦', c='y'), dict(l='Selling fees', v=2.35, i='🧾', c='b'), dict(l='Your time', v=8, i='⏱️', c='p')], total='Total cost', margin='Target margin', pct=40, result='Suggested price')),
  floats=L([dict(t=1.2, text='Coût réel ✓', x=640, y=540, c='g', rot=8), dict(t=3.6, text='Marge visée 40 % 💰', x=80, y=1500, c='y', rot=-6)],
           [dict(t=1.2, text='Real cost ✓', x=660, y=540, c='g', rot=8), dict(t=3.6, text='40% target margin 💰', x=80, y=1500, c='y', rot=-6)]),
  sub=L('Coût, marge et prix suggéré<br>pour les artisans', 'Cost, margin and suggested<br>price for makers'),
  cap=L('Artisan Empire 360° (Excel) calcule le coût réel de chaque produit, votre marge et un prix suggéré.', 'Artisan Empire 360° (Excel) works out the real cost of each product, your margin and a suggested price.'))
C['A2'] = dict(p='artisan', tabOn=0, emoji='🎄',
  hook=L('Quel produit sera en rupture avant les fêtes ?', 'Which product runs out before the holidays?'), hl=L([4], [3, 4]),
  wtitle=L('Inventaire · alerte de stock bas', 'Inventory · low-stock alert'),
  widget=L(dict(type='stock', unit='u.', low='Stock bas 🔔', items=[dict(n='Bougie soja', **{'from': 24}, to=3, min=5), dict(n='Savon lavande', **{'from': 30}, to=14, min=5), dict(n='Bonnet tricoté', **{'from': 12}, to=2, min=4), dict(n='Carte florale', **{'from': 40}, to=22, min=8)]),
           dict(type='stock', unit='pcs', low='Low stock 🔔', items=[dict(n='Soy candle', **{'from': 24}, to=3, min=5), dict(n='Lavender soap', **{'from': 30}, to=14, min=5), dict(n='Knit beanie', **{'from': 12}, to=2, min=4), dict(n='Floral card', **{'from': 40}, to=22, min=8)])),
  floats=L([dict(t=3.4, text='À refaire avant Noël 📦', x=70, y=1490, c='r', rot=-6)], [dict(t=3.4, text='Restock before Christmas 📦', x=60, y=1490, c='r', rot=-6)]),
  sub=L('Stock, coûts, ventes et marges<br>dans un seul classeur', 'Stock, costs, sales and margins<br>in one workbook'),
  cap=L('Une alerte de stock bas s\'affiche avant la rupture, pour refaire les bons produits à temps.', 'A low-stock alert shows up before you run out, so you restock the right products in time.'))
C['A3'] = dict(p='artisan', tabOn=3, emoji='🏆',
  hook=L('Marché ou Etsy : où vendez-vous le plus ?', 'Markets or Etsy: where do you sell most?'), hl=L([6, 7], [6, 7]),
  wtitle=L('Ventes par canal · 2026', 'Sales by channel · 2026'),
  widget=L(dict(type='bars', flag=0, rows=[dict(l='Marchés', v=2140, max=2500, c='y', f='cur0'), dict(l='Etsy', v=1380, max=2500, c='o', f='cur0'), dict(l='Commandes directes', v=620, max=2500, c='b', f='cur0'), dict(l='Boutiques dépôt', v=410, max=2500, c='p', f='cur0')], total=dict(l='Ventes de l\'année', v=4550, f='cur0', c='g')),
           dict(type='bars', flag=0, rows=[dict(l='Markets', v=2140, max=2500, c='y', f='cur0'), dict(l='Etsy', v=1380, max=2500, c='o', f='cur0'), dict(l='Direct orders', v=620, max=2500, c='b', f='cur0'), dict(l='Consignment shops', v=410, max=2500, c='p', f='cur0')], total=dict(l='Sales this year', v=4550, f='cur0', c='g'))),
  floats=L([dict(t=3.2, text='Meilleur canal 🏆', x=600, y=540, c='y', rot=8)], [dict(t=3.2, text='Best channel 🏆', x=620, y=540, c='y', rot=8)]),
  sub=L('Un journal des ventes par canal,<br>un tableau de bord annuel', 'A sales log by channel,<br>an annual dashboard'),
  cap=L('Le journal des ventes par canal montre d\'où vient votre argent : marchés, Etsy ou ailleurs.', 'The sales log by channel shows where your money comes from: markets, Etsy or elsewhere.'))
C['A4'] = dict(p='artisan', tabOn=2, emoji='🎪',
  hook=L('Ce marché de Noël valait-il vraiment le coup ?', 'Was that Christmas market really worth it?'), hl=L([4, 5], [4, 5]),
  wtitle=L('Verdict par événement', 'Verdict per event'),
  widget=L(dict(type='verdict', l=['Ventes', 'Coûts', 'Profit'], items=[dict(n='Marché de Noël', rev=860, cost=310, v='À refaire', c='g'), dict(n='Salon d\'automne', rev=420, cost=395, v='Équilibre', c='y'), dict(n='Foire du village', rev=180, cost=260, v='Perte', c='r')]),
           dict(type='verdict', l=['Sales', 'Costs', 'Profit'], items=[dict(n='Christmas market', rev=860, cost=310, v='Repeat', c='g'), dict(n='Fall craft fair', rev=420, cost=395, v='Break-even', c='y'), dict(n='Village fair', rev=180, cost=260, v='Loss', c='r')])),
  floats=L([dict(t=3.6, text='Profit réel ✓', x=640, y=540, c='g', rot=8)], [dict(t=3.6, text='Real profit ✓', x=640, y=540, c='g', rot=8)]),
  sub=L('Le verdict de chaque marché,<br>chiffres à l\'appui', 'A verdict for every market,<br>backed by numbers'),
  cap=L('Kiosque, frais, ventes : Artisan Empire 360° donne un verdict pour chaque événement. On y retourne ou pas ?', 'Booth fee, costs, sales: Artisan Empire 360° gives each event a verdict. Go back or skip it?'))
C['H1'] = dict(p='habit', tabOn=1, emoji='🌿',
  hook=L('Un jour manqué ? C\'est un trou, pas un échec.', 'Missed a day? It\'s a gap, not a failure.'), hl=L([6, 9], [5, 8]),
  wtitle=L('Lecture 20 min · 13 semaines', 'Reading 20 min · 13 weeks'),
  widget=L(dict(type='heat', gap=[6, 3], legend=[dict(l='Fait', c='g'), dict(l='Version minimale', c='y'), dict(l='Repos prévu', c='b')], stats=[dict(l='Jours faits', v=71, c='g'), dict(l='Série en cours', v=12, c='y')]),
           dict(type='heat', gap=[6, 3], legend=[dict(l='Done', c='g'), dict(l='Minimum version', c='y'), dict(l='Planned rest', c='b')], stats=[dict(l='Days done', v=71, c='g'), dict(l='Current streak', v=12, c='y')])),
  floats=L([dict(t=2.8, text='Pas grave, on continue 💚', x=60, y=540, c='m', rot=-6)], [dict(t=2.8, text='No guilt, keep going 💚', x=80, y=540, c='m', rot=-6)]),
  sub=L('Fait, version minimale ou repos prévu.<br>Excel, français + English', 'Done, minimum version or planned rest.<br>Excel, English + Français'),
  cap=L('Rhythm Habit Tracker 2027 : un jour manqué reste vide, sans culpabilité. Fait, version minimale ou repos prévu.', 'Rhythm Habit Tracker 2027: a missed day just stays blank, no guilt. Done, minimum version or planned rest.'))
C['H2'] = dict(p='habit', tabOn=2, emoji='📅',
  hook=L('Votre année 2027 en un coup d\'œil', 'Your whole 2027 at a glance'), hl=L([2], [2]),
  wtitle=L('Vue de l\'année · 2027', 'Year view · 2027'),
  widget=L(dict(type='heat', states=['g', 'g', 'g', 'g', 'y', 'b', 'g', 'y', 'x'], legend=[dict(l='Fait', c='g'), dict(l='Minimum', c='y'), dict(l='Repos', c='b')], stats=[dict(l='Jours faits', v=214, c='g'), dict(l='Taux de régularité', v=82, f='pct', c='y')]),
           dict(type='heat', states=['g', 'g', 'g', 'g', 'y', 'b', 'g', 'y', 'x'], legend=[dict(l='Done', c='g'), dict(l='Minimum', c='y'), dict(l='Rest', c='b')], stats=[dict(l='Days done', v=214, c='g'), dict(l='Consistency', v=82, f='pct', c='y')])),
  floats=L([dict(t=2.6, text='Meilleur mois : mars 🔥', x=90, y=1500, c='y', rot=-6)], [dict(t=2.6, text='Best month: March 🔥', x=110, y=1500, c='y', rot=-6)]),
  sub=L('Une carte de chaque jour<br>et votre meilleur mois', 'A map of every day<br>and your best month'),
  cap=L('La vue de l\'année montre chaque jour où vous avez tenu vos habitudes, et votre meilleur mois.', 'The year view shows every day you kept your habits, and your strongest month.'))
C['H3'] = dict(p='habit', tabOn=0, emoji='🎯',
  hook=L('Jusqu\'à 20 habitudes, une cible par semaine', 'Up to 20 habits, one target per week'), hl=L([1, 2], [2, 3]),
  wtitle=L('Cette semaine', 'This week'),
  widget=L(dict(type='bars', rh=104, rows=[dict(l='Marcher 30 min', v=5, max=5, c='g', vt='5 / 5 ✓'), dict(l='Lire 20 min', v=4, max=5, c='m', vt='4 / 5'), dict(l='Boire 2 L d\'eau', v=6, max=7, c='b', vt='6 / 7'), dict(l='Méditer', v=2, max=3, c='y', vt='2 / 3'), dict(l='Étirements', v=3, max=4, c='p', vt='3 / 4'), dict(l='Pas d\'écran au lit', v=4, max=7, c='o', vt='4 / 7')]),
           dict(type='bars', rh=104, rows=[dict(l='Walk 30 min', v=5, max=5, c='g', vt='5 / 5 ✓'), dict(l='Read 20 min', v=4, max=5, c='m', vt='4 / 5'), dict(l='Drink 2 L of water', v=6, max=7, c='b', vt='6 / 7'), dict(l='Meditate', v=2, max=3, c='y', vt='2 / 3'), dict(l='Stretch', v=3, max=4, c='p', vt='3 / 4'), dict(l='No screens in bed', v=4, max=7, c='o', vt='4 / 7')])),
  floats=L([dict(t=2.0, text='Cible atteinte 🎯', x=620, y=540, c='g', rot=8)], [dict(t=2.0, text='Target hit 🎯', x=660, y=540, c='g', rot=8)]),
  sub=L('Des cibles réalistes,<br>semaine après semaine', 'Realistic targets,<br>week after week'),
  cap=L('Jusqu\'à 20 habitudes, chacune avec sa cible de la semaine (de 1 à 7 jours). Réaliste, donc tenable.', 'Up to 20 habits, each with its own weekly target (1 to 7 days). Realistic, so you stick with it.'))
C['H4'] = dict(p='habit', tabOn=0, emoji='🇨🇦',
  hook=L('Votre suivi 2027, en français ou en anglais', 'Your 2027 tracker, in English or French'), hl=L([4, 7], [4, 6]),
  wtitle=L('Une case change toute la langue', 'One cell switches the language'),
  widget=L(dict(type='toggle', cell='Langue / Language', k=['FR', 'EN'], pairs=[['Habitudes', 'Habits', 'g', '✓'], ['Cible par semaine', 'Weekly target', 'y', '🎯'], ['Repos prévu', 'Planned rest', 'b', '🌿'], ['Version minimale', 'Minimum version', 'o', '½'], ['Tableau de bord', 'Dashboard', 'p', '📊']]),
           dict(type='toggle', cell='Language / Langue', k=['EN', 'FR'], pairs=[['Habits', 'Habitudes', 'g', '✓'], ['Weekly target', 'Cible par semaine', 'y', '🎯'], ['Planned rest', 'Repos prévu', 'b', '🌿'], ['Minimum version', 'Version minimale', 'o', '½'], ['Dashboard', 'Tableau de bord', 'p', '📊']])),
  floats=L([dict(t=1.6, text='Prêt pour le 1er janvier 🗓️', x=60, y=1500, c='m', rot=-5)], [dict(t=1.6, text='Ready for January 1st 🗓️', x=90, y=1500, c='m', rot=-5)]),
  sub=L('Fait pour le Canada 🇨🇦<br>une case, deux langues', 'Made for Canada 🇨🇦<br>one cell, two languages'),
  cap=L('Rhythm Habit Tracker 2027 passe du français à l\'anglais avec une seule case. Prêt pour le 1er janvier.', 'Rhythm Habit Tracker 2027 switches between English and French with one cell. Ready for January 1st.'))
C['L1'] = dict(p='landlord', tabOn=1, emoji='🟩',
  hook=L('Qui a payé son loyer ce mois-ci ?', 'Who paid rent this month?'), hl=L([3, 4], [2, 3]),
  wtitle=L('Loyers · novembre', 'Rent · November'),
  widget=L(dict(type='status', rows=[dict(n='Logement 101', s='Loyer 1 250 $', st='Payé ✓', c='g', i='🏠', ac='g'), dict(n='Logement 102', s='Loyer 1 100 $', st='Partiel', c='y', i='🏠', ac='y'), dict(n='Logement 201', s='Loyer 1 325 $', st='Payé ✓', c='g', i='🏠', ac='g'), dict(n='Logement 202', s='Loyer 980 $', st='Impayé', c='r', i='🏠', ac='r'), dict(n='Logement 301', s='Loyer 1 400 $', st='Payé ✓', c='g', i='🏠', ac='g'), dict(n='Logement 302', s='Loyer 1 150 $', st='Payé ✓', c='g', i='🏠', ac='g')]),
           dict(type='status', rows=[dict(n='Unit 101', s='Rent $1,250', st='Paid ✓', c='g', i='🏠', ac='g'), dict(n='Unit 102', s='Rent $1,100', st='Partial', c='y', i='🏠', ac='y'), dict(n='Unit 201', s='Rent $1,325', st='Paid ✓', c='g', i='🏠', ac='g'), dict(n='Unit 202', s='Rent $980', st='Unpaid', c='r', i='🏠', ac='r'), dict(n='Unit 301', s='Rent $1,400', st='Paid ✓', c='g', i='🏠', ac='g'), dict(n='Unit 302', s='Rent $1,150', st='Paid ✓', c='g', i='🏠', ac='g')])),
  floats=L([dict(t=3.2, text='Vert = payé · Rouge = à suivre', x=50, y=1500, c='g', rot=-4)], [dict(t=3.2, text='Green = paid · Red = follow up', x=60, y=1500, c='g', rot=-4)]),
  sub=L('Loyers, dépenses, réparations<br>et baux au même endroit', 'Rent, expenses, repairs<br>and leases in one place'),
  cap=L('Une grille verte / rouge pour chaque logement et chaque mois. Vous voyez tout de suite qui a payé.', 'A green / red grid for every unit and every month. You see right away who paid.'))
C['L3'] = dict(p='landlord', tabOn=4, emoji='📆',
  hook=L('Quel bail se termine bientôt ?', 'Which lease ends soon?'), hl=L([1, 4], [1, 3]),
  wtitle=L('Échéances à venir', 'Upcoming deadlines'),
  widget=L(dict(type='status', rh=118, rows=[dict(n='Logement 202', s='Renouvellement', v=0, cnt=[120, 45], st='À faire', c='r', i='🔔', ac='r'), dict(n='Logement 101', s='Fin du bail', v=0, cnt=[180, 112], st='Bientôt', c='y', i='📄', ac='y'), dict(n='Immeuble Rosemont', s='Assurance', v=0, cnt=[240, 198], st='OK', c='g', i='🛡️', ac='g'), dict(n='Logement 102', s='Fin du bail', v=0, cnt=[300, 265], st='OK', c='g', i='📄', ac='g')]),
           dict(type='status', rh=118, rows=[dict(n='Unit 202', s='Renewal', v=0, cnt=[120, 45], st='To do', c='r', i='🔔', ac='r'), dict(n='Unit 101', s='Lease end', v=0, cnt=[180, 112], st='Soon', c='y', i='📄', ac='y'), dict(n='Maple Ave building', s='Insurance', v=0, cnt=[240, 198], st='OK', c='g', i='🛡️', ac='g'), dict(n='Unit 102', s='Lease end', v=0, cnt=[300, 265], st='OK', c='g', i='📄', ac='g')])),
  floats=L([dict(t=2.4, text='Rien ne glisse 🔔', x=630, y=540, c='y', rot=8)], [dict(t=2.4, text='Nothing slips 🔔', x=640, y=540, c='y', rot=8)]),
  sub=L('Fins de bail, renouvellements<br>et assurances suivis', 'Lease ends, renewals<br>and insurance, tracked'),
  cap=L('Fins de bail, renouvellements, assurances : les jours qui restent sont comptés pour vous.', 'Lease ends, renewals, insurance: the days left are counted for you.'))
C['L4'] = dict(p='landlord', tabOn=3, emoji='🛠️',
  hook=L('Cette réparation est-elle encore ouverte ?', 'Is that repair still open?'), hl=L([4], [3, 4]),
  wtitle=L('Réparations', 'Repairs'),
  widget=L(dict(type='status', rh=118, rows=[dict(n='Fuite sous l\'évier · 102', s='Plombier · ouverte depuis 4 j', v=180, f='cur0', st='Urgent', c='r', i='🔧', ac='r'), dict(n='Thermostat · 201', s='Électricien · 2 j', v=95, f='cur0', st='En cours', c='y', i='🔌', ac='y'), dict(n='Peinture · 101', s='À planifier', v=240, f='cur0', st='Ouverte', c='b', i='🎨', ac='b'), dict(n='Porte d\'entrée · 301', s='Terminée', v=130, f='cur0', st='Fermée ✓', c='g', i='🚪', ac='g')]),
           dict(type='status', rh=118, rows=[dict(n='Sink leak · 102', s='Plumber · open 4 days', v=180, f='cur0', st='Urgent', c='r', i='🔧', ac='r'), dict(n='Thermostat · 201', s='Electrician · 2 days', v=95, f='cur0', st='In progress', c='y', i='🔌', ac='y'), dict(n='Paint · 101', s='To schedule', v=240, f='cur0', st='Open', c='b', i='🎨', ac='b'), dict(n='Front door · 301', s='Done', v=130, f='cur0', st='Closed ✓', c='g', i='🚪', ac='g')])),
  floats=L([dict(t=2.6, text='1 urgente ⚠️', x=680, y=540, c='r', rot=8)], [dict(t=2.6, text='1 urgent ⚠️', x=700, y=540, c='r', rot=8)]),
  sub=L('Priorité, statut, entrepreneur,<br>coût et jours ouverts', 'Priority, status, contractor,<br>cost and days open'),
  cap=L('Chaque réparation avec sa priorité, son statut, l\'entrepreneur, le coût et le nombre de jours ouverte.', 'Every repair with its priority, status, contractor, cost and how many days it has been open.'))
C['L5'] = dict(p='landlord', tabOn=0, emoji='🇨🇦',
  hook=L('Un seul fichier, deux langues', 'One file, two languages'), hl=L([3, 4], [2, 3]),
  wtitle=L('Une case change toute la langue', 'One cell switches the language'),
  widget=L(dict(type='toggle', cell='Langue / Language', k=['FR', 'EN'], pairs=[['Loyers perçus', 'Rent received', 'g', '💵'], ['Dépenses', 'Expenses', 'r', '🧾'], ['Réparations', 'Repairs', 'y', '🔧'], ['Baux', 'Leases', 'b', '📄'], ['Tableau de bord', 'Dashboard', 'p', '📊']]),
           dict(type='toggle', cell='Language / Langue', k=['EN', 'FR'], pairs=[['Rent received', 'Loyers perçus', 'g', '💵'], ['Expenses', 'Dépenses', 'r', '🧾'], ['Repairs', 'Réparations', 'y', '🔧'], ['Leases', 'Baux', 'b', '📄'], ['Dashboard', 'Tableau de bord', 'p', '📊']])),
  floats=L([dict(t=1.8, text='Fait pour le Québec ⚜️', x=80, y=1500, c='b', rot=-5)], [dict(t=1.8, text='Made for Canada 🍁', x=120, y=1500, c='b', rot=-5)]),
  sub=L('Français, English ou les deux,<br>avec une seule case', 'English, Français or both,<br>with one cell'),
  cap=L('Le Kit Propriétaire passe du français à l\'anglais avec une seule case. Pratique avec un associé ou un locataire anglophone.', 'The Landlord Kit switches between English and French with one cell. Handy with a partner or a French-speaking tenant.'))
C['T1'] = dict(p='treasurer', tabOn=1, emoji='👀',
  hook=L('Qui n\'a pas encore payé sa cotisation ?', 'Who still hasn\'t paid their dues?'), hl=L([6], [5]),
  wtitle=L('Cotisations · automne', 'Dues · fall term'),
  widget=L(dict(type='status', rows=[dict(n='Alex M.', s='40 $', st='Payé ✓', c='g', ac='g'), dict(n='Jade L.', s='20 $ sur 40 $', st='Partiel', c='y', ac='y'), dict(n='Sam K.', s='0 $ sur 40 $', st='Impayé', c='r', ac='r'), dict(n='Noah P.', s='40 $', st='Payé ✓', c='g', ac='g'), dict(n='Léa R.', s='40 $', st='Payé ✓', c='g', ac='g')], bubble='Salut Sam ! Petit rappel : ta cotisation de 40 $ est encore ouverte 🙂'),
           dict(type='status', rows=[dict(n='Alex M.', s='$40', st='Paid ✓', c='g', ac='g'), dict(n='Jade L.', s='$20 of $40', st='Partial', c='y', ac='y'), dict(n='Sam K.', s='$0 of $40', st='Unpaid', c='r', ac='r'), dict(n='Noah P.', s='$40', st='Paid ✓', c='g', ac='g'), dict(n='Léa R.', s='$40', st='Paid ✓', c='g', ac='g')], bubble='Hi Sam! Friendly reminder: your $40 club dues are still open 🙂')),
  floats=L([dict(t=3.4, text='Rappel prêt à copier 📋', x=80, y=1500, c='y', rot=-5)], [dict(t=3.4, text='Reminder ready to copy 📋', x=80, y=1500, c='y', rot=-5)]),
  sub=L('Statut payé / partiel / impayé<br>qui se met à jour seul', 'Paid / partial / unpaid status<br>that updates itself'),
  cap=L('Le statut (payé / partiel / impayé) se met à jour seul et un texte de rappel est prêt à copier.', 'The status (paid / partial / unpaid) updates itself and a reminder message is ready to copy.'))
C['T2'] = dict(p='treasurer', tabOn=3, emoji='🤔',
  hook=L('La banque dit un chiffre, vos livres un autre', 'The bank says one number, your books another'), hl=L([1, 6], [1, 6]),
  wtitle=L('Conciliation bancaire · octobre', 'Bank reconciliation · October'),
  widget=L(dict(type='counter', a=dict(l='Relevé bancaire', v=1842.5), b=dict(l='Vos livres', v=1597.2), label='Écart à expliquer', **{'from': 245.3}, steps=[dict(l='Chèque pas encore encaissé', v=180), dict(l='Dépôt pas encore inscrit', v=72.8), dict(l='Frais bancaires', v=-12.5), dict(l='Intérêts', v=5)], done='Écart 0,00 $ ✓'),
           dict(type='counter', a=dict(l='Bank statement', v=1842.5), b=dict(l='Your books', v=1597.2), label='Gap to explain', **{'from': 245.3}, steps=[dict(l='Cheque not cashed yet', v=180), dict(l='Deposit not recorded yet', v=72.8), dict(l='Bank fees', v=-12.5), dict(l='Interest', v=5)], done='Gap $0.00 ✓')),
  floats=L([dict(t=4.2, text='Ça balance 🎉', x=650, y=540, c='g', rot=8)], [dict(t=4.2, text='It balances 🎉', x=640, y=540, c='g', rot=8)]),
  sub=L('L\'onglet Conciliation ramène<br>l\'écart à 0,00, étape par étape', 'The Reconcile tab brings<br>the gap to 0.00, step by step'),
  cap=L('Dans le Kit Trésorier, l\'onglet Conciliation vous montre l\'écart et vous aide à le ramener à 0,00 étape par étape.', 'In the Treasurer Kit, the Reconcile tab shows the gap and helps you bring it to 0.00, step by step.'))
C['T3'] = dict(p='treasurer', tabOn=4, emoji='😅',
  hook=L('AG demain et les livres sont en désordre ?', 'Annual meeting tomorrow and the books are a mess?'), hl=L([7], [8]),
  wtitle=L('Rapport financier · réel vs budget', 'Financial report · actual vs budget'),
  widget=L(dict(type='bars', rows=[dict(l='Cotisations', v=1840, max=2000, c='g', f='cur0', of=' / 2 000 $'), dict(l='Collectes de fonds', v=1230, max=1500, c='y', f='cur0', of=' / 1 500 $'), dict(l='Commandites', v=800, max=800, c='b', f='cur0', of=' / 800 $'), dict(l='Dépenses d\'activités', v=1460, max=1800, c='r', f='cur0', of=' / 1 800 $')], total=dict(l='Résultat net', v=2410, f='cur0', c='g')),
           dict(type='bars', rows=[dict(l='Dues', v=1840, max=2000, c='g', f='cur0', of=' / $2,000'), dict(l='Fundraisers', v=1230, max=1500, c='y', f='cur0', of=' / $1,500'), dict(l='Sponsors', v=800, max=800, c='b', f='cur0', of=' / $800'), dict(l='Event spending', v=1460, max=1800, c='r', f='cur0', of=' / $1,800')], total=dict(l='Net result', v=2410, f='cur0', c='g'))),
  floats=L([dict(t=3.0, text='Prêt à imprimer 🖨️', x=640, y=540, c='y', rot=8)], [dict(t=3.0, text='Ready to print 🖨️', x=650, y=540, c='y', rot=8)]),
  sub=L('Choisissez la période,<br>imprimez le rapport', 'Pick the period,<br>print the report'),
  cap=L('Choisissez la période, vérifiez les totaux, imprimez le rapport financier. Un seul classeur, français ou anglais.', 'Pick a period, check the totals, print the financial report. One workbook, English or French.'))
C['T4'] = dict(p='treasurer', tabOn=2, emoji='🧁',
  hook=L('Cette vente de pâtisseries valait-elle la peine ?', 'Was that bake sale actually worth it?'), hl=L([3], [2, 3]),
  wtitle=L('Profit par activité', 'Profit per activity'),
  widget=L(dict(type='verdict', l=['Revenus', 'Coûts', 'Profit'], items=[dict(n='Vente de pâtisseries', rev=640, cost=180, v='À refaire', c='g'), dict(n='Soirée quiz', rev=420, cost=400, v='Équilibre', c='y'), dict(n='Lave-auto', rev=150, cost=210, v='Perte', c='r')]),
           dict(type='verdict', l=['Revenue', 'Costs', 'Profit'], items=[dict(n='Bake sale', rev=640, cost=180, v='Repeat', c='g'), dict(n='Trivia night', rev=420, cost=400, v='Break-even', c='y'), dict(n='Car wash', rev=150, cost=210, v='Loss', c='r')])),
  floats=L([dict(t=3.6, text='Verdict clair ✓', x=640, y=540, c='g', rot=8)], [dict(t=3.6, text='Clear verdict ✓', x=640, y=540, c='g', rot=8)]),
  sub=L('Le profit de chaque activité<br>et un verdict clair', 'The profit of every activity<br>and a clear verdict'),
  cap=L('Le Kit Trésorier calcule le profit de chaque activité et affiche un verdict : à refaire, à l\'équilibre ou perte.', 'The Treasurer Kit calculates the profit of every activity and shows a verdict: repeat it, break-even or loss.'))
C['T5'] = dict(p='treasurer', tabOn=2, emoji='💸',
  hook=L('Quelle part du budget est déjà dépensée ?', 'How much of your budget is already spent?'), hl=L([6], [7]),
  wtitle=L('Budget vs réel · par catégorie', 'Budget vs actual · by category'),
  widget=L(dict(type='bars', flag=1, rows=[dict(l='Événements', v=78, max=100, c='y', f='pct'), dict(l='Nourriture', v=92, max=100, c='r', f='pct'), dict(l='Communication', v=45, max=100, c='g', f='pct'), dict(l='Matériel', v=60, max=100, c='b', f='pct')], total=dict(l='Reste à dépenser', v=1240, f='cur0', c='g')),
           dict(type='bars', flag=1, rows=[dict(l='Events', v=78, max=100, c='y', f='pct'), dict(l='Food', v=92, max=100, c='r', f='pct'), dict(l='Promotion', v=45, max=100, c='g', f='pct'), dict(l='Supplies', v=60, max=100, c='b', f='pct')], total=dict(l='Left to spend', v=1240, f='cur0', c='g'))),
  floats=L([dict(t=3.4, text='Nourriture : 92 % ⚠️', x=600, y=540, c='r', rot=8)], [dict(t=3.4, text='Food: 92% ⚠️', x=680, y=540, c='r', rot=8)]),
  sub=L('Budget vs réel, mois par mois,<br>avec ce qui reste', 'Budget vs actual, month by month,<br>with what remains'),
  cap=L('Budget vs réel par catégorie, mois par mois, avec le pourcentage utilisé et ce qui reste.', 'Budget vs actual by category, month by month, with percent used and what remains.'))
C['T6'] = dict(p='treasurer', tabOn=0, emoji='📋',
  hook=L('Nouveau trésorier l\'an prochain ? Ne perdez rien.', 'New treasurer next year? Lose nothing.'), hl=L([1, 7], [1, 5]),
  wtitle=L('Liste de passation', 'Handover checklist'),
  widget=L(dict(type='check', n=15, rh=39, dt=.27, step='Étape', prog='Passation'), dict(type='check', n=15, rh=39, dt=.27, step='Step', prog='Handover')),
  floats=L([dict(t=4.3, text='15 / 15 ✓ Relève prête', x=70, y=1500, c='g', rot=-5)], [dict(t=4.3, text='15 / 15 ✓ Ready to hand over', x=50, y=1500, c='g', rot=-5)]),
  sub=L('Une liste de passation en 15 étapes<br>pour que la relève parte du bon pied', 'A 15-step handover checklist<br>so the next person starts clean'),
  cap=L('Le Kit Trésorier inclut une liste de passation en 15 étapes, pour que la relève parte du bon pied.', 'The Treasurer Kit includes a 15-step handover checklist so the next person starts clean.'))
C['T7'] = dict(p='treasurer', tabOn=0, emoji='📊',
  hook=L('Toute votre association en un coup d\'œil', 'Your whole club at a glance'), hl=L([2], [2]),
  wtitle=L('Tableau de bord · 2026-2027', 'Dashboard · 2026-2027'),
  widget=L(dict(type='kpis', focus=2, tiles=[dict(l='Revenus', v=5120, f='cur0', c='g'), dict(l='Dépenses', v=3870, f='cur0', c='r'), dict(l='Résultat', v=1250, f='cur0', c='g'), dict(l='Solde banque', v=4380, f='cur0', c='b'), dict(l='Cotisations payées', v=86, f='pct', c='y'), dict(l='Budget utilisé', v=64, f='pct', c='p'), dict(l='Membres', v=48, f='int', c='b'), dict(l='Activités', v=7, f='int', c='o'), dict(l='Meilleure collecte', v=640, f='cur0', c='k')]),
           dict(type='kpis', focus=2, tiles=[dict(l='Revenue', v=5120, f='cur0', c='g'), dict(l='Expenses', v=3870, f='cur0', c='r'), dict(l='Net result', v=1250, f='cur0', c='g'), dict(l='Bank balance', v=4380, f='cur0', c='b'), dict(l='Dues paid', v=86, f='pct', c='y'), dict(l='Budget used', v=64, f='pct', c='p'), dict(l='Members', v=48, f='int', c='b'), dict(l='Activities', v=7, f='int', c='o'), dict(l='Best fundraiser', v=640, f='cur0', c='k')])),
  floats=L([dict(t=3.6, text='Rien à saisir deux fois ✓', x=60, y=1500, c='y', rot=-5)], [dict(t=3.6, text='Nothing typed twice ✓', x=100, y=1500, c='y', rot=-5)]),
  sub=L('10 indicateurs et 3 graphiques,<br>faciles à présenter', '10 indicators and 3 charts,<br>easy to present'),
  cap=L('Le tableau de bord du Kit Trésorier : revenus, dépenses, solde, cotisations et budget, faciles à présenter à votre équipe.', 'The Treasurer Kit dashboard: revenue, expenses, balance, dues and budget, easy to present to your team.'))
C['V1'] = dict(p='seat', tabOn=0, emoji='🔎',
  hook=L('Où est assise tante Marie ?', 'Where is Aunt Marie sitting?'), hl=L([3, 4], [2, 3]),
  wtitle=L('Trouver un invité', 'Find a guest'),
  widget=L(dict(type='seat', query='Marie', ph='Rechercher un invité…', hit=3, result='Tante Marie Tremblay', resPill='Table 4', tables=[dict(n='Table 1', c='8 places', k=8), dict(n='Table 2', c='8 places', k=8), dict(n='Table 3', c='8 places', k=8), dict(n='Table 4', c='8 places', k=8)]),
           dict(type='seat', query='Marie', ph='Search a guest…', hit=3, result='Aunt Marie Tremblay', resPill='Table 4', tables=[dict(n='Table 1', c='8 seats', k=8), dict(n='Table 2', c='8 seats', k=8), dict(n='Table 3', c='8 seats', k=8), dict(n='Table 4', c='8 seats', k=8)])),
  floats=L([dict(t=2.4, text='Trouvée en 2 secondes ⚡', x=60, y=1500, c='k', rot=-5)], [dict(t=2.4, text='Found in 2 seconds ⚡', x=100, y=1500, c='k', rot=-5)]),
  sub=L('Une liste alphabétique<br>prête à imprimer', 'An alphabetical guest list,<br>ready to print'),
  cap=L('Seat & Vow retrouve la table de chaque invité en quelques secondes. Vous décidez qui s\'assoit où ; le classeur compte et vérifie.', 'Seat & Vow finds any guest\'s table in seconds. You decide who sits where; the workbook counts and checks.'))
C['V2'] = dict(p='seat', tabOn=1, emoji='🪑',
  hook=L('Toutes les tables, toutes les tailles', 'Any table, any size'), hl=L([2, 5], [1, 3]),
  wtitle=L('Plan des tables', 'Table plan'),
  widget=L(dict(type='tables', seats='places', items=[dict(n='Honneur', k=10, r=88, x=220, y=140, c='y'), dict(n='Enfants', k=6, r=70, x=640, y=140, c='k'), dict(n='Table 3', k=8, r=74, x=150, y=400, c='p'), dict(n='Table 4', k=8, r=74, x=422, y=400, c='b'), dict(n='Table 5', k=8, r=74, x=694, y=400, c='g')], stats=[dict(l='Tables', v=12, c='y'), dict(l='Invités', v=96, c='k'), dict(l='Places libres', v=4, c='g')]),
           dict(type='tables', seats='seats', items=[dict(n='Head', k=10, r=88, x=220, y=140, c='y'), dict(n='Kids', k=6, r=70, x=640, y=140, c='k'), dict(n='Table 3', k=8, r=74, x=150, y=400, c='p'), dict(n='Table 4', k=8, r=74, x=422, y=400, c='b'), dict(n='Table 5', k=8, r=74, x=694, y=400, c='g')], stats=[dict(l='Tables', v=12, c='y'), dict(l='Guests', v=96, c='k'), dict(l='Free seats', v=4, c='g')])),
  floats=L([dict(t=2.0, text='Jusqu\'à 30 tables 🎉', x=620, y=540, c='y', rot=8)], [dict(t=2.0, text='Up to 30 tables 🎉', x=640, y=540, c='y', rot=8)]),
  sub=L('Table d\'honneur, table des enfants,<br>jusqu\'à 30 tables', 'Head table, kids\' table,<br>up to 30 tables'),
  cap=L('Table d\'honneur, table des enfants, tables de 6 ou de 10 : Seat & Vow gère jusqu\'à 30 tables et compte les places pour vous.', 'Head table, kids\' table, tables of 6 or 10: Seat & Vow handles up to 30 tables and counts the seats for you.'))

SLOTS = {  # manifest id: (concept, lang)
 'd04A': ('A1', 'fr'), 'd05A': ('H4', 'en'), 'd06A': ('H1', 'fr'), 'd12A': ('T3', 'fr'), 'd13A': ('T1', 'en'),
 'd14A': ('A3', 'fr'), 'd15A': ('A2', 'en'), 'd16A': ('H4', 'fr'), 'd17A': ('H2', 'en'), 'd23A': ('T2', 'en'),
 'd24A': ('T1', 'fr'), 'd26A': ('A2', 'fr'), 'd27A': ('T3', 'en'), 'd28A': ('H2', 'fr'), 'd31A': ('T4', 'en'),
 'd34A': ('T2', 'fr'), 'd37A': ('T5', 'en'), 'd40A': ('T4', 'fr'), 'd43A': ('T6', 'en'), 'd44A': ('V1', 'fr'),
 'd45A': ('L3', 'en'), 'd46A': ('T5', 'fr'), 'd48A': ('L3', 'fr'), 'd49A': ('H1', 'en'), 'd50A': ('V2', 'fr'),
 'd51A': ('A1', 'en'), 'd52A': ('T6', 'fr'), 'd53A': ('T7', 'en'), 'd54A': ('L4', 'fr'), 'd55A': ('L1', 'en'),
 'd56A': ('T7', 'fr'), 'd57A': ('V1', 'en'), 'd58A': ('L5', 'fr'), 'd59A': ('A4', 'en'), 'd60A': ('A4', 'fr'),
 'd61A': ('L4', 'en'), 'd62A': ('H3', 'fr'), 'd63A': ('V2', 'en'),
}


def build(kit_ids=()):
    reels = []
    for sid, (cid, lg) in SLOTS.items():
        c = C[cid]; p = P[c['p']]
        kit = sid in kit_ids
        btns = ['👆 ' + ('Lien dans la bio' if lg == 'fr' else 'Link in bio')]
        btns.append(('💬 Écris KIT en commentaire' if lg == 'fr' else '💬 Comment KIT') if kit else ('🔖 Enregistre pour plus tard' if lg == 'fr' else '🔖 Save it for later'))
        reels.append(dict(id=f'{cid}_{lg.upper()}', slot=sid, lang=lg, theme=c['p'], tag=p['tag'][lg], hook=c['hook'][lg], hl=c['hl'][lg], emoji=c['emoji'],
            file=p['file'][lg], wtitle=c['wtitle'][lg], tabs=p['tabs'][lg], tabOn=c.get('tabOn', 0), widget=c['widget'][lg], floats=c['floats'][lg],
            chips=['Excel', 'FR / EN', 'Sans macros'] if lg == 'fr' else ['Excel', 'EN / FR', 'No macros'],
            cta=dict(name=p['name'][lg], sub=c['sub'][lg], btns=btns), coverAt=9.0, seed=len(sid) * 7 + int(sid[1:3])))
    return reels


def caption(sid, kit):
    cid, lg = SLOTS[sid]; c = C[cid]; p = P[c['p']]
    lines = [c['hook'][lg] + ' ' + c['emoji'], c['cap'][lg],
             'Excel, FR / EN, sans macros.' if lg == 'fr' else 'Excel, EN / FR, no macros.']
    if kit:
        lines.append('💬 Écris KIT en commentaire et je te réponds avec le lien.' if lg == 'fr' else '💬 Comment KIT and I\'ll reply with the link.')
        lines.append('👉 Ou lien dans la bio' if lg == 'fr' else '👉 Or link in bio')
    else:
        lines.append('👉 Lien dans la bio' if lg == 'fr' else '👉 Link in bio')
    lines.append(p['tags'][lg])
    return '\n'.join(lines)


if __name__ == '__main__':
    here = os.path.dirname(os.path.abspath(__file__))
    man = json.load(open(os.path.join(here, '..', '..', 'ig', 'manifest.json')))
    kit_ids = {e['id'] for e in man if 'KIT' in e['caption'] and e['id'] in SLOTS}
    # keep kit ids recorded even after manifest is rewritten
    kf = os.path.join(here, 'kit_slots.json')
    if os.path.exists(kf): kit_ids = set(json.load(open(kf)))
    else: json.dump(sorted(kit_ids), open(kf, 'w'))
    json.dump({'reels': build(kit_ids)}, open(os.path.join(here, 'reels.json'), 'w'), ensure_ascii=False, indent=1)
    json.dump({sid: caption(sid, sid in kit_ids) for sid in SLOTS}, open(os.path.join(here, 'captions.json'), 'w'), ensure_ascii=False, indent=1)
    print(len(SLOTS), 'reels; KIT slots:', sorted(kit_ids))
