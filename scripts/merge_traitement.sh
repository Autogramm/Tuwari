#!/bin/bash

###########

# Pour exécuter le script, se placer dans le répertoire du projet et exécuter : 
# ./scripts/merge_traitement.sh ./chemin/corpus_original/ ./chemin/corpus_annote/ ./chemin/output ./chemin/dico_segmentation.json ./chemin/regles_grew.tsv

###########




gloss_path=$1
dep_path=$2
output_path=$3
dico_decomp=$4
tableau_regles=$5

mkdir ./temp_corpus_segm
mkdir ./temp_corpus_merge

# Resegmentation des fichiers non traités, modifiés dans logiciel de glose
for gfile in $gloss_path* ; do
	basename_segm=$(basename -s .conll $gfile)
	python3 scripts/resegmentation.py $gfile ./temp_corpus_segm/$basename_segm.conll $dico_decomp
done

# Merge des fichiers annotés et des fichiers modifiés dans logiciel de glose
python3 scripts/merge.py ./temp_corpus_segm/ $dep_path ./temp_corpus_merge/


rules_path=$(dirname $tableau_regles)

# Génération des règles grew
python3 scripts/generation_regles_grew.py $tableau_regles $rules_path/regles_tww.grs 

# Application des règles grew
for ofile in ./temp_corpus_merge/* ; do
	basename_merge=$(basename -s .conll $ofile)
	transform=$(grew transform -grs regles/regles_tww.grs -strat "Onf(tuwari)" -i $ofile)
    echo "$transform" > $output_path$basename_merge.conllu
done

rm -r temp_corpus_*

