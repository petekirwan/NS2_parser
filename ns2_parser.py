#credit to https://pythonexamples.org/python-count-occurrences-of-word-in-text-file/ from which this is adapted. I've mainly just added the use of regex and len

#credit also to https://stackoverflow.com/questions/3895646/number-of-regex-matches for idea of using len to count the regex

import sys
import re

#get file object reference to the file
file = open(sys.argv[1], "r")

#read content of file to string
data = file.read()

#uses regex to parse the file for 
cbrre = re.findall("\n-.*cbr", data)
cbrsent = len(cbrre)
droppedre = re.findall("\nd.", data)
dropped = len(droppedre)
cbrreceivedre = re.findall("\nr.*cbr", data)
cbrreceived = len(cbrreceivedre)
hops = data.count("h")
collisionsre = re.findall("\nc.", data)
collisions = len(collisionsre)
dvroutingoverheadre = re.findall("\n-.*rtProtoDV", data)
dvroutingoverhead = len(dvroutingoverheadre)
lsroutingoverheadre = re.findall("\n-.*rtProtoLS", data)
lsroutingoverhead = len(lsroutingoverheadre)

print('this many were cbr sent:', cbrsent)
print('this many were received:', cbrreceived)
print('this many were dropped:', dropped)
print('there were this many hops:', hops)
print('there were this many collisions:', collisions)
print('there were this many rtProtoDV sent:', dvroutingoverhead)
print('there were this many rtProtoLS sent:', lsroutingoverhead)

file.close()
