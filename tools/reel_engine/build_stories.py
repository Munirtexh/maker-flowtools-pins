"""Reels « histoire » (10 nov. 2026, demande de Yaacoub) : vraies mini-histoires animées façon clipping viral,
personnages humains différents à chaque reel (moteur story.html). On se moque du héros -> galère -> il s'organise
avec l'outil -> « X plus tard » -> réussite et réactions. Fiction assumée : aucun chiffre de vente ni résultat produit inventé.
Produit stories.json + stories_captions.json ; PLACE = créneau -> reel."""
import json, os
here = os.path.dirname(os.path.abspath(__file__))
R, CAP = {}, {}
SK = ['#f1c7a5', '#d9a47e', '#a8714f', '#7a4b31', '#f6d7bf']
PT = [0.3, 1.5, 3.2, 5.5, 8.4, 10.2, 11.5, 12.6, 14]

# 1 · EN — Le gamin de l'usine qui gère son premier duplex (Landlord Kit)
hero = dict(skin=SK[1], hair='curly', hairC='#1d140e', shirt='#ff9f43', pants='#2d3250')
R['S1_factory_landlord_EN'] = dict(engine='story.html', theme='landlord', lang='en', dur=15, music='funk', seed=201, coverAt=1.2, endAt=13.0,
  accent='#0f5a52', a1='#2ee6a6', a2='#5cc8ff', previewTimes=PT, brand='Landlord Kit · Maker FlowTools',
  end=dict(name='Landlord Kit', sub='Excel · EN / FR · no macros<br>Sample data in this video', btn='👉 Link in bio', btn2='📤 Send this to someone people doubt'),
  scenes=[
    dict(t0=0, t1=2.4, set='factory', top='Everyone at the factory laughed at him 😂', thl=[0, 5], topFs=80,
      chars=[dict(hero, x=540, y=1330, s=.86, kid=True, hat='hardhat', outfit='overalls', pose='work'),
             dict(skin=SK[0], hair='short', hairC='#6b4a2b', shirt='#5cc8ff', x=170, y=1340, s=1, hat='hardhat', pose='point', haha=[[.3, 2.4]]),
             dict(skin=SK[3], hair='none', shirt='#b18cff', x=910, y=1340, s=1, hat='hardhat', pose='pointL', haha=[[.6, 2.4]])]),
    dict(t0=2.4, t1=4.7, set='break', laptop=[380], cap='On his lunch break, he managed his first duplex 🏠', hl=[3, 4, 6, 7, 8],
      chars=[dict(hero, x=380, y=1320, s=.95, pose='type'),
             dict(skin=SK[0], hair='short', hairC='#6b4a2b', shirt='#5cc8ff', x=820, y=1330, s=1, pose='laugh', says=[[.2, 2.2, 'YOU? A landlord?! 😂']], bubFs=42)]),
    dict(t0=4.7, t1=7.1, set='night', laptop=[540], cap='Then the texts started 😵', hl=[2, 3], shake=[.4, 1.6],
      notifs=[[.15, 'Unit 2', 'Rent sent? I think…'], [.45, 'Unit 1', 'The sink is leaking 💧'], [.75, 'Unit 3', 'Can I pay half this month?'], [1.05, 'Bank', 'Deposit: $600']],
      chars=[dict(hero, x=540, y=1330, s=1, pose='stress')]),
    dict(t0=7.1, t1=9.9, set='glow', cap='So he tracked every unit, every month.', hl=[3, 4, 6, 7], capO=dict(top=1500, fs=72),
      screen=dict(file='Landlord_Kit.xlsx', sample='Sample data', title='Rent · November', top=300, step=.34,
        rows=[['Unit 1', '$1,250', 'g', 'Paid ✓'], ['Unit 2', '$600 of $1,100', 'y', 'Partial'], ['Unit 3', '$0 of $980', 'r', 'Unpaid'], ['Unit 4', '$1,150', 'g', 'Paid ✓']],
        total=['Received', 0, 3000, '$'], stamp='No more guessing')),
    dict(t0=9.9, t1=10.7, set='black', card='2 years later…', mute=[0, .75]),
    dict(t0=10.7, t1=13.0, set='city', cap='Now they ask HIM for advice 👀', hl=[3, 4], burst=.15,
      chars=[dict(hero, x=540, y=1330, s=1.05, outfit='suit', shirt='#20263f', tie='#2ee6a6', pose='proud'),
             dict(skin=SK[0], hair='short', hairC='#6b4a2b', shirt='#5cc8ff', x=170, y=1350, s=.95, hat='hardhat', pose='shock', poses=[[1.1, 'clap']], says=[[.4, 2.2, 'Teach me?? 😳']], bubFs=40),
             dict(skin=SK[3], hair='none', shirt='#b18cff', x=910, y=1350, s=.95, hat='hardhat', pose='shock', poses=[[1.3, 'clap']])]),
  ])
