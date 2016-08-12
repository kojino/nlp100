# 12

filepath = 'hightemp.txt'

def separate_columns(filepath):
  col1 = []
  col2 = []
  file = open(filepath,'r')
  for line in file:
    line=line.split()
    col1.append(line[0])
    col2.append(line[1])
  col1file = open('col1.txt','w')
  for line in col1:
    col1file.write(line+"\n")
  col2file = open('col2.txt','w')
  for line in col2:
    col2file.write(line+"\n")

separate_columns(filepath)

# cut -f 1 -d " " hightemp.txt > hightemp.txt
# cut -f 2 -d " " hightemp.txt > hightemp.txt