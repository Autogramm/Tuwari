# Tuwari

## Contenu de ce dépôt : 
- corpus : 
	- `corpus_original` : contient les fichiers du corpus sortant du logiciel de glosage, au format conll
	- `corpus_non_annote` : contient les fichiers du corpus traités, prêts à être mis en ligne sur Arborator Grew pour annotation
	- `corpus_annote` : contient des fichiers du corpus à merger avec des fichiers sortant du logiciel de glosage, pour mise à jour des informations.
	- `corpus_merge` : contient les fichiers annotés et mis à jour (ce répertoire contient pour l'instant des fichiers qui devraient être identiques à ceux sur Arborator Grew, mais qui ont été générés à partir de `merge_traitement.sh` pour test)
- regles : 
	- `regles_tww.tsv` : un tableur contenant les règles de conversion des étiquettes du logiciel BaseX (?) vers les étiquettes UD
	- `regles_segmentation.json` : un dictionnaire au format json contenant les règles de segmentation de certains morphèmes à redécouper
	- `regles_tww.grs` : un fichier contenant les règles grew, généré automatiquement par le script `generation_regles.py` et par le script `traitement_fichiers.sh`
- scripts : 
	- `resegmentation.py` : un script python resegmentant certains morphèmes
	- `generation_regles_grew.py` : un script python convertissant un tableau de règles en règles grew
	- `traitement_fichiers.sh` : un script bash permettant d'exécuter en une ligne de commande : 
		- la resegmentation du corpus, 
		- la génération des règles grew,
		- leur application sur le corpus resegmenté.
	- `merge.py` : un script python permettant de merger un corpus déjà annoté sur arborator grew avec un corpus sortant du logiciel de glosage (et resegmenté), pour mettre à jour les éventuelles modifications faite sur les gloses, les pos, etc.
	- `merge_traitement.sh` : un script bash permettant d'exécuter en une ligne de commande : 
		- la resegmentation du corpus à jour, sortant du logiciel de glosage, 
		- la fusion des fichiers annotés mais pas à jour avec le corpus à jour mais non annoté (resegmenté précedemment)
		- la génération des règles grew,
		- leur application sur le corpus annoté, à jour, mais ne possédant plus les étiquettes et features (S)UD.