CAP['S1_factory_landlord_EN'] = "Everyone at the factory laughed at him 😂\nWho's the person everyone doubted in YOUR life? 👇\nSend this to someone people doubt 🏠\nLandlord Kit (Excel): paid, partial or unpaid for every unit and every month. (Animated story, sample data.)\n👉 Link in bio\n#landlord #realestateinvesting #rentalproperty #motivation #duplex #excel"

# 2 · EN — La demoiselle d'honneur à qui personne ne faisait confiance (Seat & Vow)
maid = dict(skin=SK[2], hair='bun', hairC='#2a1710', shirt='#ff7aa8', outfit='dress', pants='#7a2d55')
bride = dict(skin=SK[0], hair='long', hairC='#8a5a2b', shirt='#f7f3ff', outfit='dress', pants='#e9e2ff', hat='veil')
R['S2_maid_seat_EN'] = dict(engine='story.html', theme='seat', lang='en', dur=15, music='pop', seed=202, coverAt=1.2, endAt=13.0,
  accent='#5a1240', a1='#ff7aa8', a2='#ffd27a', previewTimes=PT, brand='Seat & Vow · Maker FlowTools',
  end=dict(name='Seat &amp; Vow', sub='Excel seating planner · EN / FR<br>Sample data in this video', btn='👉 Link in bio', btn2='📤 Tag the friend who saves every party'),
  scenes=[
    dict(t0=0, t1=2.5, set='hall', top='They gave the seating chart to the "chaotic" friend 😂', thl=[4, 5, 7, 8], topFs=76,
      chars=[dict(maid, x=540, y=1330, s=.95, pose='shock'),
             dict(skin=SK[4], hair='short', hairC='#9a9a9a', shirt='#5cc8ff', outfit='suit', tie='#ff7aa8', x=170, y=1340, s=1, pose='point', haha=[[.3, 2.5]]),
             dict(skin=SK[1], hair='long', hairC='#3a2414', shirt='#b18cff', outfit='dress', pants='#4a2f7a', x=910, y=1340, s=1, pose='pointL', haha=[[.5, 2.5]])]),
    dict(t0=2.5, t1=4.9, set='night', laptop=[540], cap='180 guests. 3 weeks. Zero plan.', hl=[0, 1, 4, 5], shake=[.5, 1.6],
      notifs=[[.15, 'Aunt Carol', 'Do NOT seat me near Karen'], [.45, 'Uncle Bob', 'Bringing +3, ok? 😅'], [.75, 'Bride 💍', 'Is table 1 done??'], [1.05, 'Caterer', 'Final count by Friday']],
      chars=[dict(maid, x=540, y=1330, s=1, pose='stress')]),
    dict(t0=4.9, t1=7.6, set='glow', cap='So she let the workbook count and check.', hl=[4, 6, 7], capO=dict(top=1500, fs=72),
      screen=dict(file='Seat_and_Vow.xlsx', sample='Sample data', title='Seating · check', top=300, step=.34,
        rows=[['Table 1', '10 / 10', 'g', 'Full ✓'], ['Table 4', 'Carol ↔ Karen', 'r', 'Keep apart'], ['Table 7', '+3 guests', 'y', '12 / 10'], ['Meals', '180', 'g', 'Counted ✓']],
        total=['Seated', 0, 180, '', ' / 180'], stamp='Every alert fixed')),
    dict(t0=7.6, t1=8.4, set='black', card='Wedding day…', cardC='#ffd27a', mute=[0, .75]),
    dict(t0=8.4, t1=10.6, set='hall', cap='Everyone found their seat. No drama. 💍', hl=[0, 4, 5, 6],
      chars=[dict(bride, x=330, y=1330, s=1, pose='cheer'), dict(maid, x=720, y=1330, s=1, pose='proud')], burst=.3),
    dict(t0=10.6, t1=13.0, set='hall', cap='Now EVERY bride wants her 👀', hl=[1, 2], 
      chars=[dict(maid, x=540, y=1330, s=1.05, pose='wave'),
             dict(skin=SK[4], hair='short', hairC='#9a9a9a', shirt='#5cc8ff', outfit='suit', tie='#ff7aa8', x=170, y=1350, s=.95, pose='shock', poses=[[1.0, 'clap']], says=[[.3, 2.2, 'Do OUR wedding?? 😳']], bubFs=40),
             dict(skin=SK[1], hair='long', hairC='#3a2414', shirt='#b18cff', outfit='dress', pants='#4a2f7a', x=910, y=1350, s=.95, pose='shock', poses=[[1.2, 'clap']])]),
  ])
