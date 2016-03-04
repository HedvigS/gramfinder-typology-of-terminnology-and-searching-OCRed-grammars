#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
#=# (c) 2015 Hedvig Skirgard, Siva Kalyan - regexps
#=# (c) 2015 T. Mark Ellison - python code
#=# Wellsprings of Language Diversity (Laureate Project)
#=# School of Culture, History and Language
#=# College of Asia and the Pacific
#=# Australian National University
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
#=# This program goes through Harald Hammerstrom's hh.bib file, identifying
#=#   Melanesian languages, and checking whether these have grammars available
#=#   in the corpus of grammars.
#=# It outputs python code defining a table listing Melanesian languages
#=#   and the grammars which describe them.
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#


Names = [
 'Receiprocal Morphology',
 'Negative Morphology',
 'Irrealis Morphology',
 'Perfective Morphology',
 'Past Distance Morphology',
 'Future Morphology',
 'Past Morphology',
 'Present Morphology',
 'Postposition',
 'Preposition',
 'Possessive Suffix',
 'Possessive Prefix',
 '(In)Alienable Posession',
 'Gender/Noun Class',
 'Distality',
 'Dual Pronoun',
 'Gendered Pronoun',
 'Clusivity',
 'Definite/Specific Article',
 'French'
 ]

Morphology = ur'((af|pre|suf|in|circum)fix|(en|pro|circum|)?clitic|tone|(by)?(reduplication|suppletion))'

Regexps = [
 ur'reciprocal'+Morphology,
 ur'negative'+Morphology,
 ur'irrealis'+Morphology,
 ur'(im)?perfect(ive)?'+Morphology,
 ur'(remote|distant|hodiernal|hesternal|immediate)past',
 ur'future'+Morphology,
 ur'(past|pra?eterite?)'+Morphology,
 ur'present'+Morphology,
 ur'postposition',
 ur'preposition',
 ur'possessivesuffix',
 ur'possessiveprefix',
 ur'((in)?alienable)|((ob|sub)jectivepossession)',
 ur'(gender|nounclass)',
 ur'(distal|proximal|closetohearer|closetospeaker|farawayfromspeaker|farawayfromhearer)',
 ur'(dualpronoun)',
 ur'(masculine|feminine|neuter|(in)?animate)pronoun',
 ur'((in|ex)clusive)'+Morphology,
 ur'(definite|specific)article',
 ur'(ils|sont|leur|langue)'
]

GrambankFeatureId = [
 20,
 28,
 30,
 31,
 35,
 50,
 59,
 61,
 62,
 74,
 75,
 82,
 83,
 84,
 85,
 86,
 87,
 107,
 115,
 1001
 ]

