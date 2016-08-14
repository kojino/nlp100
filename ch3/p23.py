# -*- coding: utf-8 -*-
# 23

import re
import p20
filepath = 'uk.txt'

def extract_category_name(filepath):
  text = open('uk.txt','r')
  categories = open('uk_category_hierarchy.txt','w')
  for line in text:
    match = re.search(r'=(=+)(.+)=', line)
    if match:
      categories.write(str(len(match.group(1)))+" "+match.group(2)[:-len(match.group(1))]+'\n')

extract_category_name(filepath)