"""28 nov. 2026 (idée de Yaacoub) : course Motivation / Discipline / Obsession (feu). Musique funk originale (funk_music.py, drop = 14 s = 3e relèvement).
Usage : python3 build_race.py -> race.json, race_captions.json ; node render.js race.json ../../videos/race R1_course_FR --preview"""
import json
R, CAP = {}, {}
base = dict(engine='race.html', dur=27, theme='seat', music='funk:14', coverAt=20.5, previewTimes=[1, 4, 6.5, 9, 13, 15, 18, 21.5, 23.5, 25.5])
R['R1_course_FR'] = dict(base, hook=[dict(t='365 jours de course.', c='#fff'), dict(t='QUI GAGNE ?', c='#ffd23d', s=96)], day='JOUR', unit='m', names=['Motivation', 'Discipline', 'Obsession'],
  bubbles=[[[6.4, 9.0, 'Je commence lundi', 34]], [], [[3.6, 4.8, 'Aïe…', 36], [9.0, 10.6, 'Encore…', 36], [14.2, 16.0, 'PLUS RIEN NE M’ARRÊTE', 30]]],
  caps=[[.8, 3.0, 'Départ : tous motivés 😤', '#fff'], [3.2, 6.0, 'La Motivation fonce…', '#ff7ab8'], [6.2, 11.0, 'puis s’assoit. L’Obsession tombe.', '#ffd23d'], [11.2, 14.0, 'Elle tombe encore. Et encore.', '#ff8a8a'], [14.2, 22.0, 'Mais elle se relève… en feu 🔥', '#ffb02e']],
  winTxt='L’OBSESSION GAGNE 🔥', endTxt='Et toi, t’es lequel ? 👇')
R['R1_course_EN'] = dict(base, hook=[dict(t='365 days. One race.', c='#fff'), dict(t='WHO WINS?', c='#ffd23d', s=96)], day='DAY', unit='m', names=['Motivation', 'Discipline', 'Obsession'],
  bubbles=[[[6.4, 9.0, 'I’ll start Monday', 34]], [], [[3.6, 4.8, 'Ouch…', 36], [9.0, 10.6, 'Again…', 36], [14.2, 16.0, 'NOTHING STOPS ME', 30]]],
  caps=[[.8, 3.0, 'Start: everyone’s motivated 😤', '#fff'], [3.2, 6.0, 'Motivation sprints off…', '#ff7ab8'], [6.2, 11.0, 'then sits down. Obsession falls.', '#ffd23d'], [11.2, 14.0, 'It falls again. And again.', '#ff8a8a'], [14.2, 22.0, 'But it gets up… on fire 🔥', '#ffb02e']],
  winTxt='OBSESSION WINS 🔥', endTxt='Which one are you? 👇')
CAP['R1_course_FR'] = "365 jours de course : Motivation, Discipline ou Obsession ? 🔥\nCommente ton camp 👇 et envoie ça à celui qui a besoin de se relever aujourd’hui 💪\nBesoin d’un coup de main pour t’organiser ? Un simple tableau Excel/Sheets peut aider ✨\n#motivation #discipline #obsession #mindset #stickman #animation #productivité #relatable"
CAP['R1_course_EN'] = "365 days of racing: Motivation, Discipline or Obsession? 🔥\nComment your side 👇 and send this to someone who needs to get back up today 💪\nNeed help staying organized? A simple Excel/Sheets tracker can help ✨\n#motivation #discipline #obsession #mindset #stickman #animation #productivity #relatable"
json.dump({'reels': [dict(id=k, **v) for k, v in R.items()]}, open('race.json', 'w'), ensure_ascii=False, indent=1)
json.dump(CAP, open('race_captions.json', 'w'), ensure_ascii=False, indent=1)
