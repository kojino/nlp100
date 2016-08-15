# 28

import re
import p25
filepath = 'uk.txt'

def remove_other_markups(line):
  return re.sub(r"\[https?://[a-zA-Z0-9\./]+\s(.+)?\]",r'\1',line)


p25.extract_template(filepath,remove_other_markups)