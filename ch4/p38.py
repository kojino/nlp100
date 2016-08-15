# -*- coding: utf-8 -*-
# 38

import p30
import p36
import matplotlib.pyplot as plt
filepath = 'neko_mecab.txt'

def plot_word_hist(words):
  D = {}
  for word in words:
    if not words[word] in D:
      D[words[word]] = 1
    else:
      D[words[word]] += 1
  plt.bar(range(len(D)), D.values(), align='center')
  plt.xticks(range(len(D)), D.keys())
  plt.show()

text = p30.read_mecab(filepath)
plot_word_hist(p36.get_frequent_words(text))