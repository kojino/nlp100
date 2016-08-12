# 14
import sys
import p10

filepath = 'hightemp.txt'

def top_n(filepath,n):
  file = open(filepath,'r')
  i = 0
  for line in file:
    print line.strip()
    i += 1
    if i == n:
      break

if len(sys.argv) != 2:
  raise ValueError("specify the value of n")
else:
  n = int(sys.argv[1])
  top_n(filepath,n)

# head -10 hightemp.txt