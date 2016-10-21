# 50

filepath = 'nlp.txt'

def split_sentences(filepath):
  file = open(filepath,'r')
  output = open('nlp_lines.txt','w')
  line = []
  while True:
    c = file.read(1)
    if not c:
      print "End of file"
      break
    if c == '\n':
      output.writelines(line)
      line = []
    else:
      if c == ''

    print "Read a character:", c

split_sentences(filepath)