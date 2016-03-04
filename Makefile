#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
#=# (c) 2015 T. Mark Ellison
#=# Wellsprings of Language Diversity (Laureate Project)
#=# School of Culture, History and Language
#=# College of Asia and the Pacific
#=# Australian National University
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
#=# This Makefile combines the scripts ApplyEnglishRegexps.py and LanguagesCsv.py
#=#   to infer linguistic typological features from OCRed grammars from Harald
##    Hamerstrom's corpus of grammars.
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

matches.csv: ApplyEnglishRegexps.py MelanesianLanguages.py EnglishFeatureRegexps3.py
	python ApplyEnglishRegexps.py > matches.csv

MelanesianLanguages.py: LanguagesCsv.py hh.bib
	python LanguagesCsv.py > MelanesianLanguages.py

