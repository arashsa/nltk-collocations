#!/usr/bin/env python

import sys
import codecs
from cg3format.reader import read_cg3, print_tsv


def run(filename):
    cg3_data = read_cg3(codecs.open(filename, 'r', 'ISO-8859-1'))
    # print str(cg3_data[0][0])
    # print str(cg3_data_token(cg3_data[0][0]))
    # print str(cg3_data_attribute_list(cg3_data[0][0]))
    # print str(cg3_data_lemma(cg3_data[0][0]))
    # print str(cg3_data_tag_list(cg3_data[0][0]))
    # print str(cg3_data_tokens(cg3_data[0]))
    # print str(cg3_data_attributes(cg3_data[0]))
    # print str(cg3_data_lemmas(cg3_data[0]))
    # print str(cg3_data_tags(cg3_data[0]))
    print_tsv(cg3_data)

if __name__ == "__main__":
    run(sys.argv[1])