CAP['S2_maid_seat_EN'] = "They gave the seating chart to the \"chaotic\" friend 😂\nWho's the friend who secretly saves every party? Tag them 👇\nSeat & Vow (Excel): you seat your guests, the workbook counts the seats and meals and flags guests to keep apart. (Animated story, sample data.)\n👉 Link in bio\n#weddingplanning #seatingchart #bridesmaid #maidofhonor #wedding2027 #weddingtips"

# 3 · FR — Le plus jeune du comité devient trésorier (Kit Trésorier)
jeune = dict(skin=SK[3], hair='short', hairC='#120c08', shirt='#2ee6a6', outfit='hoodie', pants='#28304f', hat='cap', capC='#5cc8ff')
R['S3_jeune_tresorier_FR'] = dict(engine='story.html', theme='treasurer', lang='fr', dur=15, music='funk', seed=203, coverAt=1.2, endAt=13.0,
  accent='#3a2380', a1='#ffc23d', a2='#b18cff', previewTimes=PT, brand='Kit Trésorier · Maker FlowTools',
  end=dict(name='Kit Trésorier', sub='Excel · FR / EN · sans macros<br>Données d\'exemple dans cette vidéo', btn='👉 Lien dans la bio', btn2='💬 Écris KIT en commentaire'),
  scenes=[
    dict(t0=0, t1=2.5, set='meeting', top='Le plus jeune devient trésorier. Tout le monde rit 😂', thl=[3, 6, 7], topFs=76,
      chars=[dict(jeune, x=540, y=1330, s=.9, pose='shock'),
             dict(skin=SK[0], hair='none', shirt='#20263f', outfit='suit', tie='#ffc23d', glasses=True, x=170, y=1340, s=1, pose='point', haha=[[.3, 2.5]], hahaTxt='MDR'),
             dict(skin=SK[2], hair='bun', hairC='#3a2414', shirt='#ff7aa8', x=910, y=1340, s=1, pose='pointL', haha=[[.5, 2.5]], hahaTxt='HAHA')]),
    dict(t0=2.5, t1=4.9, set='night', laptop=[540], cap='L\'AG est dans 3 jours. La banque ne balance pas.', hl=[1, 5, 6, 9], shake=[.6, 1.7],
      notifs=[[.15, 'Présidente', 'On a combien exactement ?'], [.45, 'Banque', 'Solde : 2 310,00 $'], [.75, 'Toi (livres)', 'Total : 2 185,00 $ 😳'], [1.05, 'Comité', 'Le rapport est prêt ?']],
      chars=[dict(jeune, x=540, y=1330, s=1, pose='stress')]),
    dict(t0=4.9, t1=7.6, set='glow', cap='Alors il a fait la conciliation, ligne par ligne.', hl=[4, 6, 7, 8], capO=dict(top=1500, fs=70),
      screen=dict(file='Kit_Tresorier.xlsx', sample='Données d\'exemple', title='Conciliation · octobre', top=300, step=.34,
        rows=[['Solde banque', '2 310,00 $', 'b', 'Relevé'], ['Livres', '2 185,00 $', 'y', 'À vérifier'], ['Chèque non encaissé', '125,00 $', 'g', 'Trouvé ✓'], ['Cotisations', '18 / 22', 'y', '4 en retard']],
        total=['Écart', 125, 0, '', ' $', 2], stamp='Écart : 0,00 $')),
    dict(t0=7.6, t1=8.4, set='black', card='Le jour de l\'AG…', cardC='#ffc23d', mute=[0, .75]),
    dict(t0=8.4, t1=10.6, set='meeting', cap='Rapport imprimé. Chaque dollar expliqué.', hl=[0, 1, 2, 3],
      chars=[dict(jeune, x=540, y=1330, s=1, outfit='suit', shirt='#2b2f55', tie='#ffc23d', hat=None, pose='talk', rprop='📄')]),
    dict(t0=10.6, t1=13.0, set='meeting', cap='Personne ne rit maintenant 👀', hl=[0, 2], burst=.2,
      chars=[dict(jeune, x=540, y=1330, s=1.05, outfit='suit', shirt='#2b2f55', tie='#ffc23d', pose='proud'),
             dict(skin=SK[0], hair='none', shirt='#20263f', outfit='suit', tie='#ffc23d', glasses=True, x=170, y=1350, s=.95, pose='shock', poses=[[1.0, 'clap']], says=[[.3, 2.2, 'Tu restes l\'an prochain ?? 😳']], bubFs=38),
             dict(skin=SK[2], hair='bun', hairC='#3a2414', shirt='#ff7aa8', x=910, y=1350, s=.95, pose='shock', poses=[[1.2, 'clap']])]),
  ])
