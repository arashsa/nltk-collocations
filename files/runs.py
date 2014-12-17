#!/usr/bin/python
# -*- coding: utf-8 -*-

import nltk
from nltk.collocations import *
from nltk.tokenize import PunktWordTokenizer as PWTok

collocations = open('bam.txt', 'w')
bigram_measures = nltk.collocations.BigramAssocMeasures()

text = 'Hei på deg. Hei på meg.'
tokens = PWTok().tokenize(text)
finder = BigramCollocationFinder.from_words(tokens)
print finder
scored = finder.score_ngrams(bigram_measures.raw_freq)
for i in scored:
    collocations.write(i[0][0] + ' ' + i[0][1] + ': ' + str(i[1]) + '\n')

collocations.close()