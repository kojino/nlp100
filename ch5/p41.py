# -*- coding: utf-8 -*-
# 41

filepath = 'neko_cabocha.txt'
import p40

class Chunk():
  def __init__(self):
    self.morphs = []
    self.dst = -1
    self.srcs = []

  def add_morphs(self,morph):
    self.morphs.append(morph)

  def add_srcs(self,src):
    self.srcs.append(src)

  def print_morphs(self):
    for morph in self.morphs:
      morph.print_all()

  def get_text(self):
    text = ''
    for morph in self.morphs:
      text += morph.surface
    return text

  def get_text_list(self):
    text_list = []
    for morph in self.morphs:
      text_list.append(morph.surface)
    return text_list

  def get_pos(self):
    pos = []
    for morph in self.morphs:
      pos.append(morph.pos)
    return pos

  def first_verb(self):
    for morph in self.morphs:
      if morph.pos == '動詞':
        return morph



def create_Chunks(filepath):
  file = open(filepath,'r')
  text = []
  new_line = []
  for word in file:
    if "EOS" in word:
      for i in range(len(new_line)):
        if new_line[i].dst != -1:
          new_line[new_line[i].dst].add_srcs(i)
      text.append(new_line)
      new_line = []
    elif word.startswith('*'):
      chunk = Chunk()
      chunk.dst = int(word.split()[2].strip('D'))
      new_line.append(chunk)
    else:
      word_info = p40.Morph(surface = word.split('\t')[0],
                 base = word.split('\t')[1].split(',')[6],
                 pos = word.split('\t')[1].split(',')[0],
                 pos1 = word.split('\t')[1].split(',')[1])
      new_line[-1].add_morphs(word_info)
  return text

# for chunk in create_Chunks(filepath)[7]:
#   chunk.print_morphs()
#   print chunk.dst