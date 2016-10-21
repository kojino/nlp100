# -*- coding: utf-8 -*-
# p46

import p41
import p42
import graphviz as pgv
import sys

filepath = 'neko_cabocha.txt'
output = 'verb_case_frame.txt'

def extract_patterns_get_frame(sentence):
  patterns = []
  for chunk in sentence:
    if '動詞' in chunk.get_pos():
      verb = chunk.morphs[chunk.get_pos().index('動詞')].base
      cases = []
      frames = []
      for src in chunk.srcs:
        if '助詞' in sentence[src].get_pos():
          indices = [i for i, pos in enumerate(sentence[src].get_pos()) if pos == '助詞']
          cases += [sentence[src].get_text_list()[i] for i in indices]
          frames.append(sentence[src].get_text())
      patterns.append((verb,cases,frames))
  return patterns

output_f = open(output,'w')

sentences = p41.create_Chunks(filepath)
for sentence in sentences:
  verb_case_patterns = extract_patterns_get_frame(sentence)
  for pattern in verb_case_patterns:
    output_f.writelines(' '.join([pattern[0]]+pattern[1]+pattern[2])+'\n')
output_f.close()

# sort verb_case.txt | uniq -c | sort -nr | head -10
