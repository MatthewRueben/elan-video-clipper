#!/usr/bin/env python

# COMMAND LINE WORKFLOW (paraphrased, not actual wording):
# 0. Run the script: python make_video_clips_from_codings.py ./path/to/codings.txt ./path/to/video.m4v
# 1. "Which tier name?" User> Hug_Type
# 2. "That tier has XX occurrences in this video."
# 3. "Which code for that tier? (or hit RETURN to get all codes)" User> Guest Over
# 4. "That tier has XX occurrences for that code."
# 5. <lists the codings you've selected>
# 6. "Would you like to make video clips of these? (y/n)" User> y
# 7. "Making videos..." 

import sys
import csv
import subprocess


if __name__ == "__main__":

    print '====================================================='

    # Check that input file was given as command line argument
    if len(sys.argv) is not 3:
        print 'Use: python get_coding_times.py ./path/to/your/file.txt ./path/to/your/video.{video extension}'
        print 'ERROR: wrong number of command line arguments.'
        print 'Script over.'
        print 'Goodbye.'
        print ''
        sys.exit()

    # Import ELAN codings
    path_input_text = sys.argv[1]  # get path from command-line argument
    with open(path_input_text) as f:
        reader = csv.reader(f, delimiter = '\t')
        codings_all = list(reader)
        
    # Find all codings of a certain tier
    tier_chosen = raw_input('Which tier? Type the name as is it is ELAN: ')
    print '...'
    codings_by_tier = [coding for coding in codings_all
                       if coding[0] == tier_chosen]
    print 'Found ' + str(len(codings_by_tier)) + ' codings with tier name ' + tier_chosen

    # Find all codings of a certain level
    level_chosen = raw_input('Which level of that tier? Type the name as is it is ELAN, or press RETURN to get all levels: ')
    print '...'
    if level_chosen == '':  # if they just pressed RETURN...
        codings_by_level = codings_by_tier  # ...give them all codings in that tier.
        print 'OK, here are all the codings for that tier name.'
    else:
        codings_by_level = [coding for coding in codings_by_tier
                            if coding[-1] == level_chosen]
        print 'Found ' + str(len(codings_by_level)) + ' codings with level ' + level_chosen

    # Print out all the codings that have been selected.
    print '---- Beginning of selected codings ----'
    for coding in codings_by_level:
        print [coding[i] for i in [0,2,8,-1]]  # this is clunky with python lists
    print '---- End of selected codings ----'


    # Ask if user wants to make video clips out of these. 
    want_to_make_clips = raw_input('Do you want to make clips out of these codings? (y/n) ')
    if want_to_make_clips != 'y':
        print 'OK, I won\'t make you any clips. You have your reward.'
        print 'Script over.'
        print 'Goodbye.'
        print ''
        sys.exit()

    # Call avconv
    path_input_video = sys.argv[2]
    for clip_number, coding in enumerate(codings_by_level):
        clip_number = '00' + str(clip_number); clip_number = clip_number[-3:]  # makes the clip number three digits, left-padded by zeros
        if level_chosen == '':
            level_chosen = 'All'
        path_output_clip = './' + tier_chosen + '.' + level_chosen + '_' + clip_number + '.m4v'
        command = [
            'avconv',
            '-i',
            path_input_video,
            '-ss',
            coding[2],
            '-t',
            coding[8],
            '-loglevel', 'quiet',
            path_output_clip
        ]
        print 'Creating video clip at: ', path_output_clip
        print ' ... please wait --- video gremlins at work ... '
        subprocess.call(command)
    
