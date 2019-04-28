import utils
import itertools

def fill_vectors_reusable(series):
  return list(itertools.permutations(series, 2))

def fill_vector_penalties(vectors):
  vector_penalties = {}

  for vector in vectors:
    vector_penalties[vector] = utils.calculate_individual_penalty(vector[0], vector[1])

  return vector_penalties

def fill_vector_navigator(vectors):
  navigator = {}
  for vector in vectors:
    
    source      = vector[0]
    destination = vector[1]

    if source not in navigator:
      navigator[source] = [destination]
    else:
      navigator[source].append(destination)

  return navigator

def search(size):
  series    = utils.generate_series(size)
  vectors   = fill_vectors_reusable(series)
  penalties = fill_vector_penalties(vectors)
  navigator = fill_vector_navigator(vectors)

  best_orders  = navigate_all_sources(penalties, navigator, min)
  worst_orders = navigate_all_sources(penalties, navigator, max)


  print "The best orders are...."
  print str(best_orders)
  for start_node in best_orders:
    order = best_orders[start_node]
    utils.calculate_total_penalty(order ,"debug")

  print "The worst orders are...."
  print str(worst_orders)
  for start_node in worst_orders:
    order = worst_orders[start_node]
    utils.calculate_total_penalty(order ,"debug")

def navigate_all_sources(penalties, navigator, comparator):
  paths = {}

  for source in navigator:
    paths[source] = navigate_recursive(penalties, navigator, comparator, source, [])

  return paths

def navigate_recursive(penalties, navigator, comparator, source , existing_path):

  if len(existing_path) == 0:
    existing_path = [source]

  destinations        = navigator[source]
  available_penalties = []
  next_destination    = None

  for destination in destinations:
    current_penalty    = penalties[(source,destination)]
    possible_penalties = available_penalties[:]
    possible_penalties.append(current_penalty)

    direction_nominal  = comparator(possible_penalties) == current_penalty
    already_visited    = destination in existing_path

    if direction_nominal and not already_visited:
      available_penalties.append(current_penalty)
      next_destination = destination

  if next_destination is not None: 
    existing_path.append(next_destination)
    return navigate_recursive(penalties, navigator, comparator, next_destination, existing_path)
  else:
    return existing_path

search(utils.grab_input())
