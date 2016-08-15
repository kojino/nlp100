# -*- coding: utf-8 -*-
# 35
import p30
filepath = 'neko_mecab.txt'

def get_repeated_noun(text):
  longest = []
  current = []
  for line in text:
    for word in line:
      if word['pos'] == '名詞':
        current.append(word['surface'])
      else:
        if len(current) > len(longest):
          longest = current
        current = []
  return longest


text = p30.read_mecab(filepath)
print get_repeated_noun(text)