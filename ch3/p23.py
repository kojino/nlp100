# coding: utf-8
# ch2
filepath='hightemp.txt'
fp1='col1.txt'
fp2='col2.txt'

# 10
def count_line(filepath):
  file = open(filepath,'r')
  line_count = 0
  for row in file:
    line_count += 1
  return line_count
# print count_line(filepath)

# wc -l hightemp.txt -> 24

# 11
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

# 12
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

# separate_columns(filepath)

# cut -f 1 -d " " hightemp.txt > hightemp.txt
# cut -f 2 -d " " hightemp.txt > hightemp.txt

# 13
def merge_files(fp1,fp2):
  f1 = open(fp1,'r')
  f2 = open(fp2,'r')
  mfile = open('merge.txt','w')
  for l1,l2 in zip(f1,f2):
    mfile.write(l1.strip()+"\t"+l2)
merge_files(fp1,fp2)

# paste -d'\t' col12.txt col22.txt > merge2.txt

# 14
def