# -*- coding: utf-8 -*-
# 37
import p30
import p36
import matplotlib.pyplot as plt
filepath = 'neko_mecab.txt'

def plot_words(words):
  dictionary = plt.figure()
  plt.bar(range(len(words)), [word[1] for word in words], align='center')
  plt.xticks(range(len(words)), [word[0].decode('utf-8') for word in words])
  plt.show()

text = p30.read_mecab(filepath)
plot_words(p36.get_frequent_words(text).most_common(10))

