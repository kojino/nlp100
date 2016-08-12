# 6

import p5

def set_info(X,Y):
  return {'union': X|Y, 'intersection': X&Y, 'diff':X-Y}

print set_info(set(p5.ngram(2,"paraparaparadise","char")),set(p5.ngram(2,"paragraph","char")))
