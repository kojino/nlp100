# -*- coding: utf-8 -*-
# 38

import p30
import p36
import matplotlib.pyplot as plt
filepath = 'neko_mecab.txt'

def plot_log(words):
  D = {}
  rank = []
  for word in words:
    rank.append(words[word])
  rank = sorted(rank, reverse=True)
  plt.xscale('log')
  plt.yscale('log')
  plt.bar(range(len(rank)), rank, align='center')
  plt.xticks(range(len(rank)), range(len(rank)))
  plt.show()

text = p30.read_mecab(filepath)
plot_log(p36.get_frequent_words(text))