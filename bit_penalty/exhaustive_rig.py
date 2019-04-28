import sys
import itertools
import utils
import math

def search(size):
  list  = utils.generate_list(size)
  search_recursive(list)

def search_recursive( list ):
  num_combinations = math.factorial(len(list))
  step             = math.floor(num_combinations/100)

  if step == 0:
    step = 1

  combinations  = itertools.permutations(list)
  worst_penalty = None
  best_penalty  = None

  best_combo    = None
  worst_combo   = None

  num_best_combo  = -2
  num_worst_combo = -2

  i = 0

  for combination in combinations:
    penalty = utils.calculate_total_penalty(combination)

    if worst_penalty is None:
      worst_penalty = penalty
      best_penalty  = penalty
      best_combo    = combination
      worst_combo   = combination

      num_best_combo  = 1
      num_worst_combo = 1

    elif penalty > worst_penalty:
      worst_penalty   = penalty
      worst_combo     = combination
      num_worst_combo = 1

    elif penalty < best_penalty:
      best_penalty   = penalty
      best_combo     = combination
      num_best_combo = 1
  
    elif penalty == best_penalty:
      num_best_combo = num_best_combo + 1

    elif penalty == worst_penalty:
      num_worst_combo = num_worst_combo + 1

    i = i + 1
    progress = i*100/num_combinations
    
    if i % step == 0:
     print "Traversed through " + str(i) + " of " + str(num_combinations) + " combinations -- " + str(progress) + "% done"
    

  print "Best Combination Found with hamming weight " + str(best_penalty) + ". This occurred " + str(num_best_combo) + "x times"
  print str(best_combo)
  utils.calculate_total_penalty(best_combo, "debug")

  print "Worst Combination Found with hamming weight " + str(worst_penalty) + ". This occurred " + str(num_worst_combo) + "x times"
  print str(worst_combo)
  utils.calculate_total_penalty(worst_combo, "debug")

if len(sys.argv) == 2:
  size = int(sys.argv[1])
  print "Will be searching bit penalties up to " + str(size)
  search(size)

else:
  print "Please provide a number to search bit penalties up to as an argument..."
  exit(1)

