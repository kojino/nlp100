# 14
import sys
import p10

filepath = 'hightemp.txt'

def bottom_n(filepath,n):
  num_line = p10.count_line(filepath)
  file = open(filepath,'r')
  i = 0
  for line in file:
    if i >= num_line - n:
      print line.strip()
    i += 1
    if i == num_line:
      break

if len(sys.argv) != 2:
  raise ValueError("specify the value of n")
else:
  n = int(sys.argv[1])
  bottom_n(filepath,n)

# tail -10 hightemp.txt