CAP['S3_jeune_tresorier_FR'] = "Le plus jeune du comité devient trésorier. Tout le monde rit 😂\nIdentifie le trésorier de ton asso 👇\nKit Trésorier (Excel) : la conciliation compare la banque et les livres et t'aide à ramener l'écart à 0,00 $, puis le rapport s'imprime. (Histoire animée, données d'exemple.)\n💬 Écris KIT en commentaire et je te réponds avec le lien.\n👉 Ou lien dans la bio\n#trésorier #association #clubétudiant #cégep #comité #budget"

# 4 · EN — Ses boucles d'oreilles « c'est juste un hobby » (Artisan Empire 360°)
maker = dict(skin=SK[4], hair='long', hairC='#c7541f', shirt='#5cc8ff', outfit='apron', pants='#2d3250', glasses=True)
R['S4_hobby_artisan_EN'] = dict(engine='story.html', theme='artisan', lang='en', dur=15, music='tropical', seed=204, coverAt=1.2, endAt=13.0,
  accent='#6a2a10', a1='#ffb347', a2='#ffd700', previewTimes=PT, brand='Artisan Empire 360° · Maker FlowTools',
  end=dict(name='Artisan Empire 360°', sub='Excel · EN / FR · no macros<br>Sample data in this video', btn='👉 Link in bio', btn2='📤 Send this to a maker friend'),
  scenes=[
    dict(t0=0, t1=2.5, set='market', top='Her family called it "just a hobby" 🙄', thl=[4, 5, 6], topFs=84,
      chars=[dict(maker, x=540, y=1330, s=.95, pose='sad'),
             dict(skin=SK[1], hair='short', hairC='#222', shirt='#2ee6a6', x=170, y=1340, s=1, pose='laugh', haha=[[.3, 2.5]], says=[[.4, 2.3, '$8? Cute hobby 😂']], bubFs=40),
             dict(skin=SK[0], hair='curly', hairC='#a8a8a8', shirt='#ff9f43', outfit='dress', pants='#7a3d1d', x=910, y=1340, s=1, pose='pointL', haha=[[.6, 2.5]])]),
    dict(t0=2.5, t1=4.9, set='night', laptop=[540], cap='She sold 40 pairs… and lost money on every one 😳', hl=[1, 2, 5, 6, 7, 8], shake=[.6, 1.6],
      notifs=[[.15, 'Supplier', 'Silver hooks: price up 20%'], [.45, 'Etsy', 'Fees this month: $66'], [.75, 'Post office', 'Shipping: $4.80'], [1.05, 'You', 'Wait… did I make anything?']],
      chars=[dict(maker, x=540, y=1330, s=1, pose='stress')]),
    dict(t0=4.9, t1=7.6, set='glow', cap='So she counted EVERYTHING. Even her time.', hl=[3, 5, 6], capO=dict(top=1500, fs=72),
      screen=dict(file='Artisan_Empire_360.xlsx', sample='Sample data', title='Earrings · real cost', top=300, step=.34,
        rows=[['Materials', '$4.10', 'b', 'Beads + hooks'], ['Packaging', '$1.20', 'b', 'Box + card'], ['Fees', '$1.65', 'y', 'Etsy'], ['Your time', '$7.50', 'k', '30 min']],
        total=['Suggested price', 8, 24, '$', '', 2], stamp='Real cost: $14.45')),
    dict(t0=7.6, t1=8.4, set='black', card='Next market…', cardC='#ffb347', mute=[0, .75]),
    dict(t0=8.4, t1=10.6, set='market', cap='New price. Same earrings. Real profit. ✨', hl=[0, 1, 4, 5],
      chars=[dict(maker, x=540, y=1330, s=1, pose='proud', rprop='💸'),
             dict(skin=SK[3], hair='bun', hairC='#111', shirt='#b18cff', x=220, y=1340, s=.9, pose='wave'), dict(skin=SK[2], hair='short', hairC='#2a1a10', shirt='#ff7aa8', x=860, y=1340, s=.9, pose='talk')]),
    dict(t0=10.6, t1=13.0, set='market', cap='"Just a hobby," they said 👀', hl=[1, 2, 3], burst=.2,
      chars=[dict(maker, x=540, y=1330, s=1.05, pose='cheer'),
             dict(skin=SK[1], hair='short', hairC='#222', shirt='#2ee6a6', x=170, y=1350, s=.95, pose='shock', poses=[[1.0, 'clap']], says=[[.3, 2.2, 'Can you teach me?? 😳']], bubFs=38),
             dict(skin=SK[0], hair='curly', hairC='#a8a8a8', shirt='#ff9f43', outfit='dress', pants='#7a3d1d', x=910, y=1350, s=.95, pose='shock', poses=[[1.2, 'clap']])]),
  ])
