import re
import sys
import os

from topics.py import topics_json_response

UNICODE_ESCAPE_RE = re.compile(
    r"\\u([0-9a-fA-F]{4})"
)

correction_map = {
    
}


for filename in sorted(os.listdir("parseoutput")):
  filepath = os.path.join("parseoutput", filename, filename + ".md")
  content = None
  with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()
  ans = UNICODE_ESCAPE_RE.findall(content)
  if len(ans) > 0:
    print(f"{filename}: {ans}")
  #UNICODE_ESCAPE_RE.sub(replace, content)

