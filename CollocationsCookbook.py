import string
import os
from os import walk
from collocation_modules import collocations


def remove_punctuation(s):
    """
    Simple (effective?) way of removing punctuation.
    The translate method is implemented in C using a lookup table.
    :param s:
    :return:
    """
    table = string.maketrans("", "")
    return s.translate(table, string.punctuation)


class CreateCollocations():

    def __init__(self, read_files_path, save_file_path):
        self.words = []
        self.bigram_collocations_file = open(save_file_path + 'bigrams.txt', 'w')
        # self.trigram_collocations_file = open(save_file_path + 'trigrams.txt', 'w')

        print 'Started reading files...'
        for (read_files_path, names, file_names) in walk(read_files_path):
            for f_name in file_names:
                if '.txt' in f_name and '.okl' not in f_name:
                    self.read_files(read_files_path, f_name)

        print 'extracting collocations'
        # collocations.simple_bigram_collocations(self.bigram_collocations_file, self.words, 100, 1)
        collocations.simple_trigram_collocations(self.bigram_collocations_file, self.words, 100, 1)

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

run = CreateCollocations('/Users/arashsaidi/Work/LBK - prosjekt/lbk_22.04.14/TV/',
                   'collocations_2/test')