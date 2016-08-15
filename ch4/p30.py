import MeCab

filepath = 'neko_mecab.txt'

def read_mecab(filepath):
  file = open(filepath,'r')
  text = []
  new_line = []
  for word in file:
    if 'EOS' in word:
      text.append(new_line)
      new_line = []
      continue
    word_info = {'surface': word.split('\t')[0],
                 'base': word.split('\t')[1].split(',')[6],
                 'pos': word.split('\t')[1].split(',')[0],
                 'pos1': word.split('\t')[1].split(',')[1]}
    new_line.append(word_info)
  return text


# read_mecab(filepath)