CAP['S4_hobby_artisan_EN'] = "Her family called it \"just a hobby\" 🙄\nMakers: what's the one cost you always forget to count? 👇\nSend this to a maker friend before their next market 🎪\nArtisan Empire 360° (Excel): materials, packaging, fees and your time, then a suggested price. (Animated story, sample data.)\n👉 Link in bio\n#handmadebusiness #craftfair #etsyseller #smallbusiness #handmadejewelry #pricing"

# 5 · FR — Tout le monde abandonne ses résolutions… sauf elle (Rhythm Habit Tracker 2027)
coure = dict(skin=SK[1], hair='bun', hairC='#1b120c', shirt='#4dffb5', outfit='hoodie', pants='#22304a')
R['S5_resolution_habit_FR'] = dict(engine='story.html', theme='habit', lang='fr', dur=15, music='future', seed=205, coverAt=1.2, endAt=13.0,
  accent='#0b4a33', a1='#4dffb5', a2='#ffd166', previewTimes=PT, brand='Rhythm Habit Tracker 2027 · Maker FlowTools',
  end=dict(name='Rhythm Habit Tracker 2027', sub='Excel · FR / EN · sans macros<br>Données d\'exemple dans cette vidéo', btn='👉 Lien dans la bio', btn2='📤 Envoie ça à ton partenaire de motivation'),
  scenes=[
    dict(t0=0, t1=2.5, set='city', top='« Tes résolutions ? Tu lâches le 15 janvier 😂 »', thl=[1, 5, 6], topFs=78,
      chars=[dict(coure, x=540, y=1330, s=.95, pose='sad'),
             dict(skin=SK[0], hair='curly', hairC='#6b3a1b', shirt='#ff7aa8', x=170, y=1340, s=1, pose='point', haha=[[.3, 2.5]], hahaTxt='MDR'),
             dict(skin=SK[3], hair='short', hairC='#111', shirt='#5cc8ff', hat='cap', capC='#ffc23d', x=910, y=1340, s=1, pose='pointL', haha=[[.5, 2.5]])]),
    dict(t0=2.5, t1=4.9, set='night', laptop=[540], cap='15 janvier. Elle manque un jour. 😩', hl=[0, 1, 3, 4, 5], mute=[.7, 1.3],
      notifs=[[.15, 'Rappel', 'Course : 0 / 1 aujourd\'hui'], [.5, 'Ami', 'Alors, déjà fini ? 😏'], [.85, 'Toi', 'J\'ai tout raté…']],
      chars=[dict(coure, x=540, y=1330, s=1, pose='sad')]),
    dict(t0=4.9, t1=7.6, set='glow', cap='Mais un jour manqué reste juste… vide. Pas un échec.', hl=[3, 6, 8, 9], capO=dict(top=1500, fs=68),
      screen=dict(file='Rhythm_Habit_Tracker_2027.xlsx', sample='Données d\'exemple', title='Janvier · course', top=300, step=.34,
        rows=[['14 janv.', 'Fait', 'g', '✓'], ['15 janv.', '—', '#8f9bc0', 'vide'], ['16 janv.', 'Version minimale', 'y', '10 min'], ['17 janv.', 'Repos prévu', 'b', 'OK']],
        total=['Janvier', 0, 27, '', ' / 31 jours'], stamp='On continue')),
    dict(t0=7.6, t1=8.4, set='black', card='31 décembre…', cardC='#4dffb5', mute=[0, .75]),
    dict(t0=8.4, t1=10.6, set='city', cap='Elle n\'a jamais tout abandonné. 💪', hl=[2, 3, 4, 5],
      chars=[dict(coure, x=540, y=1330, s=1, pose='cheer', rprop='🏅')], burst=.3),
    dict(t0=10.6, t1=13.0, set='city', cap='Et maintenant, ils lui demandent comment 👀', hl=[3, 4, 5, 6],
      chars=[dict(coure, x=540, y=1330, s=1.05, pose='proud', rprop='🏅'),
             dict(skin=SK[0], hair='curly', hairC='#6b3a1b', shirt='#ff7aa8', x=170, y=1350, s=.95, pose='shock', poses=[[1.0, 'clap']], says=[[.3, 2.2, 'Tu fais comment ?? 😳']], bubFs=40),
             dict(skin=SK[3], hair='short', hairC='#111', shirt='#5cc8ff', hat='cap', capC='#ffc23d', x=910, y=1350, s=.95, pose='shock', poses=[[1.2, 'clap']])]),
  ])
CAP['S5_resolution_habit_FR'] = "« Tes résolutions ? Tu lâches le 15 janvier 😂 »\nEt toi, ta dernière résolution a duré combien de temps ? 👇\nEnvoie ça à ton partenaire de motivation 🤝\nRhythm Habit Tracker 2027 (Excel) : fait, version minimale ou repos prévu. Un jour manqué reste vide, sans culpabilité. (Histoire animée, données d'exemple.)\n👉 Lien dans la bio\n#habitudes #résolutions2027 #motivation #objectifs2027 #productivité #excel"

PLACE = {}
if __name__ == '__main__':
    reels = [dict(r, id=k) for k, r in R.items()]
    json.dump({'reels': reels}, open(os.path.join(here, 'stories.json'), 'w'), ensure_ascii=False, indent=1)
    json.dump(CAP, open(os.path.join(here, 'stories_captions.json'), 'w'), ensure_ascii=False, indent=1)
    print(len(reels), 'stories')
