# -*- coding: utf-8 -*-
# 20

import gzip
import json

filepath = 'jawiki-country.json'

def get_UK(filepath):
  file = open(filepath)
  uk_file = open('uk.txt','w')
  for line in file:
    content = json.loads(line)
    if content.get('title') == u"イギリス":
      uk_file.write(content.get('text').encode('utf-8'))

get_UK(filepath)