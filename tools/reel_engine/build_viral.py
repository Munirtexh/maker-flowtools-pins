"""Nouvelle stratégie (20 nov. 2026, Yaacoub) : le but = vues, likes, abonnés. Animations 100 % tendance, 15 s.
Simulations satisfaisantes (bounce.html, aucune mention du produit) + stickman (story.html, look stick).
Le produit n'apparaît qu'à la fin de certaines vidéos (X1 mariage gardé), jamais dans les vidéos « pures ».
Usage : python3 build_viral.py -> viral.json, viral_captions.json ; rendu : node render.js viral.json ../../videos/viral ids"""
import json, copy
PT = [0.2, 1.5, 3.0, 5.0, 7.5, 10.0, 12.0, 12.9, 13.6, 14.6]
R, CAP, PLACE = {}, {}, {}

R['V1_anneaux_FR'] = dict(engine='bounce.html', mode='rings', dur=15, seed=11, mel='elise', music='notes:0', theme='seat', h0=190, bg='#141a3a', previewTimes=PT, coverAt=6.0,
  hook='Elle va plus vite à chaque <em>évasion</em> 😳', finTxt='LIBRE ! 🎉', subTxt='anneaux restants')
CAP['V1_anneaux_FR'] = "Elle va plus vite à chaque évasion 😳\nTu as reconnu la musique ? 🎹👇\n#satisfaisant #satisfying #simulation #oddlysatisfying #asmr #animation"
PLACE['V1_anneaux_FR'] = 'd23B'

R['V2_grossit_EN'] = dict(engine='bounce.html', mode='grow', dur=15, seed=12, mel='joy', music='notes:10', theme='seat', h0=320, bg='#1f1235', previewTimes=PT, coverAt=8.0,
  hook='Every bounce makes it <em>bigger</em>…<br>wait for it 👀', finTxt='FULL! 🤯', subTxt='of the circle')
CAP['V2_grossit_EN'] = "Every bounce makes it bigger… wait for it 👀\nDid you guess the song? 🎶👇\n#satisfying #oddlysatisfying #simulation #bouncingball #asmr #animation"
PLACE['V2_grossit_EN'] = 'd26B'

R['V3_multiplie_FR'] = dict(engine='bounce.html', mode='multiply', dur=15, seed=13, mel='turk', music='notes:12', theme='seat', h0=40, cap=999, bg='#10233a', previewTimes=PT, coverAt=10.0,
  hook='Chaque rebond peut créer <em>une balle</em>.<br>Le cercle va tenir ? 😬', finTxt='ÇA DÉBORDE 🤯', subTxt='balles')
CAP['V3_multiplie_FR'] = "Chaque rebond peut créer une balle. Le cercle va tenir ? 😬\nTu dirais combien au moment où ça casse ? 👇\n#satisfaisant #satisfying #simulation #oddlysatisfying #asmr"
PLACE['V3_multiplie_FR'] = 'd27B'

R['V4_guerre_FR'] = dict(engine='bounce.html', mode='wars', dur=15, seed=14, speed=1500, nb=3, mel='king', music='notes:8', theme='seat', bg='#151530', previewTimes=PT, coverAt=6.0,
  hook='🩷 contre 🩵<br>Choisis ton camp <em>avant la fin</em> 👇', winTxt=['🩷 GAGNE', '🩵 GAGNE'], subTxt='cases')
CAP['V4_guerre_FR'] = "🩷 contre 🩵 : choisis ton camp avant la fin 👇\nCommente ta couleur !\n#satisfaisant #satisfying #simulation #pongwars #oddlysatisfying"
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

R['V6_stickman_episode_EN'] = dict(engine='story.html', world='binge', look='stick', theme='habit', lang='en', dur=15, music='gm:keys', seed=606,
  coverAt=10.6, endAt=15, cinema=False, previewTimes=PT, accent='#000000', a1='#ffd23d', a2='#5cc8ff',
  meme='Me at 11 PM: “just ONE episode” 📺', mhl=[5, 6], memeFs=66,
  chips=[[0.3, 2.6, 'EP 1', 140, 1500, '#ffffff'], [2.6, 3.9, 'EP 2', 140, 1500, '#ffffff'], [3.9, 5.1, 'EP 3', 140, 1500, '#ffffff'], [5.1, 6.3, 'EP 4', 140, 1500, '#ffc23d'],
         [6.3, 7.5, 'EP 5', 140, 1500, '#ffc23d'], [7.5, 8.7, 'EP 6', 140, 1500, '#ff9f43'], [8.7, 10.4, 'EP 7', 140, 1500, '#ff5d73'], [10.4, 15, 'EP 8 😵', 140, 1500, '#ff5d73']],
  bubbles=[[0.6, 2.4, 'Just one 😌', 120, 960, 44], [10.6, 12.0, 'WORK?!', 200, 1050, 54], [13.2, 15, '…ok ONE more 😌', 90, 960, 44]],
  scenes=[dict(t0=0, t1=15, set='none')])
CAP['V6_stickman_episode_EN'] = "Me at 11 PM: “just ONE episode” 📺\nWhat show did this to you? 👇\nTag the friend who does this every night 😂\n#stickman #stickmananimation #relatable #bingewatching #funnyanimation #animation"
PLACE['V6_stickman_episode_EN'] = 'd28B'

if __name__ == '__main__':
    json.dump({'reels': [dict(id=k, **v) for k, v in R.items()]}, open('viral.json', 'w'), ensure_ascii=False, indent=1)
    json.dump({k: {'caption': CAP[k], 'slot': PLACE[k]} for k in R}, open('viral_captions.json', 'w'), ensure_ascii=False, indent=1)
    print(len(R), 'reels')
