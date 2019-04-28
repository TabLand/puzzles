import sys,itertools,utils

def search(size):
  list  = utils.generate_list(size)
  search_recursive(list)

def search_recursive( list ):
  combinations = itertools.permutations(list)
  for combination in combinations:
    utils.calculate_total_penalty(combination, "debug")


if len(sys.argv) == 2:
  size = int(sys.argv[1])
  print "Will be searching bit penalties up to " + str(size)
  search(size)

else:
  print "Please provide a number to search bit penalties up to as an argument..."
  exit(1)

