--------------
INTRODUCTION
--------------
This is a tool for extracting video clips using codings made in ELAN. If you have done video coding in ELAN and would like to make video clips of, say, all the codings in a certain Tier, then this is the tool for you. The tool is pretty simple and inflexible right now, but you're welcome to add functionality or fork it to make your own custom version. 


--------------
GETTING READY
--------------
You will need a video and a file of ELAN codings. The ELAN file can *not* be in the .eaf format, but rather needs to be the tab-delimited text format that you can export from ELAN. To convert, just open your .eaf file in ELAN and go File -> Export As... -> Tab-Delimited Text file.

Right now the video must be of .m4v format. Someone should make this better.


--------------
COMMAND LINE WORKFLOW (paraphrased, not actual wording)
--------------
 0. Run the script: python make_video_clips_from_codings.py ./path/to/codings.txt ./path/to/video.m4v
 1. "Which tier name?" User> Hug_Type
 2. "That tier has XX occurrences in this video."
 3. "Which code for that tier? (or hit RETURN to get all codes)" User> Guest Over
 4. "That tier has XX occurrences for that code."
 5. <lists the codings you've selected>
 6. "Would you like to make video clips of these? (y/n)" User> y
 7. "Making videos..." 


