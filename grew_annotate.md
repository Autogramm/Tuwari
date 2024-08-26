



% The following rule add a dependency det between a DET and a NOUN
rule r1 {
 pattern { X[upos=DET] ; Y[upos=NOUN] ; X > Y } 
 without { * -> X } 
 commands { add_edge X -[comp:det]-> Y } 
}




% The following rule add a dependency comp:det for plural marker
rule r1 {
 pattern { X[upos=X, lemma="-le_1"] ; Y[upos=NOUN] ; X > Y } 
 without { * -> X } 
 commands { add_edge X -[comp:det]-> Y } 
}


