#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from json import load



def decomp(file:str, output:str, dico_decomp:dict):
    with open(file, "r") as rf, open(output, "w") as wf:
        compt = 1
        for line in rf:
            line = line.strip()
            
            if line.startswith("#"):
                # Écrit les lignes de commentaires sans modification
                wf.write(line + "\n")
            elif line:
                # Traite les lignes de phrase
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
                        # print(i)
                        new_token_id = str(compt)
                        new_form, new_lemma, new_upos, new_misc = decomp_form
                        # new_form = dico_decomp[lemma][form][i][0]
                        # new_lemma = dico_decomp[lemma][form][i][1]
                        # new_upos = dico_decomp[lemma][form][i][2]
                        # new_misc = dico_decomp[lemma][form][i][3]
                        
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
                    wf.write(line + "\n")  # Écrit la ligne telle quelle si aucune modification n'est nécessaire
                    compt += 1
            else:
                wf.write("\n")  # Écrit une ligne vide entre les phrases
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



