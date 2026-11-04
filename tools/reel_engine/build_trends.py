"""Reels tendance (formats viraux 2026) -> trends.json + trend_captions.json.
Moteur : trend.html (boucle parfaite ~9,6 s, POV lisible dès la 1re image, chaos -> ordre, pas d'écran de pub).
SLOTS : créneau du calendrier ig/manifest.json -> reel. Lancer : python3 build_trends.py"""
import json, os
here = os.path.dirname(os.path.abspath(__file__))
FR = dict(sample="Données d'exemple", seated='Placés', alerts='Alertes', table='Table')
EN = dict(sample='Sample data', seated='Seated', alerts='Alerts', table='Table')
G = ["Emma","Liam","Noah","Ava","Mia","Leo","Zoe","Eli","Ivy","Max","Ana","Sam","Lou","Jade","Ben","Nora"]
def it(l, s, st, c): return dict(l=l, s=s, st=st, c=c)
R = {}
R['TR01_seat_EN'] = dict(format='seatChaos', theme='seat', lang='en', seed=41, t=dict(EN,
  l1="POV: you're doing the seating chart", l2a="and Carol can't sit near Rick 😬", hl2a=[1,5], l2b="so I let the spreadsheet check it ✨", hl2b=[4,5],
  guests=G, clash=["Carol","Rick"], warn="⚠️ Conflict!", stamp="Kept apart ✓", file="Seat_and_Vow.xlsx", brand="Seat & Vow · Maker FlowTools"),
  cap="POV: you're doing the seating chart and Carol can't sit near Rick 😬\nWho's the \"Carol\" at your wedding? Tell me below 👇\nSend this to the friend who's planning a wedding 💍\nSeat & Vow (Excel): you decide who sits where, the workbook counts the seats and flags guests to keep apart.\n👉 Link in bio\n#weddingplanning #seatingchart #wedding #bride2027 #engaged #weddingtips")
R['TR03_seat_FR'] = dict(format='seatChaos', theme='seat', lang='fr', seed=43, t=dict(FR,
  l1="POV: tu fais le plan de table", l2a="et Carole ne doit pas voir Richard 😬", hl2a=[1,6], l2b="alors le classeur vérifie tout ✨", hl2b=[2,4],
  guests=G, clash=["Carole","Richard"], warn="⚠️ Conflit !", stamp="Séparés ✓", file="Seat_and_Vow.xlsx", brand="Seat & Vow · Maker FlowTools"),
  cap="POV : tu fais le plan de table et Carole ne doit pas voir Richard 😬\nC'est qui, la « Carole » de ton mariage ? Dis-le en commentaire 👇\nEnvoie ça à l'amie qui prépare son mariage 💍\nSeat & Vow (Excel) : tu décides qui s'assoit où, le classeur compte les places et signale les invités à éloigner.\n👉 Lien dans la bio\n#mariage #plandetable #mariagequébec #organisationmariage #fiancée #mariage2027")
R['TR02_landlord_FR'] = dict(format='sortChaos', theme='landlord', lang='fr', seed=52, t=dict(FR,
  l1="POV: tu gères tes loyers sur des Post-it", l2a="et tu ne sais plus qui a payé 😬", hl2a=[5,6,7], l2b="alors le classeur fait le suivi ✨", hl2b=[2,5],
  items=[it('Logement 101','1 250 $','Payé ✓','g'), it('Logement 102','600 $ / 1 100 $','Partiel','y'), it('Logement 201','1 325 $','Payé ✓','g'),
         it('Logement 202','0 $ / 980 $','Impayé','r'), it('Logement 301','1 150 $','Payé ✓','g'), it('Logement 302','1 050 $','Payé ✓','g')],
  total=dict(l='Reçu ce mois-ci', v=5375, f='cur0', c='g'), wtitle='Loyers · novembre', warn='❓ Qui a payé ?', stamp='Suivi à jour ✓',
  file='Kit_Proprietaire.xlsx', brand='Kit Propriétaire · Maker FlowTools'),
  cap="POV : tu gères tes loyers sur des Post-it et tu ne sais plus qui a payé 😬\nTon système à toi, c'est quoi ? Post-it, cahier ou Excel ? 👇\nEnvoie ça à un proprio qui en a besoin 🏠\nKit Propriétaire (Excel) : payé, partiel ou impayé pour chaque logement, chaque mois.\n👉 Lien dans la bio\n#propriétaire #immobilier #plex #québec #excel #investisseurimmobilier")
