# -*- coding: utf-8 -*-
# 34
import p30
filepath = 'neko_mecab.txt'

def get_a_no_b(text):
  verb_file = open('neko_a_no_b.txt','w')
  for line in text:
    for i in range(len(line)-2):
      if line[i]['pos'] == '名詞':
        if line[i+1]['surface'] == 'の' and line[i+2]['pos'] == '名詞':
          verb_file.write(line[i]['surface']+'の'+line[i+2]['surface']+'\n')

text = p30.read_mecab(filepath)
get_a_no_b(text)