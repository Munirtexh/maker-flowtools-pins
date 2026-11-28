"""28 nov. 2026 (Yaacoub) : reel « comparaison 3 colonnes » ORIGINAL (format viral Motivation/Discipline/Obsession, autre sujet : où on garde ses tâches).
Usage : python3 build_compare.py -> compare.json, compare_captions.json ; rendu : node render.js compare.json ../../videos/compare K1_tetevspostit_FR"""
import json
R, CAP = {}, {}
R['K1_tete_postit_tableau_FR'] = dict(engine='compare.html', lang='fr', dur=20, theme='seat', music='gm:keys', coverAt=14.5, previewTimes=[1.0, 2.5, 5, 8, 11, 14.5, 16.5, 19],
  hook=[dict(t='Où tu gardes', c='#fff'), dict(t='TES TÂCHES ?', c='#ffd23d', s=96)],
  endTxt='Et toi, t’es lequel ? 👇',
  cols=[dict(title='Dans ma tête', emoji='🧠', color='#7e8bff', score=412, pow=1.5, tasks=['facture', 'rdv', 'appeler', 'rendu', 'anniv', 'loyer', 'commande'],
             bubbles=[[2.2, 4.4, 'Je m’en souviens', 0, 950, 30], [9.0, 11.2, 'C’était quoi ?', 0, 950, 32]]),
        dict(title='Sur un post-it', emoji='📝', color='#ff9ecf', score=87, pow=1.1, bubbles=[[2.6, 4.6, 'Je note ça', 0, 950, 32], [11.5, 13.5, 'Où est le bon ?', 0, 950, 30]]),
        dict(title='Dans un tableau', emoji='📊', color='#2ee6a6', score=0, bubbles=[[3.0, 5.0, 'Tout est là', 0, 950, 32]])],
  caps=[[1.6, 3.4, 'Jour 1 : tout va bien 😌', '#fff'], [3.6, 9.0, 'Les tâches s’accumulent…', '#ffd23d'], [9.7, 14.8, 'On oublie. On cherche. On stresse.', '#ff8aa0'], [15.2, 20, 'Tâches oubliées en 1 an : x412 · x87 · x0', '#fff']])
CAP['K1_tete_postit_tableau_FR'] = ("Où tu gardes tes tâches ? 🧠 📝 📊\nCommente 1, 2 ou 3 👇 (et envoie ça à celui qui oublie tout 😂)\n"
  "Pour la 3e colonne, c’est un tableau tout simple dans Excel/Sheets : un outil, pas de magie ✨\n#organisation #productivité #todolist #étudiant #entrepreneur #animation #relatable #stickman")
R['K1_head_sticky_sheet_EN'] = dict(R['K1_tete_postit_tableau_FR'], lang='en', coverAt=14.5, music='gm:uke',
  hook=[dict(t='Where do you keep', c='#fff'), dict(t='YOUR TO-DOS?', c='#ffd23d', s=96)], endTxt='Which one are you? 👇',
  cols=[dict(title='In my head', emoji='🧠', color='#7e8bff', score=412, pow=1.5, tasks=['invoice', 'meeting', 'call mom', 'deadline', 'rent', 'order', 'gift'],
             bubbles=[[2.2, 4.4, 'I’ll remember', 0, 950, 32], [9.0, 11.2, 'Wait… what?', 0, 950, 32]]),
        dict(title='On a sticky note', emoji='📝', color='#ff9ecf', score=87, pow=1.1, bubbles=[[2.6, 4.6, 'Noted it', 0, 950, 34], [11.5, 13.5, 'Which one?!', 0, 950, 32]]),
        dict(title='In a sheet', emoji='📊', color='#2ee6a6', score=0, bubbles=[[3.0, 5.0, 'All in one place', 0, 950, 28]])],
  caps=[[1.6, 3.4, 'Day 1: all good 😌', '#fff'], [3.6, 9.0, 'Tasks start piling up…', '#ffd23d'], [9.7, 14.8, 'Forget. Search. Stress.', '#ff8aa0'], [15.2, 20, 'Tasks forgotten in 1 year: x412 · x87 · x0', '#fff']])
CAP['K1_head_sticky_sheet_EN'] = ("Where do you keep your to-dos? 🧠 📝 📊\nComment 1, 2 or 3 👇 (and send this to the friend who forgets everything 😂)\n"
  "Column 3 is just a simple sheet in Excel/Google Sheets: a tool, no magic ✨\n#organization #productivity #todolist #student #smallbusiness #animation #relatable #stickman")
json.dump({'reels': [dict(id=k, **v) for k, v in R.items()]}, open('compare.json', 'w'), ensure_ascii=False, indent=1)
json.dump(CAP, open('compare_captions.json', 'w'), ensure_ascii=False, indent=1)
