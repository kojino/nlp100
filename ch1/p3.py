# 3

def pi(s):
  result = []
  words = s.replace(',','').split( )
  for word in words:
    result.append(len(word))
  return result

# print pi("Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.")
