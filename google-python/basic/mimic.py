#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import random
import sys


def mimic_dict(filename):
  """Returns mimic dict mapping each word to list of words which follow it."""
  # +++your code here+++
  mimicDict = {}
  allwords = []

  f = open(filename,'rU')
  for line in f:
    words = line.split()
    for word in words:
      allwords.append(word)
  print len(allwords)

  for i in range(len(allwords)-1):
    if allwords[i] in mimicDict.keys():
      # print words[i],'---yes, already has key'

      if allwords[i+1] not in mimicDict[allwords[i]]:
        mimicDict[allwords[i]].append(allwords[i+1])
        # print allwords[i+1],'next word add','all->',mimicDict[allwords[i]]
    else:
        mimicDict[allwords[i]] = [allwords[i+1]]

  # print 'all keys --->',sorted(mimicDict.keys())
  return mimicDict
 
def print_mimic(mimic_dict, word):
  """Given mimic dict and start word, prints 200 random words."""
  # # +++your code here+++
  # for key in mimic_dict.keys():
  #   print key,mimic_dict[key]
  newarticle=[]
  if word == '' : word = 'Alice'
  if word not in mimic_dict.keys(): 
    print 'not used in this article, please select other word'
    sys.exit()
  newarticle.append(word)

  for ct in range(200):
    
    nextword = mimic_dict[word][random.randint(0,len(mimic_dict[word])-1)]
    # print ct,'nextword is ===> ',nextword,'total length =>',len(mimic_dict[word]),'random => ',random.randint(0,len(mimic_dict[word])-1)
    newarticle.append(nextword)
    word = nextword
    ct +=1
    print ct,nextword

  print ' '.join(newarticle)

  return


# Provided main(), calls mimic_dict() and mimic()
def main():
  if len(sys.argv) < 2:
    print 'usage: ./mimic.py file-to-read word'
    sys.exit(1)

  dict = mimic_dict(sys.argv[1])
  word = 'Alice'
  if len(sys.argv) == 3: word = sys.argv[2]

  print_mimic(dict, word)


if __name__ == '__main__':
  main()
