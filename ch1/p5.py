# 5

def ngram(n,s,unit):
  if unit == "char":
    chars = s
    return ngram_char(n,s)
  elif unit == "word":
    words = s.replace(',','').split( )
    return ngram_word(n,words)
  else:
    raise ValueError('unit must be char or word')

def ngram_char(n,s):
  result = []
  for i in range(len(s)-n+1):
    result.append(s[i:i+n])
  return result

def ngram_word(n,words):
  result = []
  for i in range(len(words)-n+1):
    result.append(words[i:i+n])
  return result

# print ngram(2,"I am an NLPer","char")
# print ngram(2,"I am an NLPer","word")