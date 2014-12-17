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

    def __init__(self, path):
        self.words = []

        for (path, names, file_names) in walk(path):
            for f_name in file_names:
                if '.txt' in f_name and '.okl' not in f_name:
                    self.read_files(path, f_name)

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
        bcf = BigramCollocationFinder.from_words(self.words)
        collocations = bcf.nbest(BigramAssocMeasures.likelihood_ratio, 4)
        for w in collocations:
            print w[0], w[1]