R['TR04_treasurer_EN'] = dict(format='sortChaos', theme='treasurer', lang='en', seed=61, t=dict(EN,
  l1="POV: you just became club treasurer", l2a="and nobody knows who paid 😬", hl2a=[3,4], l2b="so the spreadsheet tracks it all ✨", hl2b=[2,3],
  items=[it('Alex M.','$40','Paid ✓','g'), it('Jade L.','$20 of $40','Partial','y'), it('Sam K.','$0 of $40','Unpaid','r'),
         it('Noah P.','$40','Paid ✓','g'), it('Lea R.','$40','Paid ✓','g'), it('Omar B.','$40','Paid ✓','g')],
  total=dict(l='Dues collected', v=180, f='cur0', c='y'), wtitle='Dues · fall term', warn='❓ Who paid?', stamp='Up to date ✓',
  file='Treasurer_Kit.xlsx', brand='Treasurer Kit · Maker FlowTools'),
  cap="POV: you just became club treasurer and nobody knows who paid 😬\nTag your club's treasurer 👇\nTreasurer Kit (Excel): paid / partial / unpaid updates itself, and a reminder message is ready to copy.\n💬 Comment KIT and I'll reply with the link.\n👉 Or link in bio\n#treasurer #studentclub #studentlife #nonprofit #budget #college")
R['TR05_artisan_EN'] = dict(format='sortChaos', theme='artisan', lang='en', seed=73, t=dict(EN,
  l1="POV: it's craft fair season", l2a="and your prices are a total guess 😬", hl2a=[2,6], l2b="so the spreadsheet does the math ✨", hl2b=[2,5],
  items=[it('Soy candle','cost $17.85','$29.75','g'), it('Lavender soap','cost $6.10','$10.17','b'), it('Knit beanie','cost $21.40','$35.67','y'),
         it('Floral card','cost $3.20','$5.33','p'), it('Ceramic mug','cost $12.60','$21.00','o'), it('Tote bag','cost $9.30','$15.50','k')],
  total=dict(l='Target margin', v=40, f='pct', c='y'), wtitle='Suggested price · 40% margin', warn='❓ What do I charge?', stamp='Every cost counted ✓',
  file='Artisan_Empire_360.xlsx', brand='Artisan Empire 360° · Maker FlowTools'),
  cap="POV: it's craft fair season and your prices are a total guess 😬\nHonestly, how do you price your work? 👇\nSend this to a maker friend before their next market 🎪\nArtisan Empire 360° (Excel): materials, packaging, fees and your time, then a suggested price.\n👉 Link in bio\n#handmadebusiness #craftfair #etsyseller #maker #smallbusiness #pricing")
R['TR06_habit_EN'] = dict(format='sortChaos', theme='habit', lang='en', seed=88, t=dict(EN,
  l1="POV: your 2027 resolutions, week 2", l2a="and you already missed a day 😬", hl2a=[3,5], l2b="a gap is not a failure ✨", hl2b=[1,4],
  items=[it('Read 20 min','4 / 5 this week','Done ✓','g'), it('Walk 30 min','3 / 5 this week','Minimum','y'), it('Stretch','planned day off','Rest','b'),
         it('Drink 2 L of water','6 / 7 this week','Done ✓','g'), it('Journal','2 / 3 this week','Done ✓','g'), it('No phone in bed','4 / 7 this week','Minimum','y')],
  total=dict(l='Consistency', v=82, f='pct', c='g'), wtitle='Rhythm 2027 · this week', warn='❌ Streak broken?', stamp='No guilt ✓', emoji='😩',
  file='Rhythm_Habit_Tracker_2027.xlsx', brand='Rhythm Habit Tracker 2027 · Maker FlowTools'),
  cap="POV: your 2027 resolutions, week 2, and you already missed a day 😬\nWhich habit are you starting in 2027? 👇\nSend this to your accountability buddy 🤝\nRhythm Habit Tracker 2027 (Excel): done, minimum version or planned rest. A missed day stays blank, no guilt.\n👉 Link in bio\n#habittracker #2027goals #newyearresolution #productivity #selfimprovement #excel")
