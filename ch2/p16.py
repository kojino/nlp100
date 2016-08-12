# 16

import sys
import math
import p10

filepath = 'hightemp.txt'

def split(filepath,n):
  file = open(filepath,'r')
  line_count = 0
  for line in file:
    path = 'split_%d.txt' % (line_count % n)
    split_file = open(path,'a')
    split_file.write(line)
    line_count += 1

if len(sys.argv) != 2:
  raise ValueError("specify the value of n")
else:
  n = int(sys.argv[1])
  split(filepath,n)

# split -n 10 hightemp.txt