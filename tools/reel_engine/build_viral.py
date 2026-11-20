"""Nouvelle stratégie (20 nov. 2026, Yaacoub) : le but = vues, likes, abonnés. Animations 100 % tendance, 15 s.
Simulations satisfaisantes (bounce.html, aucune mention du produit) + stickman (story.html, look stick).
Le produit n'apparaît qu'à la fin de certaines vidéos (X1 mariage gardé), jamais dans les vidéos « pures ».
Usage : python3 build_viral.py -> viral.json, viral_captions.json ; rendu : node render.js viral.json ../../videos/viral ids"""
import json, copy
PT = [0.2, 1.5, 3.0, 5.0, 7.5, 10.0, 12.0, 12.9, 13.6, 14.6]
PT30 = [0.2, 3, 8, 14, 20, 25, 26.5, 27.5, 29.5]
R, CAP, PLACE = {}, {}, {}

R['V1_anneaux_FR'] = dict(engine='bounce.html', mode='rings', dur=30, finAt=26.8, rings=12, maxGap=3.4, seed=11, mel='elise', music='notes:0', theme='seat', h0=190, bg='#141a3a', previewTimes=PT, coverAt=6.0,
  hook='Moi qui essaie d\'encaisser<br><em>les 12 loyers</em> du mois 😮‍💨', finTxt='TOUT PAYÉ ! 🎉', subTxt='loyers encaissés', ballEmoji='💵', cntUp=True)
CAP['V1_anneaux_FR'] = "Moi qui essaie d'encaisser les 12 loyers du mois 😮‍💨\nProprios : il vous reste combien de loyers à encaisser ? 👇 (et tu as reconnu la musique ? 🎹)\n#propriétaire #immobilier #plex #satisfaisant #satisfying #simulation #oddlysatisfying #asmr #animation"
PLACE['V1_anneaux_FR'] = 'd23B'

R['V2_grossit_EN'] = dict(engine='bounce.html', mode='grow', dur=30, finAt=26.8, seed=12, mel='joy', music='notes:10', theme='seat', h0=320, bg='#1f1235', previewTimes=PT, coverAt=8.0,
  hook='Our wedding guest list after<br><em>every family dinner</em> 🙃', finTxt='VENUE FULL! 🤯', subTxt='guests', ballTxt='GUEST LIST', growCount=[40, 220])
CAP['V2_grossit_EN'] = "Our wedding guest list after every family dinner 🙃\nHow many guests did YOUR list start with? 👇 (and did you guess the song? 🎶)\nTag your other half 💍\n#weddingplanning #guestlist #engaged #wedding2027 #satisfying #oddlysatisfying #simulation #bouncingball #asmr #animation"
PLACE['V2_grossit_EN'] = 'd26B'

R['V3_multiplie_FR'] = dict(engine='bounce.html', mode='multiply', dur=30, finAt=26.6, seed=13, mel='turk', music='notes:12', theme='seat', h0=40, cap=999, bg='#10233a', previewTimes=PT, coverAt=10.0,
  hook='Mes commandes avant le <em>marché de Noël</em> 🎄<br>Je vais tenir ? 😬', finTxt='DÉBORDÉE 🤯', subTxt='commandes')
CAP['V3_multiplie_FR'] = "Mes commandes avant le marché de Noël 🎄 Je vais tenir ? 😬\nArtisans : vous en êtes à combien de commandes ? 👇\n#artisan #faitmain #marchédenoël #petitecommerce #satisfaisant #satisfying #simulation #oddlysatisfying #asmr"
PLACE['V3_multiplie_FR'] = 'd27B'

R['V4_guerre_FR'] = dict(engine='bounce.html', mode='wars', dur=30, finAt=27.0, seed=14, speed=1500, nb=3, mel='king', music='notes:8', theme='seat', bg='#151530', previewTimes=PT, coverAt=6.0,
  hook='Cotisations du club :<br>🩷 payé contre 🩵 <em>pas payé</em> 👇', winTxt=['PAYÉ GAGNE 🎉', 'PAS PAYÉ GAGNE 😭'], subTxt='🩷 payé · 🩵 pas payé')
