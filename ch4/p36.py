# -*- coding: utf-8 -*-
# 36
import p30
import collections
filepath = 'neko_mecab.txt'

def get_frequent_words(text):
  words = []
  for line in text:
    for word in line:
      words.append(word['base'])
  return collections.Counter(words)


text = p30.read_mecab(filepath)
# print get_frequent_words(text)