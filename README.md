spellcheck
==========

Twitch.tv Programming Challenge

wordgen.py appends ~/Downloads to the system path in order to call the functions in spellcheck.py.  It's rather uninteresting to watch, however, because it only displays any behavior if there is an error or you allow it to finish testing mutations of every entry in the dictionary.

In my implementation, correct dictionary words are stored in a Python set, so look ups for correctly spelled words should be O(1) on average (with O(n) worst case).    

Lookups for an incorrectly spelled word W:

If v = # vowels in W
   k = length of W
   r = # of letters in W belonging to a consecutive repeated sequence of the same letter, minus the first in each     sequence (i.e. for  rrabbitttt r=5).
   
   
