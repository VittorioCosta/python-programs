##
#   This program reads a sequence of die toss values and prints how many times
#   each value occurred.
#
import random

def main() :
   counters = countInputs(6)
   printCounters(counters)
   
## Reads a sequence of die toss values between 1 and sides (inclusive) 
#  and counts how frequently each of them occurs.
#  @param sides the die's number of sides 
#  @return a list whose ith element contains the number of times the value i
#  occurred in the input. The 0 element is unused.
#


def countInputs(sides) :
   counters = [0] * (sides + 1)   # counters[0] is not used.

   
   for i in range(100):
      value = random.randint(1,6)
      
      # Increment the counter for the input value.
      if value >= 1 and value <= sides :
         counters[value] = counters[value] + 1
      
   
      
      
         
   return counters

## Prints a table of die value counters.
#  @param counters a list of counters. counters[0] is not printed.
#
def printCounters(counters) :
   for i in range(1, len(counters)) :
      print("%2d: %4d" % (i, counters[i]))

   
# Start the program.
main()

