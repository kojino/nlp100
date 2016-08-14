# -*- coding: utf-8 -*-
# 25

import re
filepath = 'uk.txt'

def extract_template(filepath,func=None):
  file = open(filepath,'r')
  result = {}
  in_template = False
  for line in file:
    if re.search(r'\{\{基礎情報(.*)', line):
      in_template = True
      continue
    if re.search(r'^\}\}$', line):
      if in_template:
        break
    match = re.search(r'\|(.+) = (.+)', line)
    if match:
      info = match.group(2)
      if func != None:
        info = func(info)
      result[match.group(1)] = info
  for key in result:
    print key,result[key]

print extract_template(filepath)