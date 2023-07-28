#!/bin/bash

###########

# Pour exécuter le script, se placer dans le répertoire du projet et exécuter : 
# ./scripts/traitement_fichiers.sh ./chemin/corpus/ ./chemin/regles_grew.tsv ./chemin/dico_segmentation.json ./chemin/output/

###########



files_path=$1
tableau_regles=$2
dico_decomp=$3
output_path=$4

rules_path=$(dirname $tableau_regles)
python3 scripts/generation_regles_grew.py $tableau_regles $rules_path/regles_tww.grs 

for file in $files_path* ; do 
    basename=$(basename -s .conll $file)
    python3 scripts/resegmentation.py $file temp.conll $dico_decomp
    transform=$(grew transform -grs regles/regles_tww.grs -strat "Onf(tuwari)" -i temp.conll)
    echo "$transform" > $output_path$basename.conllu
done

rm temp.conll



