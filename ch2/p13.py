# 13

filepath = 'hightemp.txt'
fp1 = 'col1.txt'
fp2 = 'col2.txt'

def merge_files(fp1,fp2):
  f1 = open(fp1,'r')
  f2 = open(fp2,'r')
  mfile = open('merge.txt','w')
  for l1,l2 in zip(f1,f2):
    mfile.write(l1.strip()+"\t"+l2)

merge_files(fp1,fp2)

# paste -d'\t' col12.txt col22.txt > merge2.txt