CAP['V4_guerre_FR'] = "Cotisations du club : 🩷 payé contre 🩵 pas payé 👇\nTrésoriers, dans votre club, qui gagne ? Commente ta couleur !\n#trésorier #association #clubétudiant #cotisations #satisfaisant #satisfying #simulation #pongwars #oddlysatisfying"
PLACE['V4_guerre_FR'] = 'd29B'

# ---- Stickman (fond noir) : gags 100 % animation, aucune mention du produit ----
import build_styles as BS
x4 = copy.deepcopy(BS.R['X4_stickman_habit_EN'])
x4.update(endAt=15, brand=None, previewTimes=PT, coverAt=4.4,
  chips=[[0.4, 3.5, 'DAY 1', 470, 380, '#ffffff'], [3.5, 5.6, 'DAY 4', 470, 380, '#ff5d73'], [5.6, 7.1, 'DAY 12', 450, 380, '#ff5d73'], [7.1, 8.6, 'DAY 20', 450, 380, '#ff5d73'], [9.0, 15, 'DAY 31', 450, 380, '#2ee6a6']],
  scenes=[dict(t0=0, t1=3.5, set='none'), dict(t0=3.5, t1=8.6, set='none', shake=[.05, .4]), dict(t0=8.6, t1=10.8, set='none'),
          dict(t0=10.8, t1=15, set='none', cap='Small beats perfect. 🏁', hl=[0, 2], capO=dict(top=1500, fs=84))])
x4.pop('end', None); x4.pop('brand', None)
R['V5_stickman_habitudes_EN'] = x4
CAP['V5_stickman_habitudes_EN'] = "10 new habits on Jan 1 vs. 1 tiny habit a day 🏁\nBe honest: which one are you? 👇\nTag your 2027 buddy 🤝\n#stickman #stickmananimation #animation #newyearsresolutions #2027goals #relatable"
PLACE['V5_stickman_habitudes_EN'] = 'd24B'

R['V6_stickman_episode_EN'] = dict(ep='Stickman · Ep. 1', engine='story.html', world='binge', look='stick', theme='habit', lang='en', dur=15, music='gm:keys', seed=606,
  coverAt=10.6, endAt=15, cinema=False, previewTimes=PT, accent='#000000', a1='#ffd23d', a2='#5cc8ff',
  meme='Me at 11 PM: “just ONE episode” 📺', mhl=[5, 6], memeFs=66,
  chips=[[0.3, 2.6, 'EP 1', 140, 1500, '#ffffff'], [2.6, 3.9, 'EP 2', 140, 1500, '#ffffff'], [3.9, 5.1, 'EP 3', 140, 1500, '#ffffff'], [5.1, 6.3, 'EP 4', 140, 1500, '#ffc23d'],
         [6.3, 7.5, 'EP 5', 140, 1500, '#ffc23d'], [7.5, 8.7, 'EP 6', 140, 1500, '#ff9f43'], [8.7, 10.4, 'EP 7', 140, 1500, '#ff5d73'], [10.4, 13.0, 'EP 8 😵', 140, 1500, '#ff5d73'], [13.0, 15, 'New habit: sleep by 11 PM… Day 1 ❌', 90, 1500, '#ff5d73']],
  bubbles=[[0.6, 2.4, 'Just one 😌', 120, 960, 44], [10.6, 12.0, 'WORK?!', 200, 1050, 54], [13.2, 15, '…ok ONE more 😌', 90, 960, 44]],
  memeSub=None,
  scenes=[dict(t0=0, t1=15, set='none')])
CAP['V6_stickman_episode_EN'] = "Me at 11 PM: “just ONE episode” 📺\nNew habit: sleep by 11 PM… Day 1 ❌\nWhat show did this to you? 👇\nTag the friend who does this every night 😂\n#stickman #stickmananimation #relatable #bingewatching #funnyanimation #animation"
PLACE['V6_stickman_episode_EN'] = 'd28B'

