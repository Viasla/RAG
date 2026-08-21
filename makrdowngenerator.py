from pathlib import Path

import os
import json

if os.path.exists("datasets.json"):
  datasets = json.load(open("datasets.json", "r"))
  print("Datasets loaded from memory")

Path("markdown_output").mkdir(parents=True, exist_ok=True)

for name, desc in datasets["definitions"].items():
  try:
    with open(Path("markdown_output") / (name + ".md"), "w", encoding="utf-8") as f:
      print("# Historical Notes\n", file=f)
      for info in desc["Historical Notes"]:
        print(info, end="\n\n", file=f)

      print("# Intuition\n", file=f)
      for info in desc["Intuition"]:
        print(info, end="\n\n", file=f)

      print("# Formal Definition\n", file=f)
      for info in desc["Formal Definition"]:
        print(info, end="\n\n", file=f)

      print("# Examples\n", file=f)
      for info in desc["Examples"]:
        print(info, end="\n\n", file=f)

      print("# Notation\n", file=f)
      for info in desc["Notation"]:
        print(info, end="\n\n", file=f)

      print("# Interpretation\n", file=f)
      for info in desc["Interpretation"]:
        print(info, end="\n\n", file=f)

      print("# Properties\n", file=f)
      for info in desc["Properties"]:
        print(info, end="\n\n", file=f)
  except Exception as e:
    print(e)



