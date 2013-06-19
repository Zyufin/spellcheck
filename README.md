spellcheck
==========

Programming Challenge


wordgen.py appends ~/Downloads to the system path in order to call the functions in spellcheck.py.  It's rather uninteresting to watch, however, because it only displays any behavior if there is an error or you allow it to finish testing mutations of every entry in the dictionary.

In my implementation, correct dictionary words are stored in a Python set, so look ups for correctly spelled words should be O(1) on average (with O(n) worst case).    

Worst case lookups for an incorrectly spelled word W:

If v = # vowels in W
   w = length of W
   r = # of letters in W belonging to a consecutive repeated sequence of the same letter, minus the first in each     sequence (i.e. for  rrabbitttt r=5).
   
      Breakdown by function:
         vowel_variants:  w + w + 7 + w + w + 7 + v + 7**v + w + 4(7**v)v ~= O(7**v)
         .
         .
         .
         More analysis was planned.
         
         
         
         
         
         
         
   Most importantly, the lookups for incorrect words are exponential with respect to v and r. 
   However, this should not be a problem for the user unless he/she is grossly incompetent at spelling (or he/she is a 
   cat napping on the keyboard) (asfjoasfjoasfjoasfjoasfjoasfjoasfjoasfjoasfjoasfjoasfjoasfjoasfjoasfjoasfjoasfjoasfjo
   asfjoasfjoasfjoasfjoasfjoasfjoasfjoasfjoasfjoasfjoasfjoasfjoasfjo)
   
   An exponential time complexity in such a situation does not represent real problems for the user, but it does
   present a risk for having your clock cycles eaten up by malicious cats, er, users.
