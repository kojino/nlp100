# -*- coding: utf-8 -*-
# p44

import p41
import p42
import graphviz as pgv
import sys

filepath = 'neko_cabocha.txt'


def sentenceToDot(sentence):
  dot = pgv.Digraph()
  for pair in sentence:
    dot.edge(pair[0].get_text().decode('utf-8'),pair[1].get_text().decode('utf-8'))
  filename = dot.render(filename='img/image')
  return dot

if len(sys.argv) != 2:
  raise ValueError("specify the value of n")
else:
  sentence = p41.create_Chunks(filepath)[int(sys.argv[1])]
  pairs = p42.make_chunk_pairs(sentence)
  dotString = sentenceToDot(pairs)