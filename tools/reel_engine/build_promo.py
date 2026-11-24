"""Reels promo Cyber Sale -30 % (24 nov. 2026). python3 build_promo.py -> promo.json ; rendu : node render.js promo.json ../../videos/promo ids"""
import json
EN=dict(cyber='🚨 CYBER SALE',sub='EVERYTHING<br>IS <b>30% OFF</b>',bubble='WAIT… EVERYTHING?! 😱',limited='⏳ SALE ENDS DEC 2',mq='🔥 CYBER SALE  ★  30% OFF EVERYTHING  ★  ENDS DEC 2',units=['DAYS','HRS','MIN','SEC'],end='ENDS DEC 2 ⏰',days=7,cta='LINK IN BIO 👆',ctaSub='Excel tools · English + Français',
 items=[['Landlord Kit','rent · repairs · leases'],['Treasurer Kit','club budget · dues'],['Seat & Vow','wedding seating plan'],['Habit Tracker 2027','no streak pressure'],['Artisan Empire 360°','craft shop profits']])
FR=dict(cyber='🚨 CYBER SALE',sub='TOUT EST<br>À <b>-30 %</b>',bubble='ATTENDS… TOUT ?! 😱',limited='⏳ FIN DE LA PROMO : 2 DÉC.',mq='🔥 CYBER SALE  ★  -30 % SUR TOUT  ★  FIN LE 2 DÉC.',units=['JOURS','H','MIN','SEC'],end='FIN LE 2 DÉC. ⏰',days=6,cta='LIEN DANS LA BIO 👆',ctaSub='Outils Excel · Français + English',
 items=[['Kit Propriétaire','loyers · réparations · baux'],['Kit Trésorier','budget · cotisations'],['Seat & Vow','plan de table mariage'],['Habit Tracker 2027','sans pression'],['Artisan Empire 360°','profits de ton atelier']])
R=[dict(id=i,engine='promo.html',theme='pop',music='promo0' if i.endswith('EN') else 'promo1',dur=15,t=t,previewTimes=[0,.5,1.5,3.5,5,7,9,11,12.5,14.5],coverAt=1.0) for i,t in (('P1_cybersale_EN',EN),('P2_cybersale_FR',FR))]
json.dump(dict(reels=R),open('promo.json','w'),ensure_ascii=False)
