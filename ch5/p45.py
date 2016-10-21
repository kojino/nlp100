# -*- coding: utf-8 -*-
# p45

import p41
import p42
import graphviz as pgv
import sys

filepath = 'neko_cabocha.txt'
output = 'verb_case.txt'

def extract_patterns(sentence):
  patterns = []
  for chunk in sentence:
    if '動詞' in chunk.get_pos():
      verb = chunk.morphs[chunk.get_pos().index('動詞')].base
      cases = []
      for src in chunk.srcs:
        if '助詞' in sentence[src].get_pos():
          indices = [i for i, pos in enumerate(sentence[src].get_pos()) if pos == '助詞']
          cases += [sentence[src].get_text_list()[i] for i in indices]
      patterns.append((verb,cases))
  return patterns

output_f = open(output,'w')

sentences = p41.create_Chunks(filepath)
for sentence in sentences:
  verb_case_patterns = extract_patterns(sentence)
  for pattern in verb_case_patterns:
    output_f.writelines(' '.join([pattern[0]]+pattern[1])+'\n')
output_f.close()

# sort verb_case.txt | uniq -c | sort -nr | head -10
# sort verb_case.txt | awk '{ if ($1=="する") print $0}' | uniq -c | sort -nr | head -10
# sort verb_case.txt | awk '{ if ($1=="見る") print $0}' | uniq -c | sort -nr | head -10
# sort verb_case.txt | awk '{ if ($1=="与える") print $0}' | uniq -c | sort -nr | head -10