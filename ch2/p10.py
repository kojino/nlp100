# 10

filepath='hightemp.txt'

def count_line(filepath):
  file = open(filepath,'r')
  line_count = 0
  for row in file:
    line_count += 1
  return line_count

# print count_line(filepath)

# wc -l hightemp.txt