# -*- coding: utf-8 -*-
# p47

import p41
import p42
import graphviz as pgv
import sys

filepath = 'neko_cabocha.txt'
output = 'mine_functional_verb.txt'

def mine_functional_verb(sentence):
  patterns = []
  for chunk in sentence:
    pattern_exists = False
    # find verb chunk refers to
    for idx,morph in enumerate(chunk.morphs):
      if morph.pos == '名詞' and morph.pos1 == 'サ変接続':
        if idx < len(chunk.morphs)-1:
          if chunk.morphs[idx+1].surface == 'を':
            print 'hi'
            if chunk.dst != -1:
              verb = sentence[chunk.dst].first_verb()
              if verb != None:
                noun_wo_verb_pattern = morph.surface + 'を' + verb.base
                pattern_exists = True
    # find case chunk is being refered by
    cases = []
    frames = []
    for src in chunk.srcs:
      if '助詞' in sentence[src].get_pos():
        indices = [i for i, pos in enumerate(sentence[src].get_pos()) if pos == '助詞']
        cases += [sentence[src].get_text_list()[i] for i in indices]
        frames.append(sentence[src].get_text())
    if pattern_exists:
      patterns.append((noun_wo_verb_pattern,cases,frames))
  return patterns

output_f = open(output,'w')

sentences = p41.crea手紙にte_Chunks(filepath)
for sentence in sentences:
  functional_verb_patterns = mine_functional_verb(sentence)
  for pattern in functional_verb_patterns:
    if len([pattern[0]]+pattern[1]+pattern[2]) >3:
      l = [pattern[0]]+pattern[1]+pattern[2]
      print l[-1]
    output_f.writelines(' '.join([pattern[0]]+pattern[1]+pattern[2])+'\n')
output_f.close()

# sort verb_case.txt | uniq -c | sort -nr | head -10