R['V7_stickman_snooze_FR'] = dict(ep='Stickman · Ép. 2', engine='story.html', world='snooze', look='stick', theme='habit', lang='fr', dur=15, music='gm:uke', seed=707,
  coverAt=10.0, endAt=15, cinema=False, previewTimes=PT, accent='#000000', a1='#ffd23d', a2='#5cc8ff',
  meme='Moi hier soir : « demain, gym à 6 h » 💪', mhl=[5, 6, 7], memeFs=66,
  chips=[[2.0, 3.6, 'SNOOZE ×1', 120, 1500, '#ffffff'], [3.6, 5.2, 'SNOOZE ×2', 120, 1500, '#ffffff'], [5.2, 6.8, 'SNOOZE ×3', 120, 1500, '#ffc23d'],
         [6.8, 8.4, 'SNOOZE ×4', 120, 1500, '#ff9f43'], [8.4, 9.8, 'SNOOZE ×5 😴', 120, 1500, '#ff5d73'], [12.6, 15, 'Nouvelle habitude : jour 1 ❌', 90, 1500, '#ff5d73']],
  bubbles=[[0.4, 1.8, 'Facile 😎', 140, 960, 44], [2.5, 3.4, '5 min…', 300, 960, 40], [10.0, 11.6, 'QUOI ?!', 220, 1000, 56]],
  scenes=[dict(t0=0, t1=15, set='none')])
CAP['V7_stickman_snooze_FR'] = "Moi hier soir : « demain, gym à 6 h » 💪\\nÉpisode 2 de ses mauvaises habitudes 😂 Tu as appuyé combien de fois sur snooze ce matin ? 👇\\nIdentifie ton/ta partenaire de gym 🏋️\\n#stickman #animation #snooze #gym #relatable #humour"
PLACE['V7_stickman_snooze_FR'] = 'd25C'

# ---- Versions « pures » 30 s (aucun produit, juste pour les vues) : posts en plus à 16 h 30 (sam., dim., jeu., ven.) ----
PURE = {
 'A1_anneaux_pur': ('V1_anneaux_FR', dict(seed=21, mel='canon', hook='Elle va plus vite à chaque <em>évasion</em>.<br>Reste jusqu\'à la fin 😳', finTxt='LIBRE ! 🎉', subTxt='anneaux restants', ballEmoji=None, cntUp=False),
   "Elle va plus vite à chaque évasion… reste jusqu'à la fin 😳\nTu as reconnu la musique ? 🎹👇\n#satisfaisant #satisfying #simulation #oddlysatisfying #asmr #animation", 'd23C'),
 'A2_grossit_pur': ('V2_grossit_EN', dict(seed=22, mel='elise', hook='Every bounce makes it <em>bigger</em>…<br>wait for it 👀', finTxt='FULL! 🤯', subTxt='of the circle', ballTxt=None, growCount=None),
   "Every bounce makes it bigger… wait for it 👀\nDid you guess the song? 🎶👇\n#satisfying #oddlysatisfying #simulation #bouncingball #asmr #animation", 'd24C'),
 'A3_multiplie_pur': ('V3_multiplie_FR', dict(seed=23, mel='joy', hook='Chaque rebond peut créer <em>une balle</em>.<br>Le cercle va tenir ? 😬', finTxt='ÇA DÉBORDE 🤯', subTxt='balles'),
   "Chaque rebond peut créer une balle. Le cercle va tenir ? 😬\nTu dirais combien au moment où ça casse ? 👇\n#satisfying #simulation #oddlysatisfying #asmr #animation", 'd28C'),
 'A4_guerre_pur': ('V4_guerre_FR', dict(seed=24, mel='turk', hook='🩷 contre 🩵<br>Choisis ton camp <em>avant la fin</em> 👇', winTxt=['🩷 GAGNE', '🩵 GAGNE'], subTxt='cases'),
   "🩷 contre 🩵 : choisis ton camp avant la fin 👇\nCommente ta couleur !\n#satisfying #simulation #pongwars #oddlysatisfying #asmr", 'd29C'),
}
for k, (base, upd, cap, slot) in PURE.items():
    r = copy.deepcopy(R[base]); r.update(upd); r = {a: b for a, b in r.items() if b is not None}; R[k] = r; CAP[k] = cap; PLACE[k] = slot
for k in R:
    if R[k].get('dur') == 30: R[k]['previewTimes'] = PT30; R[k]['coverAt'] = 8.0

if __name__ == '__main__':
    json.dump({'reels': [dict(id=k, **v) for k, v in R.items()]}, open('viral.json', 'w'), ensure_ascii=False, indent=1)
    json.dump({k: {'caption': CAP[k], 'slot': PLACE[k]} for k in R}, open('viral_captions.json', 'w'), ensure_ascii=False, indent=1)
    print(len(R), 'reels')
