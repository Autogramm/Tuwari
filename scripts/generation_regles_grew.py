#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""

Pour exécuter : 

python3 ./scripts/generations_regles_grew.py ./chemin/regles.tsv ./chemin/regles.grs

"""
import pandas as pd
import argparse
# from pprint import pprint


def ecriture_regles(table_regles:str, output: str):
	regles=pd.read_table(table_regles)
	with open (output, "w") as wf:
		wf.write("package tuwari {\n")
		compteur=0
		for i in range(len(regles["Conditions"])):

			# Liste des conditions (première colonne) séparée entre conditions avec et conditions sans
			liste_conditions=regles["Conditions"][i].split(" || ")

			# Liste des conditions "avec"
			liste_avec=liste_conditions[0].split(" & ")


			liste_sans=[]

			# S'il y a des conditions "sans"
			if len(liste_conditions)>1:

				# Liste des conditons "sans"
				liste_sans=liste_conditions[1].split(" & ")

			# Chaîne de caractères contenant les conditions avec
			conditions=""
			for cond in liste_avec:
				conditions+= cond + ", "
			conditions=conditions[:-2]

			# Récupère les éléments sans des conditions
			sans1=""
			if len(liste_sans)>=1:
				# Il ne faut pas que l'élément ait déjà été traité donc on ajoute la liste des résultats au filtre
				for cond_sans in liste_sans:
					sans1+=cond_sans + ", "
			sans1=sans1[:-2]

			# Liste contenant les effets de la règle en fonction de la condition (2ème colonne)
			liste_result=regles["Résultat"][i].split(" & ")


			# Ajoute dans les conditions sans les effets de la règle pour ne pas qu'il y ait de règles qui s'appliquent en boucle sur un élément
			sans2=""
			for res in liste_result:
				sans2 += res + ", "
			sans2=sans2[:-2]

			
			# Création de la chaîne de caractère en fonction des éléments "sans" indiqués (juste les résultats ou condition "sans")
			if sans1 != "":
				wo=f"\t\twithout {{X [{sans1}]}}\n\t\twithout {{X[{sans2}]}}\n"
			else:
				wo=f"\t\twithout {{X [{sans2}]}}\n"

			# S'il n'y a qu'une seule condition


			wf.write(f"""\trule r{compteur} {{\n\t\tpattern {{ X [{conditions}]}}\n{wo}""")
			if "upos" in sans2:
				command=f"""\t\tcommands {{X.xpos=X.upos;\n\t\t\t\t"""
			else:
				command=f"""\t\tcommands {{"""
			for r in liste_result:
				command+=f"""X.{r};\n\t\t\t\t"""
			command=command[:-6]+"}\n"
			wf.write(f"{command}\t}}\n")
			compteur+=1
		wf.write("}")
	

if __name__=="__main__":
	parser=argparse.ArgumentParser()
	parser.add_argument("path_tableur_regles", help="chemin du tableur contenant les règles grew à convertir")
	parser.add_argument("output", help="chemin du fichier .grs de sortie")
	args=parser.parse_args()

	table_regles=args.path_tableur_regles
	output=args.output
	ecriture_regles(table_regles, output)
	
