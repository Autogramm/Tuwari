#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Pour exécuter ce script, se placer dans le répertoire global du projet et exécuter : 
python3 scripts/merge.py ./chemin/corpus_segm/ ./chemin/corpus_annote/ ./chemin/output/

"""


import argparse
from pprint import pprint
from glob import glob
import pyconll

def crea_dico_gloss(corpus_gloss:str):
	dico_gloss={}
	sublist=[]
	for doc_gloss in glob(f"{corpus_gloss}*"):
		with open(doc_gloss, "r") as g_file:
			for gline in g_file:
				if gline.startswith("#"):
					if sublist!=[]:
						dico_gloss[doc_id].update({sent_id:sublist})
						sublist=[]
					if "sent_id" in gline:
						sent_id=gline.split(" = ")[1][:-1]
					elif "doc_id" in gline and sent_id!="":
						doc_id=gline.split(" = ")[1][:-1]
						if doc_id not in dico_gloss:
							dico_gloss.update({doc_id:{}})
				elif gline != "\n" and gline!="" :
					fields=gline.split("\t")
					token_id = fields[0]
					form = fields[1]
					lemma = fields [2]
					upos = fields [3]
					xpos = fields [4]
					feats = fields[5]
					misc = fields [9]
					sublist.append([token_id, form, lemma, upos, xpos, feats, misc])
		dico_gloss[doc_id].update({sent_id:sublist})
	return dico_gloss


def merge(corpus_dep: str, dico_gloss: dict, output_path: str):
	for file in glob(f"{corpus_dep}*"):
		conll=pyconll.load_from_file(file)
		for sentence in conll:
			doc_id=sentence.meta_value("doc_id")
		if doc_id in dico_gloss:
			output=f"{output_path}{doc_id}.conll"
			with open(file, "r") as rf:
				compt_tok=0
				with open(output, "w") as wf:
					for line in rf : 
						line = line.strip()
						if line.startswith("#"):
							wf.write(line + "\n")
							if "sent_id" in line:
								sent_id=line.split(" = ")[1]
								# print(sent_id, type(sent_id))
						elif line != "\n" and line!="":
							fields=line.split("\t")
							head = fields[6]
							deprel = fields[7]
							deps = fields[8]
							if compt_tok >= len(dico_gloss[doc_id][sent_id]):
								print(f"La phrase {sent_id} n'a pas le même nombre de token dans les deux fichiers")
							if sent_id in dico_gloss[doc_id]:
								dico_gloss[doc_id][sent_id][compt_tok][0]
								new_line = "\t".join([
										dico_gloss[doc_id][sent_id][compt_tok][0],
										dico_gloss[doc_id][sent_id][compt_tok][1],
										dico_gloss[doc_id][sent_id][compt_tok][2],
										dico_gloss[doc_id][sent_id][compt_tok][3],
										dico_gloss[doc_id][sent_id][compt_tok][4],
										dico_gloss[doc_id][sent_id][compt_tok][5],
										head,
										deprel,
										deps,
										dico_gloss[doc_id][sent_id][compt_tok][6]
										])
								wf.write(new_line)
								compt_tok+=1
						else:
							wf.write("\n")
							compt_tok=0
			print("Merging effectué")
		else:
			print(f"Le fichier avec lequel le fichier {file} doit être mergé n'a pu être trouvé.")



if __name__ == "__main__":
	parser=argparse.ArgumentParser()
	parser.add_argument("path_gloss", help="chemin du fichier à vérifier")
	parser.add_argument("path_dep", help="chemin du fichier de sortie")
	parser.add_argument("path_output", help="Dictionnaire pour la décomposition des morphèmes")
	args=parser.parse_args()
	dico_gloss=crea_dico_gloss(args.path_gloss)
	merge(args.path_dep, dico_gloss, args.path_output)
