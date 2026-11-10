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

PLACE = {}
if __name__ == '__main__':
    reels = [dict(r, id=k) for k, r in R.items()]
    json.dump({'reels': reels}, open(os.path.join(here, 'stories.json'), 'w'), ensure_ascii=False, indent=1)
    json.dump(CAP, open(os.path.join(here, 'stories_captions.json'), 'w'), ensure_ascii=False, indent=1)
    print(len(reels), 'stories')
