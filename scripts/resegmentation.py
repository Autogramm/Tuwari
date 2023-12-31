#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
python3 scripts/resegmentation.py ./chemin/fichier_a_segmenter.conll ./chemin/output.conll ./chemin/dico_segmentation.json
"""

import argparse
from json import load



def decomp(file:str, output:str, dico_decomp:dict):
	with open(file, "r") as rf, open(output, "w") as wf:
		compt = 1
		for line in rf:
			line = line.strip()
			
			if line.startswith("#"):
				# Écrit les lignes d'informations sans modification
				wf.write(line + "\n")
			elif line:
				# Traite les lignes de token
				fields = line.split("\t")
				token_id = fields[0]
				form = fields[1]
				lemma = fields[2]
				upos = fields[3]
				xpos = fields[4]
				feats = fields[5]
				head = fields[6]
				deprel = fields[7]
				deps = fields[8]
				misc = fields[9]
				
				if lemma in dico_decomp and form in dico_decomp[lemma]:
					for i, decomp_form in enumerate(dico_decomp[lemma][form],1):
						new_token_id = str(compt)
						new_form, new_lemma, new_upos, new_misc = decomp_form
						
						new_line = "\t".join([
						    new_token_id,
						    new_form,
						    new_lemma,
						    new_upos,
						    xpos,
						    feats,
						    head,
						    deprel,
						    deps,
						    new_misc
						])
						wf.write(new_line + "\n")
						compt+=1
				else:
					split_line=line.split("\t")
					split_line[0]=str(compt)
					line="\t".join(split_line)
					# Écrit la ligne telle quelle si aucune modification n'est nécessaire
					wf.write(line + "\n")
					compt += 1
			else:
				# Écrit une ligne vide entre les phrases
				wf.write("\n")
				compt = 1

if __name__=="__main__":
	parser=argparse.ArgumentParser()
	parser.add_argument("file", help="chemin du fichier à vérifier")
	parser.add_argument("output", help="chemin du fichier de sortie")
	parser.add_argument("dico", help="Dictionnaire pour la décomposition des morphèmes")
	args=parser.parse_args()

	file=args.file
	output=args.output
	with open(args.dico, 'r') as json_file:
		dico_decomp=load(json_file)
	decomp(file, output, dico_decomp)



