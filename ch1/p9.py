# 9

import random

def typoglycemia(s):
  words = s.split( )
  result = []
  for word in words:
    if len(word) <= 4:
      result.append(word)
    else:
      result.append(word[0]+''.join(random.sample(word[1:-1],len(word[1:-1])))+word[-1])
  return ' '.join(result)

# print typoglycemia("I couldn\'t believe that I could actually understand what I was reading : the phenomenal power of the human mind .")