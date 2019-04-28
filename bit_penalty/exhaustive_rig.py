import sys
import itertools
import utils
import math

def search(size):
  list  = utils.generate_list(size)
  search_recursive(list)

def search_recursive( list ):
  num_combinations = math.factorial(len(list))

  combinations  = itertools.permutations(list)
  worst_penalty = None
  best_penalty  = None

  best_combo    = None
  worst_combo   = None


  i = 0

  for combination in combinations:
    print str(combination)
    penalty = utils.calculate_total_penalty(combination)

    if worst_penalty is None:
      worst_penalty = penalty
      best_penalty  = penalty
      best_combo    = combination
      worst_combo   = combination

    if penalty > worst_penalty:
      worst_penalty = penalty
      worst_combo   = combination

    if penalty < best_penalty:
      best_penalty  = penalty
      best_combo    = combination
  
    i = i + 1

    print "Traversed through " + str(i) + " of " + str(num_combinations) + " combinations"
    

  print "Best Combination Found with hamming weight " + str(best_penalty)
  print str(best_combo)
  utils.calculate_total_penalty(best_combo, "debug")

  print "Worst Combination Found with hamming weight " + str(worst_penalty)
  print str(worst_combo)
  utils.calculate_total_penalty(worst_combo, "debug")

if len(sys.argv) == 2:
  size = int(sys.argv[1])
  print "Will be searching bit penalties up to " + str(size)
  search(size)

else:
  print "Please provide a number to search bit penalties up to as an argument..."
  exit(1)

