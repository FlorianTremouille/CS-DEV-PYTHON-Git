SPACE INVADER
FLORIAN TRÉMOUILLE & HUGO MIAGLIA

Adresse répertoire GIT : 'https://github.com/FlorianTremouille/CS-DEV-PYTHON-Git'

Règles spéciales/Mécaniques de jeu choisies : 
	Après avoir été touché, nous sommes en mode 'invincible' pendant 5 secondes.
	Les tirs du joueurs ne traversent pas les rochers.
	Les tirs du joueurs ne détruisent pas les rochers.
	Les ennemis en contact avec un rocher meurent et le rocher est détruit.
	Le joueur meurt si un ennemi le touche peu importe son nombre de vie.
	Le joueur meurt si il est à '0' vie puis est touché par un tir.
	Lorsque qu'un alien d'un niveau meurt, les autres aliens du niveau en cours accélèrent.
	Le l'alien BOSS possède 3 vies. Sa santé est indiqué par sa bordure:
		Vert = 3 coups restants pours le tuer
		Orange = 2 coups restants pours le tuer
		Rouge = 1 coup restants pours le tuer

Fonctionnement du système de niveau:
	5 niveaux sont prédéfinis dans les fichiers level_X.json.
	Les 4 premiers sont des niveaux "classiques" avec des aliens normaux et des aliens en capacité de tirer.
	Le niveau 5 est un nivveau spécial avec un alien BOSS.
	Au niveau 6, les niveaux redémarrent a 1 avec une vitesse de déplacement des aliens plus rapide.
	Au nieaux 11, il en est de même... etc

Implémentation de la LISTE:
	Gestion du placement des rochers prédéfini par une liste.
	Points d'apparition des groupes de rochers calculés puis inséré dans une liste, cette liste est ensuite lue pour faire apparaitre chaque rocher.
	Voir le fichier 'RocksGroup.py'

Implémentation de la PILE:
	Ajout des meilleurs score au fur et à mesure et possibilité de supprimer le dernier meilleur score dans le menu.
	Voir le fichier 'Score.py'

Commandes de triche :
Touche 'L' pour s'ajouter une vie
Touche 'G' pour passer en mode invincible (rappuyer pour sortir de ce mode)

Commandes:
Touche 'Flèche Droite' pour aller à droite
Touche 'Flèche Gauche' pour aller à gauche
Touche 'Espace' pour tirer