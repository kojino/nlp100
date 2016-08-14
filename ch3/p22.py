# -*- coding: utf-8 -*-
# 22

import re
import p20

filepath = 'uk.txt'

def extract_category_name(filepath):
  text = open(filepath,'r')
  categories = open('uk_category_names.txt','w')
  for line in text:
    match = re.search(r'\[\[Category:(.+)\]\]', line)
    if match:
      categories.write(match.group(1)+'\n')

extract_category_name(filepath)