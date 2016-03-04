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
#=# This program applies the regexps in EnglishFeatureRegexps3 to the grammars
#=#   in MelanesianLanguages to produce proposed featue values for
##    language*feature.
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

import MelanesianLanguages
import EnglishFeatureRegexps3
import re
import codecs
import sys

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
#=# Construct an array of compiled (for speed) regular expressions
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

REs                             = []
for reg in EnglishFeatureRegexps3.Regexps:
 r                              = re.compile(reg,re.U)
 REs.append( r )

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
#=# For each language, for each grammar for that language
#=#  load the grammar as text, then check each feature regexp against the grammar
#=# If the pattern is matched more than 10 times, the feature is 'proved'
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#

brkct                           = 0
allct                           = 0
print "Matched,Feature Name,Feature Line,Grambank Feature Id,Language Code,Grammar,Number of Matches"
for code in MelanesianLanguages.Grammars.keys():
 grammars = MelanesianLanguages.Grammars[code]
 for grammar in grammars:
  allct                        += 1
  # print grammar
  try:
   f                            = open(grammar, "rb")
   txt                          = f.read()
   f.close()
   #
   txt                          = re.sub(r'[^A-Za-z\n]*', r'', txt)
   txt                          = txt.lower()
   # print txt
   # txt                          = re.sub(ur'\s\s+', ' ', txt)
  except UnicodeDecodeError:
   print >> sys.stderr, "Bad Grammar", grammar
   brkct                       += 1
   continue
  for ri in range(len(REs)):
   r                            = REs[ri]
   fname                        = EnglishFeatureRegexps3.Names[ri]
   fid                          = EnglishFeatureRegexps3.GrambankFeatureId[ri]
   matches                      = r.findall( txt )
   matched                      = ""
   if len(matches) > 1: matched =  "+"
   if len(matches) > 10: matched = "*"
   print "\"%s\",\"%s\",%d,%d,%s,\"%s\",%d" % (matched,fname,ri+2, fid,code, grammar, len( matches ))
# print brkct, allct

