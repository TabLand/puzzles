import math

base        = 2
bits_needed = 4

def convert_to_binary( number ):
  return "{0:b}".format( number ).zfill( bits_needed )

def generate_list( size ):
  bits_needed = math.ceil( math.log( size, base) )
  return list( range( size ) )

def debug_in_binary(list):

  previous = None

  print "Item\tBin\tDiff\tPenalty"

  for current in list:
    binary        = convert_to_binary( current )
    penalty       = calculate_individual_penalty(previous, current)
    debug_penalty = calculate_individual_penalty(previous, current, True)

    print str(current) + "\t" + str(binary)  + "\t" + str(debug_penalty) + "\t" + str(penalty)
    previous = current

def calculate_individual_penalty( first, second, verbose = False):
  differing_bits = 0
  if first is not None:
        differing_bits = first ^ second
  if verbose:
    final = convert_to_binary( differing_bits )
  else:
    final = hamming_weight( differing_bits )
  
  return final

def hamming_weight( differing_bits ):
  count = 0
  
  while( differing_bits ):
      differing_bits &= ( differing_bits - 1)
      count += 1

  return count
