#!/usr/bin/env python

# OUTLINE:
# 1. Script can get entry for each coding in a hard-coded tier.
# 2. Can pull out just the start and end times for each coding.
# 3. The tier name can now be user-specified.
# 7. Convert start and end times from ELAN to format for commanding the video clipping script.

# USE FLOW:
#  1. "Which tier name?" User> Hug_Type
#  2. "That tier has XX occurences in this video."
#  3. "Would you like to make video clips of all of them? (y/n)" User> y
#  4. "Making videos..." 

import sys
import csv


if __name__ == "__main__":

    print '====================================================='

    # Check that input file was given as command line argument
    if len(sys.argv) is not 2:
        print 'Use: python get_coding_times.py ./path/to/your/file.txt'
        print 'ERROR: no input file.'
        print 'Script over.'
        print 'Goodbye.'
        print ''
        sys.exit()

    # Import ELAN codings
    path = sys.argv[1]  # get path from command-line argument
    with open(path) as f:
        reader = csv.reader(f, delimiter = '\t')
        codings_all = list(reader)

    # Find all codings of a certain tier
    tier_chosen = raw_input('Which tier? Type the name as is it is ELAN: ')
    print '...'
    codings_chosen = [coding for coding in codings_all
                      if coding[0] == tier_chosen]
    print 'Found ' + str(len(codings_chosen)) + ' codings with tier name ' + tier_chosen

    for coding in codings_chosen:
        print [coding[i] for i in [0,2,5]]  # this is clunky with python lists
    

