# -*- coding: utf-8 -*-
# 42

filepath = 'neko_cabocha.txt'
import p41

def make_chunk_pairs(chunks):
  pairs = []
  for chunk in chunks:
    if chunk.dst != -1:
      # （かかり元、かかり先）
      pairs.append((chunk,chunks[chunk.dst]))
  return pairs

def display_dst_src(text):
  sentences_in_chunk_pairs = []
  for sentence in text:
    setence_in_chunk_pairs = make_chunk_pairs(sentence)
    sentences_in_chunk_pairs.append(setence_in_chunk_pairs)
  return sentences_in_chunk_pairs


# for sentence_in_chunk_pairs in display_dst_src(p41.create_Chunks(filepath)):
#     for chunk_pairs in sentence_in_chunk_pairs:
#       print (chunk_pairs[0].get_text()+"\t"+chunk_pairs[1].get_text()).strip('。').strip('、')
