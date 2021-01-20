# pythonProj2_OC
Projet 2 Web scraping

Ce projet Open Classrooms permet de récuperer des informations en ligne sur le site http://books.toscrape.com/ et de les stocker dans un fichier CSV.

La partie 1 permet de récuperer les informations d'un livre uniquement

La partie 2 : une catégorie de livre complète

La partie 3 : site complet

La partie 4 : stocker les images de chaque livre.

Pour utiliser ces programmes, téléchargez chaque fichier dans un dossier de votre choix.

A l'aide d'un terminal, placez vous dans le dossier ou se trouve les fichiers et entrez : 
"python -m venv env"
Afin d'activer cet environnement, entrez la commande "source env/bin/activate" sur ubuntu, ou "env/Scripts/activate.bat" sur windows.

Maintenant votre environnement créé et activé, il ne vous reste plus qu'a installer les libraires pythons du requirements.txt et à executer via le terminal le fichier de votre choix.

Programme 1 : python <programme1.py> <lien_vers_le_livre.html>

Programme 2 : python <programme2.py> <lien_vers_la_catégorie.html>

Programme 3 : python <programme3.py>

Programme 4 : python <programme4.py> ( requiert le programme 3 car utilise les liens images dans les fichiers CSV crées par le programme 3 )
