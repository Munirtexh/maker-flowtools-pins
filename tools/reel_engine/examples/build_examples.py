"""3 exemples de reels améliorés (15 s, hook / body / fin, musique accrocheuse). PAS au calendrier : en attente d'approbation de Yaacoub."""
import json, os, sys
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.dirname(here))
import build_trends as B
NB = ' '
base = {r['id']: r for r in json.load(open(os.path.join(os.path.dirname(here), 'reels.json')))['reels']}
out = []
# A : refonte d'un reel animé existant (T2 conciliation, FR, prévu le 2 déc.)
a = dict(base['T2_FR']); a.update(id='EXA_tresorier_FR', trend=True, dur=15, music='lofi', callout='Trésoriers 👀', emoji='😳',
  hook=f'La banque dit 1{NB}842{NB}$, tes livres 1{NB}597{NB}$', hl=[3, 6], coverAt=7.5,
  previewTimes=[0, 0.8, 1.7, 2.6, 4, 6, 8.5, 11, 12.6, 14.2])
a['floats'] = list(a['floats']) + [dict(t=5.6, text="Prêt pour l'AG 📋", x=90, y=1480, c='y', rot=-6), dict(t=7.2, text='Rapport à imprimer 🖨️', x=70, y=640, c='b', rot=-5)]
a['cta'] = dict(a['cta']); a['cta']['btns'] = ['👉 Lien dans la bio', '💬 Écris KIT en commentaire']
out.append(a)
# B : reconstruction d'une vidéo P4 (fond blanc) -> Kit Propriétaire EN, prévu le 17 nov.
items = B.R['TR09_landlord_EN']['t']['items']
out.append(dict(id='EXB_landlord_EN', engine='trend.html', format='sortChaos', theme='landlord', lang='en', dur=15, music='funk', seed=57, coverAt=6.5,
  previewTimes=[0, 0.8, 1.7, 2.6, 4, 6, 8, 9.6, 11, 12.6, 14.2],
  end=dict(name='Landlord Kit', sub='Excel · English / Français · no macros', btn='👉 Link in bio', btn2='📤 Send to a landlord friend'),
  t=dict(B.EN, l1='Landlords, be honest 👀', l2a="$980 is missing and you don't know who 😬", hl2a=[0, 2],
         l2b='so the spreadsheet shows it at a glance ✨', hl2b=[2, 6], items=items,
         total=dict(l='Received this month', v=5375, f='cur0', c='g'), wtitle='Rent · November', warn='❓ Who paid?', stamp='Found it ✓',
         beats=[dict(text='Unit 202 · $980 unpaid 🔴', c='r', x=60, y=640, rot=-6), dict(text='Paid · partial · unpaid ✓', c='g', x=400, y=1560, rot=5),
                dict(text='Every unit, every month 📅', c='b', x=110, y=1090, rot=-4)],
         file='Landlord_Kit.xlsx', brand='Landlord Kit · Maker FlowTools')))
# C : reconstruction d'une vidéo Seat & Vow (fond clair) -> FR, prévu le 20 nov.
out.append(dict(id='EXC_seat_FR', engine='trend.html', format='seatChaos', theme='seat', lang='fr', dur=15, music='pop', seed=47, coverAt=6.5,
  previewTimes=[0, 0.8, 1.7, 2.6, 4, 6, 8, 9.6, 11, 12.6, 14.2],
  end=dict(name='Seat &amp; Vow', sub='Plan de table de mariage<br>Excel · FR / EN', btn='👉 Lien dans la bio', btn2='📤 Envoie-le à ta témoin'),
  t=dict(B.FR, l1="POV: ta mère t'envoie SA liste d'invités", l2a='et tes deux ex sont invités 😬', hl2a=[2, 3],
         l2b='alors le classeur me prévient ✨', hl2b=[2, 4], guests=B.G, clash=['Jérémy', 'Kevin'], warn='⚠️ Conflit !', stamp='Séparés ✓',
         beats=[dict(text='🍽️ Repas comptés pour le traiteur', c='y', x=50, y=600, rot=-5), dict(text='🪧 Cartes de table à imprimer', c='b', x=330, y=1600, rot=5),
                dict(text='🇨🇦 FR / EN en une case', c='p', x=150, y=1110, rot=-4)],
         file='Seat_and_Vow.xlsx', brand='Seat & Vow · Maker FlowTools')))
json.dump({'reels': out}, open(os.path.join(here, 'examples.json'), 'w'), ensure_ascii=False, indent=1)
print([r['id'] for r in out])
