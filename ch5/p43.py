# -*- coding: utf-8 -*-
# 43

filepath = 'neko_cabocha.txt'
import p41

def display_nv_relationship(text):
  for chunks in text:
    for i in range(len(chunks)):
      if '名詞' in chunks[i].get_pos():
        if '動詞' in chunks[chunks[i].dst].get_pos():
          print (chunks[i].get_text()+'\t'+chunks[chunks[i].dst].get_text()).replace('、','').replace('。','')

# display_nv_relationship(p41.create_Chunks(filepath))

