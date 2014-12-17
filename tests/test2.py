import itertools
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures


def bigram_word_feats(words, score_fn=BigramAssocMeasures.chi_sq, n=200):
    """
    Simple method for extracting significant bigrams
    :param words:
    :param score_fn:
    :param n:
    :return:
    """
    bigram_finder = BigramCollocationFinder.from_words(words)
    bigrams = bigram_finder.nbest(score_fn, n)
    return dict([(n_gram, True) for n_gram in itertools.chain(words, bigrams)])

test_file = open('/Users/arashsaidi/Work/LBK - prosjekt/lbk_22.04.14/Periodika/AV01/AV01VL9629.txt', 'r')
test_dict = bigram_word_feats('What do you want from me? Give me something that you want from me.')

for i in test_dict.items():
    print i