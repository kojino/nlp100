# -*- coding: utf-8 -*-
# 33
import p30
filepath = 'neko_mecab.txt'

def get_sa_nouns(text):
  verb_file = open('neko_sa_nouns.txt','w')
  for line in text:
    for word in line:
      if word['pos'] == '名詞' and word['pos1'] == 'サ変接続':
        verb_file.write(word['surface']+'\n')


text = p30.read_mecab(filepath)
get_sa_nouns(text)