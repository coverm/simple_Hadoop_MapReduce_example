#!/usr/bin/env python
import sys

# new update


# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # make lower case
    line = line.lower()

    # split the line into words; splits on any whitespace
    words = line.split()

    # output tuples (word, 1) in tab-delimited format
    stopwords = set(['the', 'and','a','for','I','go','four','three','be','not','to','be','railings','or','not'])

    # notice the loop is different

    for word in words:
        if word not in stopwords:
         print '%s\t%s' % (word, "1")

