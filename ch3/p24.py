# -*- coding: utf-8 -*-
# 24

import re
import p20
filepath = 'uk.txt'

def extract_ref(filepath):
  text = open('uk.txt','r')
  categories = open('uk_ref.txt','w')
  for line in text:
    match = re.search(r'(File|ファイル):(.+\.[a-zA-Z0-9]+)\|', line)
    if match:
      categories.write(match.group(2)+'\n')

extract_ref(filepath)