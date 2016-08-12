# 11

filepath = 'hightemp.txt'

def tab_to_space(filepath):
  new_file = []
  file = open(filepath,'r')
  for line in file:
    new_file.append(' '.join(line.split('\t')))
  file = open(filepath,'w')
  for line in new_file:
    file.write(line)

tab_to_space(filepath)

# TODO