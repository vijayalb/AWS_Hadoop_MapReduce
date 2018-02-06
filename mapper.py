#!/usr/bin/env python
"""A more advanced Mapper, using Python iterators and generators."""

import sys

for words in sys.stdin:
    	words = words.strip()
    	words = words.split(',')
	if len(words)>0:
            print '%s\t%s\t%s' % (words[3],words[6], 1)
