import re
import sys
import os

from topics import topics_json_response

UNICODE_ESCAPE_RE = re.compile(
    r"\\u([0-9a-fA-F]{4})"
)

correction_map = {
  "00f3": "o",
    "2013": "-"
}


# for filename in sorted(os.listdir("parseoutput")):
#   filepath = os.path.join("parseoutput", filename, filename + ".md")
#   content = None
#   with open(filepath, "r", encoding="utf-8") as f:
#     content = f.read()
#   ans = UNICODE_ESCAPE_RE.findall(content)
#   if len(ans) > 0:
#     print(f"{filename}: {ans}")
#   #UNICODE_ESCAPE_RE.sub(replace, content)

def replace(match):
  value = match.group(1)
  if value and value in correction_map:
    #print(f"correcting \\u{value} to {correction_map[value]}")
    return correction_map[value]
  else:
    print(f"Unknown value {value}, ignored")
    return value

def correct_file(filepath):
  content = None
  with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()
  with open(filepath, "w") as f:
    f.write(UNICODE_ESCAPE_RE.sub(replace, content))