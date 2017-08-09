--------------
AN EXAMPLE
--------------
Here is a full workflow from my (MatthewRueben's) computer; you can
see me (1) run the script with inputs called 4.txt and 4.m4v, (2)
choose the tier called "Age_Group", (3) choose the "Teenager" level of
that tier, and (4) say "y" (yes), I'd like to make clips from the 8
codings listed.


>>>>>>>> BEGIN: EXAMPLE FROM COMMAND LINE <<<<<<<<<<<<<

ruebenmlocal@johnson:~/Documents/elan-video-clipper$ python make_video_clips_from_codings.py ./test-inputs-elan-files/4.txt ./test-inputs-video/4.m4v
=====================================================
Which tier? Type the name as is it is ELAN: Age_Group
...
Found 85 codings with tier name Age_Group
Which level of that tier? Type the name as is it is ELAN, or press RETURN to get all levels: Teenager
...
Found 8 codings with level Teenager
---- Beginning of selected codings ----
['Age_Group', '00:02:21.980', '00:00:02.120', 'Teenager']
['Age_Group', '00:35:46.796', '00:00:04.685', 'Teenager']
['Age_Group', '00:40:26.469', '00:00:02.843', 'Teenager']
['Age_Group', '00:42:30.600', '00:00:02.085', 'Teenager']
['Age_Group', '01:00:09.771', '00:00:03.686', 'Teenager']
['Age_Group', '01:14:44.550', '00:00:05.345', 'Teenager']
['Age_Group', '01:15:49.254', '00:00:06.633', 'Teenager']
['Age_Group', '01:18:23.639', '00:00:04.978', 'Teenager']
---- End of selected codings ----
Do you want to make clips out of these codings? (y/n) y
Creating video clip at:  ./Age_Group.Teenager_000.m4v
... please wait --- video gremlins at work ...
Creating video clip at:  ./Age_Group.Teenager_001.m4v
... please wait --- video gremlins at work ...
Creating video clip at:  ./Age_Group.Teenager_002.m4v
... please wait --- video gremlins at work ...
Creating video clip at:  ./Age_Group.Teenager_003.m4v
... please wait --- video gremlins at work ...
Creating video clip at:  ./Age_Group.Teenager_004.m4v
... please wait --- video gremlins at work ...
Creating video clip at:  ./Age_Group.Teenager_005.m4v
... please wait --- video gremlins at work ...
Creating video clip at:  ./Age_Group.Teenager_006.m4v
... please wait --- video gremlins at work ...
Creating video clip at:  ./Age_Group.Teenager_007.m4v
... please wait --- video gremlins at work ...

ruebenmlocal@johnson:~/Documents/elan-video-clipper$

>>>>>>>> END: EXAMPLE FROM COMMAND LINE <<<<<<<<<<<<<
