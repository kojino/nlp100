# 27

import re
import p25
filepath = 'uk.txt'

def remove_internal_link(line):
  return re.sub(r"\[\[([^|\]]+?\|)*(.+?)\]\]",r'\2',line)

p25.extract_template(filepath,remove_internal_link)