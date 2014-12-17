from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
import string
import os
from os import walk


def remove_punctuation(s):
    """
    Simple (effective?) way of removing punctuation.
    The translate method is implemented in C using a lookup table.
    :param s:
    :return:
    """
    table = string.maketrans("", "")
    return s.translate(table, string.punctuation)


class Collocations():

    def __init__(self, read_files_path, save_file_path):
        self.words = []
        self.bigram_collocations_file = open(save_file_path + 'bigrams.txt', 'w')
        self.trigram_collocations_file = open(save_file_path + 'trigrams.txt', 'w')

        print 'Started reading files...'
        for (read_files_path, names, file_names) in walk(read_files_path):
            for f_name in file_names:
                if '.txt' in f_name and '.okl' not in f_name:
                    # print f_name
                    self.read_files(read_files_path, f_name)

        self.extract()

    def read_files(self, path, f_name):
        """
        Reads each file and appends to word_list removing punctuation
        :param path:
        :param f_name:
        :return:
        """
        self.words = []
        with open(os.path.join(path, f_name), 'r') as f:
            for line in f:
                for word in line.split():
                    self.words.append(remove_punctuation(word.lower()))

    def extract(self):
        # TODO: remove stop words
        # bcf.apply_word_filter(filter_stops)
        """
        Simple extraction method from the nltk cookbook

        There are many more scoring functions available besides likelihood_ratio().
        Consult the NLTK API documentation for NgramAssocMeasures in the nltk.metrics package,
        to see all the possible scoring functions.
        :return: None
        """

        # print words
        print 'Extracting collocations...'
        bcf = BigramCollocationFinder.from_words(self.words)
        collocations = bcf.nbest(BigramAssocMeasures.likelihood_ratio, 100)
        for w in collocations:
            self.bigram_collocations_file.write(w[0] + ' ' + w[1] + '\n')
        self.bigram_collocations_file.close()

run = Collocations('/Users/arashsaidi/Work/LBK - prosjekt/lbk_22.04.14/',
                   'collocations/saved_test1_LBK_Hele')