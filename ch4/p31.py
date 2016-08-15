# -*- coding: utf-8 -*-
# 31
import p30
filepath = 'neko_mecab.txt'

def get_verbs_surface(text):
  verb_file = open('neko_verbs_surface.txt','w')
  for line in text:
    for word in line:
      if word['pos'] == '動詞':
        verb_file.write(word['surface']+'\n')


text = p30.read_mecab(filepath)
get_verbs_surface(text)