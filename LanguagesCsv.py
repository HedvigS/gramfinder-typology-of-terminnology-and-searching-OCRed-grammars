#! /usr/bin/env python
# -*- coding: utf-8 -*-

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
#=# (c) 2015 T. Mark Ellison
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

import codecs
import re
import csv
import sys
import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode
import os
import os.path

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
#=# Load Melanesian Languages
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
def iso_lgcode(item):
 codes                          = []
 codestr                        = item["lgcode"]
 if len(codestr) == 3: return [ codestr ]
 parts                          = re.split(ur'([\[\]])', codestr)
 INCODE                         = False
 lastPart                       = ""
 for part in parts:
  if part == "[":
   INCODE                       = True
  elif part == "]" and INCODE:
   codes.append( lastPart )
   INCODE                       = False
  else: lastPart                = part
 return codes

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
#=# Load Melanesian Languages
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
PreMelanesianCodes = csv.DictReader(open("melanesia.tab"),delimiter="\t")
MelanesianCodes = []
MelanesianLines = {}
MelanesianGrammars = {}
for code in PreMelanesianCodes:
 MelanesianCodes.append( code["Code"] )
 MelanesianLines[ code["Code"] ] = [ code["Code"], 0,0,0,0,0,0,0, "","" ] # Code, BibTexEntry, Fn, HhType, Grammar, GrammarSketch, GrammarOcred, GrammarSketchOcred

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
#=# Load BibTex Languages
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
with open("hh.bib","r") as f:
 lines                          = f.read()
 BibDatabase                   = bibtexparser.loads(lines) # , parser=parser)

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
#=# Txt Grammar Dirs
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
TxtGrammarDirs1                 = [
  "./../typology_of_grammars/py/ocrgrammars/ptxt/africa/",
  "./../typology_of_grammars/py/ocrgrammars/ptxt/australia/",
  "./../typology_of_grammars/py/ocrgrammars/ptxt/eurasia/",
  "./../typology_of_grammars/py/ocrgrammars/ptxt/north_america/",
  "./../typology_of_grammars/py/ocrgrammars/ptxt/south_america/",
  "./../typology_of_grammars/py/ocrgrammars/ptxt/papua/"
 ]
TxtGrammarDirs2                 = [
  "./../typology_of_grammars/py/ocrgrammars/ptxt2/africa/",
  "./../typology_of_grammars/py/ocrgrammars/ptxt2/australia/",
  "./../typology_of_grammars/py/ocrgrammars/ptxt2/eurasia/",
  "./../typology_of_grammars/py/ocrgrammars/ptxt2/north_america/",
  "./../typology_of_grammars/py/ocrgrammars/ptxt2/south_america/",
  "./../typology_of_grammars/py/ocrgrammars/ptxt2/papua/"
]

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
#=# Build up the columns for each line
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
for item in BibDatabase.entries:
 if not item.has_key("lgcode"): continue
 codes                          = iso_lgcode( item )
 if len( codes ) > 1: continue
 print >> sys.stderr, "Codes", codes
 #
 found                          = False
 for code in codes:
  if code not in MelanesianCodes: continue
  found = True
  MelanesianLines[ code ][1]   += 1
 if not found: continue
 #
 if item.has_key("hhtype"):
  for code in codes:
   if code not in MelanesianCodes: continue
   MelanesianLines[ code ][3]  += 1
  types                         = item["hhtype"].split(";")
  #
  if "grammar" in types:
   for code in codes:
    if code not in MelanesianCodes: continue
    MelanesianLines[ code ][4] += 1
  #
  if "grammar_sketch" in types:
   for code in codes:
    if code not in MelanesianCodes: continue
    MelanesianLines[ code ][5] += 1
 #
 if item.has_key("fn"):
  for code in codes:
   if code not in MelanesianCodes: continue
   MelanesianLines[ code ][2]  += 1
 #
 if item.has_key("fn") and re.match(ur'^.*grammar.*$', item["hhtype"]):
  filename                      = re.split(ur'[\\/]',item["fn"])[-1]
  filename                      = re.sub(ur'.pdf', '.txt', filename)
  #
  #
  filepaths                     = []
  for grammardir in TxtGrammarDirs1:
   if os.path.isfile(grammardir+filename):
    filepaths.append( grammardir+filename )
  for code in codes:
   if code not in MelanesianCodes: continue
   if not MelanesianGrammars.has_key( code ): MelanesianGrammars[ code ] = []
  for code in codes:
   if code not in MelanesianCodes: continue
   MelanesianLines[ code ][6]  += len( filepaths )
  if filepaths:
   for code in codes:
    if code not in MelanesianCodes: continue
    MelanesianLines[ code ][8] = filepaths[0]
    MelanesianGrammars[ code ] += filepaths
  #
  filepaths                     = []
  for grammardir in TxtGrammarDirs2:
   if os.path.isfile(grammardir+filename):
    filepaths.append( grammardir+filename )
  for code in codes:
   if code not in MelanesianCodes: continue
   MelanesianLines[ code ][7]  += len( filepaths )
  if filepaths:
   for code in codes:
    if code not in MelanesianCodes: continue
    MelanesianLines[ code ][9]  = filepaths[0]
    MelanesianGrammars[ code ] += filepaths


#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
#=# Print out the results
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

MelanesianCodes.sort()
print "Code,BibTex Entry,Fn,HhType,Grammar,GrammarSketch,Txts,Txt2s,Example Txt,Example Txt2"
for code in MelanesianCodes:
 print "%s,%d,%d,%d,%d,%d,%d,%d,\"%s\",\"%s\"" % tuple(MelanesianLines[code])

f                               = codecs.open("MelanesianLanguages.py","w","utf8")
#
f.write( "Grammars = {}\n" )
for code in MelanesianCodes:
 f.write( "# Code: %s\n" % (code) )
 if not MelanesianGrammars.has_key( code ): continue
 f.write( "Grammars[\"%s\"] = []\n" % (code) )
 for grammar in MelanesianGrammars[code]:
  f.write( "Grammars[\"%s\"].append(\"%s\")\n\n" % (code, grammar) )
#
f.close()
