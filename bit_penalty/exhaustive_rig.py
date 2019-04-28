import sys
import itertools
import utils
import math

worst_penalty = None
best_penalty  = None

best_order    = None
worst_order   = None

num_best_order  = -2
num_worst_order = -2

def reset_bounds():
  global worst_penalty  , best_penalty
  global worst_order    , best_order
  global num_worst_order, num_best_order

  worst_penalty = None
  best_penalty  = None

  best_order    = None
  worst_order   = None

  num_best_order  = -2
  num_worst_order = -2

def bounds_decisioning(penalty, permutation):
  penalty_bounds_changed = False
  
  global worst_penalty  , best_penalty
  global worst_order    , best_order
  global num_worst_order, num_best_order

  if worst_penalty is None:
    worst_penalty = penalty
    best_penalty  = penalty
    best_order    = permutation
    worst_order   = permutation

    num_best_order  = 1
    num_worst_order = 1
    penalty_bounds_changed = True

  elif penalty > worst_penalty:
    worst_penalty   = penalty
    worst_order     = permutation
    num_worst_order = 1
    penalty_bounds_changed = True

  elif penalty < best_penalty:
    best_penalty   = penalty
    best_order     = permutation
    num_best_order = 1
    penalty_bounds_changed = True

  if penalty == best_penalty and not penalty_bounds_changed:
    num_best_order = num_best_order + 1

  if penalty == worst_penalty and not penalty_bounds_changed:
    num_worst_order = num_worst_order + 1

def interim_search_debug(i, num_permutations, permutation, penalty, step):
    progress = i*100/num_permutations
    
    if i % step == 0:
      print "Traversed through " + str(i) + " of " + str(num_permutations) + " permutations -- " + str(progress) + "% done"
      print str(permutation) + " has a penalty of " + str(penalty)

def final_search_debug():
  print "Best Combination Found with hamming weight " + str(best_penalty) + ". This occurred " + str(num_best_order) + "x times"
  print str(best_order)
  utils.calculate_total_penalty(best_order, "debug")

  print "Worst Combination Found with hamming weight " + str(worst_penalty) + ". This occurred " + str(num_worst_order) + "x times"
  print str(worst_order)
  utils.calculate_total_penalty(worst_order, "debug")

def search(size):
  list  = utils.generate_list(size)
  num_permutations = math.factorial(len(list))
  step             = math.floor(num_permutations/1000)

  if step == 0:
    step = 1

  permutations  = itertools.permutations(list)
  reset_bounds()

  i = 0

  for permutation in permutations:
    penalty = utils.calculate_total_penalty(permutation)
    bounds_decisioning(penalty, permutation)
    i = i + 1

    interim_search_debug(i, num_permutations, permutation, penalty, step)
    
  final_search_debug()

search(utils.grab_input())
