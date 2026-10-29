# Maker FlowTools: dossier des réseaux sociaux (29 oct. – 31 déc. 2026)

Structure du dossier
- 01_INSTAGRAM/<date>/: les fichiers de chaque publication (reel, carte, couverture, légende) classés par jour
- 02_FACEBOOK/: contenus planifiés sur la page (légendes) et calendrier
- 03_PINTEREST/: pins (images 1000×1500), titres, descriptions, liens UTM
- 04_CALENDRIER_GLOBAL/: calendrier_global.csv (toutes plateformes)
- 05_SCRIPTS_ET_LEGENDES/: toutes les légendes et hashtags
- 06_COUVERTURES_ET_VISUELS/: couvertures de reels et cartes
- 07_RAPPORTS_HEBDOMADAIRES/: modèle et rapports
- 08_GUIDES_ET_PROCEDURES/: ce guide, recherche, UTM, plan Black Friday, profils, QA, actions pour toi

Comment ça publie (rien à faire de ton côté, sauf la liste du fichier 07_Actions)
- Instagram: 2 tâches automatiques par jour (12 h 20 et 19 h 20, heure de Montréal) lisent le calendrier sur GitHub et publient le post prévu. Instagram ne permet pas la planification native par l'API, donc c'est fait à l'heure par ces tâches.
- Facebook: les vidéos et photos sont planifiées directement dans Facebook (limite de 30 jours pour les vidéos; deux tâches ponctuelles planifient la suite); la tâche du lundi ajoute des posts texte pour qu'il y ait au moins un post par jour.
- Pinterest: une tâche quotidienne (10 h 52) publie le pin du jour avec lien UTM, en rattrapant les jours manqués.
- Bilans: chaque lundi après-midi, pour la semaine lundi–dimanche (Facebook + remplissage; rapport global Facebook, Instagram, Pinterest et Etsy public). Voir 07_RAPPORTS_HEBDOMADAIRES.

Règles respectées: aucun achat, aucune pub, aucun faux abonné/commentaire/avis, aucun rabais ni prix inventé, aucune promesse de résultat, aucun conseil fiscal ou juridique, jamais de mot de passe dans le chat.