R['TR07_treasurer_FR'] = dict(format='sortChaos', theme='treasurer', lang='fr', seed=64, t=dict(FR,
  l1="POV: tu deviens trésorier de ton asso", l2a="et personne ne sait qui a payé 😬", hl2a=[5,6,7], l2b="alors le classeur suit tout ✨", hl2b=[2,4],
  items=[it('Alex M.','40 $','Payé ✓','g'), it('Jade L.','20 $ sur 40 $','Partiel','y'), it('Sam K.','0 $ sur 40 $','Impayé','r'),
         it('Noah P.','40 $','Payé ✓','g'), it('Léa R.','40 $','Payé ✓','g'), it('Omar B.','40 $','Payé ✓','g')],
  total=dict(l='Cotisations reçues', v=180, f='cur0', c='y'), wtitle="Cotisations · session d'automne", warn='❓ Qui a payé ?', stamp='À jour ✓',
  file='Kit_Tresorier.xlsx', brand='Kit Trésorier · Maker FlowTools'),
  cap="POV : tu deviens trésorier de ton asso et personne ne sait qui a payé 😬\nIdentifie le trésorier de ton comité 👇\nKit Trésorier (Excel) : payé, partiel ou impayé se met à jour seul, et un texte de rappel est prêt à copier.\n💬 Écris KIT en commentaire et je te réponds avec le lien.\n👉 Ou lien dans la bio\n#trésorier #association #clubétudiant #cégep #vieétudiante #budget")
R['TR09_landlord_EN'] = dict(format='sortChaos', theme='landlord', lang='en', seed=55, t=dict(EN,
  l1="POV: you track rent on sticky notes", l2a="and you can't remember who paid 😬", hl2a=[5,6], l2b="so the spreadsheet keeps track ✨", hl2b=[2,4],
  items=[it('Unit 101','$1,250','Paid ✓','g'), it('Unit 102','$600 of $1,100','Partial','y'), it('Unit 201','$1,325','Paid ✓','g'),
         it('Unit 202','$0 of $980','Unpaid','r'), it('Unit 301','$1,150','Paid ✓','g'), it('Unit 302','$1,050','Paid ✓','g')],
  total=dict(l='Received this month', v=5375, f='cur0', c='g'), wtitle='Rent · November', warn='❓ Who paid?', stamp='All tracked ✓',
  file='Landlord_Kit.xlsx', brand='Landlord Kit · Maker FlowTools'),
  cap="POV: you track rent on sticky notes and you can't remember who paid 😬\nWhat's your system: sticky notes, notebook or spreadsheet? 👇\nSend this to a landlord friend 🏠\nLandlord Kit (Excel): paid, partial or unpaid for every unit, every month.\n👉 Link in bio\n#landlord #rentalproperty #realestateinvesting #propertymanagement #excel #canada")
# créneau du calendrier -> reel (remplace le reel prévu ; l'original est gardé dans ig/archive/)
SLOTS = {'d08A': 'TR02_landlord_FR', 'd10A': 'TR03_seat_FR', 'd13A': 'TR04_treasurer_EN', 'd15A': 'TR05_artisan_EN',
         'd17A': 'TR06_habit_EN', 'd20A': 'TR07_treasurer_FR', 'd23A': 'TR09_landlord_EN'}
PUBLISHED = {'TR01_seat_EN': '2026-11-03 21:23 (Montréal) · https://www.instagram.com/reel/DfTX-g6jr8P/'}
if __name__ == '__main__':
    reels = []
    for rid, r in R.items():
        reels.append(dict(id=rid, engine='trend.html', format=r['format'], theme=r['theme'], lang=r['lang'], dur=9.6, loop=True, seed=r['seed'],
                          coverAt=6.2, previewTimes=[0, 1.5, 2.4, 3.8, 5.3, 6.4, 8.2, 9.55], t=r['t']))
    json.dump({'reels': reels}, open(os.path.join(here, 'trends.json'), 'w'), ensure_ascii=False, indent=1)
    json.dump({rid: r['cap'] for rid, r in R.items()}, open(os.path.join(here, 'trend_captions.json'), 'w'), ensure_ascii=False, indent=1)
    print(len(reels), 'reels tendance')
