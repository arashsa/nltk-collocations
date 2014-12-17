import nltk
from nltk.collocations import *
from os import walk
import os

bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()
text_as_string = ''
collocations = open('files/test_run.txt', 'w')

for (path, names, file_names) in walk('/Users/arashsaidi/Work/LBK - prosjekt/lbk_22.04.14/Sakprosa/SA03'):
    for f_name in file_names:
        if '.txt' in f_name and '.okl' not in f_name:
            print f_name
            text = open(os.path.join(path, f_name), 'r')
            for w in text.readlines():
                text_as_string += w
tokens = nltk.wordpunct_tokenize(text_as_string)
finder = BigramCollocationFinder.from_words(tokens)
finder.apply_freq_filter(3)
scored = finder.score_ngrams(bigram_measures.raw_freq)
# scored = finder.nbest(bigram_measures.pmi, 10)
# result = sorted(bigram for bigram, score in scored)
for i in scored:
    collocations.write(i[0][0] + ' ' + i[0][1] + ': ' + str(i[1]))