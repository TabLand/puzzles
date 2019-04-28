Catch all for random math puzzles

-> Bit Penalty
   For consecutive numbers 0..n, how do we find the best and worst sort order?
   Where the best sort order is defined as the least number of digits changed in base m.
   Assuming base m = 2 (binary) for this exercise, but could be attempted with a different base.

   Inspired by component service stop / start combination testing.

   Vanilla:
     The cost of a bit toggle is the same for switching on vs switching off. I.e service stops / starts take the same amount of time and resources.

   Ginger:
     The cost of a bit toggle is different for switching on vs switching off. I.e a service stop may be quicker / slower / easier / harder than a service start.

   Canon:
     Penalties are calculated in one direction from 2nd element to the last. The first penalty is between the 1st and 2nd element i.e n-1 penalties.

   Wild Goose:
     Penalties are calculated in a circular fashion. The first penalty will be between the last and first element i.e n penalties.
     
