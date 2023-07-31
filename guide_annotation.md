# Guide d'annotation du Tuwari (Tww)

> Le corpus est découpé en morphèmes et non en mots. Cela implique une annotation particulière. Le tuwari est une langue en cours d'analyse, aussi son annotation est appelée à changer.

## Conversion du corpus au format (S)UD

L'une des particularité du Tuwari est la présence de genre nominaux, au nombre de 12. Nous les avons identifié via des `NounClass` (Tww1 à Tww12) et leur avons attribué la POS `DET`. Voici un tableau récapitulatif des genres : 

gloss|Gender|Examples|Semantic
---|---|---|---
M|we|Man, boy (PN and nouns referring to masculine individuals)|Male (human only)
F|se|Woman, girl, PN and nouns referring to female individuals|Female (human only)
III|mo|Road, taro, name, dog, bone, backbone, wound, canoe, stick, wind...|Length
IV|he|Speech, shoulder, snake, paddle, gourd, rain, mouth, lips, knife, wave, sand|Flat
V|fo|cloth, sun, fish, spear, papaye, stone, mountain, summit, rodent, tooth|Something standing out from a surface
VI|o|mosquito, tree, light, penis, toad|
VII|fe|hand, firewood, awe, leg|
VIII|pe|raft, bow, feather|
IX|sapo|house, shelter, raft, plane, song, danse|Something one can stand in
X|tano|water, fire|
XI|pla|arrow|
XII|mi|rice|Edible part of a vegetable or of an animal

Tout ce qui caractérise les noms a été identifié comme `DET`, tandis que tout ce qui caractérise les verbes ont été annotés comme `AUX` (en dehors des marques d'accord en nombre, annotés `X`.)

Pour les verbes se trouvant en milieu de phrase, ils ont été identifiés comme étant des verbes médiaux, auxquels on a donc ajouté le feature `VerbForm=Med`. Pour les auxiliaires indiquant la fin de phrase, nous les avons considéré comme la racine de la phrase, ayant un statut prédicatif. Nous leur avons donc attribué le feature `VerbForm=Fin`.

Il y a également des light verbs en Tuwari, auxquels nous avons donc attribué le feature `VerbType=Light`. Ils sont sinon identifiés comme des `VERB`, sauf dans les cas où ils ont un rôle de copule. Ils sont alors identifiés comme des `AUX`.

Il existe encore une interrogation sur le statut des démonstratifs. S'agit-il de déterminants ou de pronoms ? Nous leur avons pour l'instant attribué la POS `PRON` mais cela pourra changer par la suite.

## Annotation sur Arborator Grew

> Nous avons commencé l'annotation sur un petit échantillon de phrases. Aussi, toutes les relations et structures possibles n'ont pas été rencontrées.

### Syntagmes verbaux


Nous avons ajouté quelques `deeprel` pour affiner quelques relations entre morphèmes : 
- `@tense` : utilisé pour les relations entre le morphème verbal marquant le temps et le verbe
- `@asp` : utilisé pour les relations entre le morphème verbal marquant l'aspect et le verbe
- `@mod` : utilisé pour les relations entre le morphème verbal marquant la modalité et le verbe.

Pour la relation entre l'auxiliaire indiquant la fin de la phrase et le verbe auquel il est rattaché, nous avons choisi la relation `comp:pred`.

Une `subrel` a également été ajouté pour les relations entre le prédicat est les verbes médiaux : ces relations sont annotées `conj:chain` et partent du prédicat vers chacun des verbes médiaux.

Il y a encore des questionnements sur les relations reliant le prédicat et les autres morphèmes verbaux le caractérisant, notamment ceux se plaçant entre le verbe prédicatif et l'auxiliaire final.

### Syntagmes nominaux

Pour ce qui est des groupes nominaux, le `DET` marquant le genre du nom a été choisi comme étant la tête du syntagme. Aussi, la relation entre le verbe et le groupe nominal se fait sur cet élément.


