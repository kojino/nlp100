# 2

def merge_strings(s1,s2):
  i = 0
  j = 0
  result = ""
  while i < len(s1) and j < len(s2):
    result += s1[i] + s2[j]
    i += 1
    j += 1
  if i>0:
    result += s1[i:]
  if j>0:
    result += s2[j:]
  return result

# print merge_strings("nice","job!")