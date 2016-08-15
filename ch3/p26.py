# 26

import re
import p25
filepath = 'uk.txt'

def remove_emph(line):
  return re.sub(r"'{2,5}", r"",line)

p25.extract_template(filepath,remove_emph)