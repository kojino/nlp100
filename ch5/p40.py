# 40

filepath = 'neko_cabocha.txt'

class Morph():
  def __init__(self, surface, base, pos, pos1):
    self.surface = surface
    self.base = base
    self.pos = pos
    self.pos1 = pos1

  def print_all(self):
    print self.surface, self.base, self.pos, self.pos1



def create_Morphs(filepath):
  file = open(filepath,'r')
  text = []
  new_line = []
  for word in file:
    if "EOS" in word:
      text.append(new_line)
      new_line = []
    elif word.startswith('*'):
      continue
    else:
      word_info = Morph(surface = word.split('\t')[0],
                 base = word.split('\t')[1].split(',')[6],
                 pos = word.split('\t')[1].split(',')[0],
                 pos1 = word.split('\t')[1].split(',')[1])
      new_line.append(word_info)
  return text

# for word in create_Morphs(filepath)[2]:
#   word.print_all()