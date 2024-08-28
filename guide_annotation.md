# Question sylvain

- ## Subordiation /=mo/
  io -[mod]-> =mo -[comp]-> verb ; actuellement aussi : conf:conj
  ??? non, conj:sub !!!
  mais alors la relation mo -> Vb
  14...T47 / 1.6
- aadv pour fail ? "fali : aadv"
- annoter indexation sujet dans i-nai-m-wi-i : m et we ? comp:det ?
- où met-on le "m" de morphem? prend-il la place d'une annotation sémantique ?
- deepl
- wefi-mo (14...T47/1.2 "with a rope" : mod? mod@instrumental ?
- gloser les étiquettes
- les phrases doivent avoir un ID unique dans le corpus ?
- mod:poss pour possession adnominale ?
- coverb, object interne? (pour l'instnat : comp@lvc)
- négation : 141116_01_T47
  fe- tuei -ne
- citation style direct
- pour mod, possibilité de mettre @place, @time, @maner... ?
- maminofo 2015T22_10 -> comp:det entre mami et mo ? Bon sens (cohérent 
avec les autres, mais noter la relation inverse?)



# TODO sur corpus en amont

- mo "verb"-> SCONJ




# Tuwari annotation scheme

The corpus is segmented into morphemes (UD tokens = morphems and not 
word). Relations between morphems have the additional "deep" feature "m".


# Verb

## Person indexation suffixes

comp:det

## TAM suffixes

the root of a sentence is the predicate marker -wo ~ -io, last suffix on 
the verb. TAM markers are then linked from right to left with the relation 
comp:aux.

## adv


aplo





## SVC : compound:svc

https://github.com/UniversalDependencies/docs/issues/819

https://github.com/UniversalDependencies/docs/issues/386


compound:lvc

- svc -> compound:svc ; compound : relation syntaxique cohésive

## Subordiation /=mo/

io -[mod]-> =mo -[comp]-> verb
??? non, conj:sub !!!

# GN

# determiner

det -[comp:det]-> N

# N-N compound

ni-tosi 'fire-torsh' : -[compound]->

# subject of the form: "NP + PR"

- When a subject GN has the form "Samuel, Erik, ta..." ("Samuel, Erik, 
we..."), then : V-[subj]->ta-[comp:det]->Samuel

# cc for correlative construcion (1sg=fa... 3sg=fa)

# mod:appos

for apposition : =fa-[mod:appos]->=lo in mwe=fa [ni tosi-tano=lo] 'as for 
he, with a torsh, ...'


# Syntaxe

## clause chain

, conj:chain pour l'instant : conj:appos (faute de 

linked from right to left (not all conj:chain are linked on the same final 
verb).

Il y a des comp:chain à corriger

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





#


What could be a appropriate way for encoding clause chaining in UD?

Clause chaining is a construction for linking a serie of clauses; in all
clauses but the final one the verb is not fully inflected
and inherit some features from the verb of the final clause, which is fully
inflected.  Clause chaining is common in particular in Papuan languages.

Languages using clause chaining often (but not always) have a switch
reference system, i.e. a marker at the end of the medial clauses that
express whether the subject of the following clause is coreferential with
the subject of the current one or not.

The first of the two following examples illustrates clause chaining in a
language having a switch-reference system, the second example illustrates a
language without switch reference.

In (1) (Tauya, MacDonald Lorna (1990) A grammar of Tauya, Mouton/Berlin),
the two medial verbs inherit from the final verb the specification for mood
(here, indicative).  The subject stay the same, thus each clause has the
"-pa" suffix for 'SS' ('same subject'), instead of the "-te" for 'different
subject'.

(1) Tauya
ya mei  fofe-pa  momune-pa  ni-e-’a
1S hear venir-SS asseoir-SS manger-1/2S-IND
‘I came hear, sat down and ate.’

In Tuwari, the medial verb are marked with "-ne", the final one by 
"-io". In (2), the medial verb "afeteli" is not inflected but for the medial 
marker; the final verb is inflected for mood ('irrealis'), illocutionary 
force ('affirmative'), agree with the gender and number of the subject, 
and have a marker of final verb (-i~-io)

(2) Tuwari
a   opsono-ma   afeteli-ne nepia-ma.     i-nai-m-wi-i
1SG village-dir leave-med  far_away-dir  go-IRR-AFF-SG.M-FIN
'I will leave the village and go far away'

Clause chain has been analysed either as subordination, coordination, or as
a third clause linking type, cosubordination (Olson 1981, Foley and Van
Valin 1984).  Unlike subordinates, medial clauses are not embedded (they
are not complement or adjunct of the final clause).  However, alike
subordinates (and unlike coordinates) clauses, medial clauses have a
dependency relationship for a particular inflectional category with the
final clause.

In Foley 2010 (Clause linkage and nexus in Papuan languages, In Brill I. ed
(2010) Clause linking and clause hierarchy: Syntax and pragmatics,
Benjamins/Amsterdam, 27-50, clause chain are characterized as an instance
of coordination " that differs from normal clausal coordination in the type
of constituents coordinated".


(Sylvain je ne suis pas sûr ici :)

We could use "conj", with a specification "conj:chain". "conj" can mark 
"asyndetic" coordination 
(https://universaldependencies.org/u/dep/conj.html). However with "conj" 
"The head of the relation is the first conjunct", whereas in clause chain 
we would like the head of the relation to be the last verb.

