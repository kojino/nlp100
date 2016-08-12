# ch1

# 0
def reverse_string(s):
  return s[::-1]
# print reverse_string("stressed")

# 1
def get_odd(s):
  return s[::2]
# print get_odd("njiocbe!")

# 2
def merge_strings(s1,s2):
  i = 0
  j = 0
  result = ""
  while i < len(s1) and j < len(s2):
    result+=s1[i]+s2[j]
    i+=1
    j+=1
  if i>0:
    result+=s1[i:]
  if j>0:
    result+=s2[j:]
  return result
# print merge_strings("nice","job!")

# 3
def pi(s):
  result = []
  words = s.replace(',','').split( )
  for word in words:
    result.append(len(word))
  return result
# print pi("Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.")

# 4
def elements(s):
  result = {}
  words = s.replace(',','').split( )
  get_one = [1, 5, 6, 7, 8, 9, 15, 16, 19]
  for i in range(len(words)):
    k = 1 if i + 1 in get_one else 2
    result[words[i][:k]] = i+1
  return result
# ,print elements("Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.")

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

# 6
def set_info(X,Y):
  return {'union': X|Y, 'intersection': X&Y, 'diff':X-Y}
# print set_info(set(ngram(2,"paraparaparadise","char")),set(ngram(2,"paragraph","char")))

# 7
def template(x,y,z):
  return "The " + str(y) + " at " + str(x) + " is " + str(z) + "."

# print template(12,"temparature",22.4)

# 8
def cipher(s):
  result=""
  for char in s:
    if ord(char) >= 97 and ord(char) <= 122:
      result += unichr(219-ord(char))
    else:
      result += char
  return result

# print cipher("May the Force 1234 be with you.")
# print cipher(cipher("May the Force 1234 be with you."))

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