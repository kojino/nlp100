# 18

filepath = 'hightemp.txt'

def sort_col3(filepath):
  lines = open(filepath).readlines()
  sorted_lines = sorted(lines, key=lambda line: line.split()[2], reverse=True)
  sorted_file = open('hightemp_sorted.txt','w')
  sorted_file.writelines(sorted_lines)

sort_col3(filepath)

# sort -r -k 3 hightemp.txt