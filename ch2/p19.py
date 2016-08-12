# 19

filepath = 'hightemp.txt'

def sort_col1(filepath):
  file = open(filepath)
  counter = {}
  for line in file:
    first_el = line.split()[0]
    if first_el in counter:
      counter[first_el] += 1
    else:
      counter[first_el] = 1
  sorted_file = open('hightemp_sorted1.txt','w')
  for key in sorted(counter, key=counter.__getitem__, reverse=True):
    print counter[key],key

sort_col1(filepath)

# cut -f 1 -d " " hightemp.txt | sort | uniq -c | sort -r