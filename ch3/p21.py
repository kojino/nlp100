# -*- coding: utf-8 -*-
# 21

import re
import p20

filepath = 'uk.txt'

def extract_category(filepath):
  text = open(filepath,'r')
  categories = open('uk_categories.txt','w')
  for line in text:
    match = re.search(r'\[\[Category:.+\]\]', line)
    if match:
      categories.write(line)

extract_category(filepath)