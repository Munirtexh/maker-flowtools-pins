# Maker FlowTools · règles pour toute session qui travaille dans ce dépôt

## Reels Instagram : animations seulement (règle de Yaacoub, 1er nov. 2026)
- Tout reel doit être une animation très vivante : éléments qui « pop » et sortent, couleurs fortes, mouvement continu, fond foncé (jamais de blanc), grosse accroche, tableau de bord incliné et animé.
- **Jamais de diaporama d'images en reel.** Une image fixe se publie en post `image` dans `ig/manifest.json`.
- Fabriquer les reels avec `tools/reel_engine` (voir son README) et vérifier des aperçus (`--preview`) avant de les mettre au calendrier.
- Données d'exemple seulement, jamais assez du produit pour le copier ; musique douce sans « boum boum » ; Yaacoub n'apparaît jamais ; aucun rabais ni résultat inventé.

## Calendrier
- Avant de modifier `ig/manifest.json`, copier l'original dans `ig/archive/` (aucune publication prévue jusqu'au 31 déc. ne doit disparaître).
- Alternance un jour FR / un jour EN (31 oct = FR, 1er nov = EN), légende dans la langue du post.

## Reels tendance (4 nov. 2026)
- 2 à 3 par semaine, dans des créneaux reels existants (on remplace, on n'ajoute pas). Moteur `tools/reel_engine/trend.html`, configs `build_trends.py` (voir README du moteur).
- Changer de format régulièrement (nouvelle recherche de tendances chaque semaine) ; ne jamais montrer une fonction que le produit n'a pas (ex. Seat & Vow ne place pas les invités tout seul : il compte et alerte).

## 2e reel quotidien à 19 h 30 (4 nov. 2026, décision de Yaacoub)
- Les posts image de 19 h 30 sont remplacés par des reels 15 s (hook / body / fin) : `tools/reel_engine/build_daily.py` (configs + `EVENING` date → reel), rendu dans `videos/daily/`, puis `apply_daily.py` (archive auto dans `ig/archive/*_avant_reels_19h30_*`).
- Le reel de 19 h 30 est dans la langue opposée à celle du jour (chaque langue chaque jour). Une image n'est remplacée que quand son reel est prêt ; sinon elle reste au calendrier.
- Musique : `music.py` (5 styles générés, libres de droits), à varier d'un jour à l'autre.

## Série « duo » (8 nov. 2026, après le 1er reel à 1,3K vues)
- Recette gagnante : 2 personnages (blobs), conflit qui monte avec un compteur, gel + silence, l'ordi règle ça, fin heureuse, puce « épisode ». Format `couple` de `trend.html` (paramétrable), configs `build_duos.py`, placement `apply_duos.py`.
- Priorité Instagram (objectif 5K vues par reel). Garder le style, mais un sujet neuf à chaque reel : jamais une copie ni une simple traduction d'un reel déjà publié.

## Reels « histoire » (10 nov. 2026, consigne de Yaacoub)
- Ne plus copier le duo gagnant : vrais personnages humains (moteur `tools/reel_engine/story.html`), une vraie mini-histoire façon « clipping » (on se moque du héros → galère → il s'organise avec l'outil → « X plus tard » → réussite, les autres sont bouche bée). Configs `build_stories.py`, placement `apply_stories.py`.
- Chaque histoire : héros, décor, quête et produit différents. Jamais le même format plus de 2 jours de suite.
- Les meilleurs reels vont du jeudi au dimanche (ce sont eux qui percent) ; la semaine, les formats à tester.
