# Moteur de reels animés · Maker FlowTools

Règle de Yaacoub (1er nov. 2026) : **tous les reels sont des animations très vivantes** (éléments qui « pop », sortent, bougent, couleurs fortes, fond foncé, grosse accroche, tableau de bord incliné et animé). **Plus jamais de diaporama d'images en reel** : une image fixe se publie en post image.

## Fichiers
- `engine.html` : moteur d'animation (1080×1920, 30 i/s). Rendu déterministe : `init(config)` puis `render(t)`.
- `render.js` : capture chaque image avec Playwright, ajoute la bande son, encode en MP4 H.264 (`ffmpeg`). Écrit aussi `<id>_cover.jpg` (image à `coverAt` secondes).
- `audio.py` : musique douce générée (nappes, arpèges, pas de grosse caisse) + petits sons « pop », « tick », « whoosh », « ding » calés sur les animations.
- `build_configs.py` : textes et données de chaque reel (FR/EN), et association créneau du calendrier → reel. Produit `reels.json` et `captions.json`.

## Fabriquer un reel
```bash
cd tools/reel_engine
python3 build_configs.py                      # régénère reels.json / captions.json
node render.js reels.json ../../videos/anim A1_FR,A1_EN --workers 3   # ≈ 40 s par reel
node render.js reels.json /tmp/apercu A1_FR --preview                 # images fixes pour vérifier
```
Ajouter un reel = ajouter un concept dans `C` (accroche, mots surlignés `hl` = index des mots, `widget`, `floats`, `sub`, `cap`) puis un créneau dans `SLOTS`.

Widgets disponibles : `kpis` (tuiles qui comptent), `status` (lignes + pastilles, compte à rebours, bulle de rappel), `bars` (barres qui poussent + total), `counter` (écart bancaire ramené à 0), `calc` (coût → marge → prix suggéré), `heat` (carte d'habitudes, jour vide entouré), `check` (liste d'étapes cochées), `seat` (recherche d'un invité), `tables` (tables de toutes tailles), `toggle` (bascule FR/EN), `verdict` (tampons À refaire / Équilibre / Perte), `stock` (alerte de stock bas).

Thèmes : `landlord`, `treasurer`, `seat`, `habit`, `artisan`.

## Règles de contenu
- Fond foncé, jamais de blanc. Accroche énorme, mots clés surlignés, emoji qui pop.
- Données d'exemple seulement (étiquette « Données d'exemple » sur la carte) ; jamais assez du produit pour le copier ; on ne montre que des fonctions qui existent vraiment.
- Musique douce, aucun « boum boum ». Yaacoub n'apparaît jamais.
- Aucun rabais ni résultat inventé.
