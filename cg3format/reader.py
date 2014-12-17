#!/usr/bin/env python

import sys
import codecs
import re


# FIXME Will probably barf on larg files, make use of generators
def read_cg3(cg3_file, newline_eos=True):
    """Read a file containing CG3-formatted data.

Returns: a list of sentences of the following structure:
- Each sentence is itself a list containing information about each word.
- Each word is again a list of the form:
  [TOKEN, LEMMA, TAG0, TAG1, ...]
- TOKENS and LEMMAS are enclosed in double quotes.

    """
    rx_token = re.compile("^\"<(.+?)>\"$")
    rx_attributes = re.compile("^\s+\".+?\"\s+.+$")
    rx_eos = re.compile("^\s*$")

    curr_token = None
    curr_word = []
    curr_sentence = []
    result = []

    for line in cg3_file:

        if rx_token.match(line):
            curr_token = "\"%s\"" % rx_token.match(line).group(1)
            continue

        if rx_attributes.match(line):
            curr_word = line.split()
            if curr_token and curr_word:
                curr_sentence += [[curr_token] + curr_word]
                curr_token = None
                curr_word = []
                continue

        if rx_eos.match(line):
            result += [curr_sentence]
            curr_sentence = []
            curr_token = None
            curr_word = []
            continue

    # Final cleanup (in case of missing blank line or attributes at the end)
    if curr_token and curr_word:
        curr_sentence += [[curr_token] + curr_word]
        curr_token = None
        curr_word = []

    if curr_sentence:
        result += curr_sentence

    return result

###############################################################################
# HELPER FUNCTIONS FOR EXTRACTING ELEMENTS FROM PARSED CG3 DATA
###############################################################################

def _parsed_token(parsed_word):
    return parsed_word[0]


def _parsed_attribute_list(parsed_word):
    return parsed_word[1:]


def _parsed_lemma(parsed_word):
    return _parsed_attribute_list(parsed_word)[0]


def _parsed_tag_list(parsed_word):
    return _parsed_attribute_list(parsed_word)[1:]


def _parsed_tokens(parsed_sentence):
    return [_parsed_token(w) for w in parsed_sentence]


def _parsed_attributes(parsed_sentence):
    return [_parsed_attribute_list(w) for w in parsed_sentence]


def _parsed_lemmas(parsed_sentence):
    return [_parsed_lemma(w) for w in parsed_sentence]


def _parsed_tags(parsed_sentence):
    return [_parsed_tag_list(w) for w in parsed_sentence]


###############################################################################
# MAIN FUNCTIONS
###############################################################################

def tokens(parsed_cg3):
    """Return a list of tokens from the parsed cg3 data."""
    return [_parsed_tokens(s) for s in parsed_cg3]


def attributes(parsed_cg3):
    """Return a list of attributes (as a list) from the parsed cg3 data."""
    return [_parsed_attributes(s) for s in parsed_cg3]


def lemmas(parsed_cg3):
    """Return a list of lemmas from the parsed cg3 data."""
    return [_parsed_lemmas(s) for s in parsed_cg3]


def tags(parsed_cg3):
    """Return a list of tags (as a list) from the parsed cg3 data."""
    return [_parsed_tags(s) for s in parsed_cg3]


def print_tsv(parsed_cg3):
    """Print parsed cg3 as tab-separated lines.

Each sentence is separated by an empty line."""
    for sent in parsed_cg3:
        for w in sent:
            print "\t".join(w)
        print

def run(filename):
    parsed = parse_cg_format(codecs.open(filename, 'r', 'ISO-8859-1'))
    # print str(parsed[0][0])
    # print str(parsed_token(parsed[0][0]))
    # print str(parsed_attribute_list(parsed[0][0]))
    # print str(parsed_lemma(parsed[0][0]))
    # print str(parsed_tag_list(parsed[0][0]))

    # print str(parsed_tokens(parsed[0]))
    # print str(parsed_attributes(parsed[0]))
    # print str(parsed_lemmas(parsed[0]))
    # print str(parsed_tags(parsed[0]))

    print_tsv(parsed)

    # for s in tags(parsed):
    #     print [" ".join(t) for t in s]


if __name__ == "__main__":
    run(sys.argv[1])
