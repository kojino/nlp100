# -*- coding: utf-8 -*-
# 17

filepath = 'hightemp.txt'

def unique_el(filepath):
  file = open(filepath,'r')
  els = []
  for line in file:
    line=line.split()
    if not (line[0] in els):
      print line[0]
    els.append(line[0])

unique_el(filepath)

# sort col1.txt | uniq