# 4

def elements(s):
  result = {}
  words = s.replace(',','').split( )
  get_one = [1, 5, 6, 7, 8, 9, 15, 16, 19]
  for i in range(len(words)):
    k = 1 if i + 1 in get_one else 2
    result[words[i][:k]] = i+1
  return result

# print elements("Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.")
