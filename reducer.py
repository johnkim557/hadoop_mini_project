#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys


word2count={}
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    #line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
        word2count[word] = word2count.get(word, 0) + count

    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
sorted_word2count = sorted(word2count.items(), key=itemgetter(0))

for word, count in sorted_word2count:
    print('%s\t%s'% (word, count))
