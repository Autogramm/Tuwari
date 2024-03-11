# Guide d'annotation du Tuwari (Tww)

Morphem-based SUD annotation scheme.

## POS

### Noun

Noun class agreeing article have the feature Class and values such as `Tww1`, ..., `Tww12)` and POS=`DET`. Some other noun-determination devices have POS= DET` (which one ?)

Démonstratifs (adnominal or pronominal) have POS=`PRON`. To be further analysed.

### Verb

All TAM affixes, clitics or free forms have POS=`AUX` (gender and number agreeing affixes have POS=`X`.)

Medial verbs have a feature `VerbForm=Med`. Last affixes, with predicative value, have a feature `VerbForm=Fin` (should be on the lexical verb?).

Light verbs have feature `VerbType=Light` (some have POS=`VERB`, while copula have POS=`AUX`).

## Relations

### Nouns

Pour ce qui est des groupes nominaux, le `DET` marquant le genre du nom a été choisi comme étant la tête du syntagme. Aussi, la relation entre le verbe et le groupe nominal se fait sur cet élément.

### Verb

Some `deeprel` further qualify comp:aux relation between a POS=AUX and another POS=AUX (or the lexical verb):

- `@tense` : tense
- `@asp` : aspect
- `@mod` : mood

Relation with the affixes indicative of predicative / final verb status and its target is `comp:pred`.

Medial verb are linked the final verb as their head (or the following medial verb) with `conj:chain`.


