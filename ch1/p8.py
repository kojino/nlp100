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
