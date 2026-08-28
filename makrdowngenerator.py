from pathlib import Path

import os
import json

from datasets import datasets

from datasets import definition_topics, theorem_topics

Path("markdown_output").mkdir(parents=True, exist_ok=True)

for name, desc in datasets["definitions"].items():
  try:
    print(f"Creating file \"{name}\"")
    with open(Path("markdown_output") / (name + ".md"), "w", encoding="utf-8") as f:
      print("""---
tags:
  - definition
Type: Definition
---
        """, file=f)

      for topic in definition_topics:
        print(f"# {topic}", file=f)
        for infos in desc[topic]:
          for info in infos["items"]:
            print(info, end="\n\n", file=f)
    print("Done")
  except Exception as e:
    print(e)

for name, desc in datasets["theorems"].items():
  try:
    print(f"Creating file \"{name}\"")
    with open(Path("markdown_output") / (name + ".md"), "w", encoding="utf-8") as f:
      print("""---
tags:
  - theorem
Type: Theorem
---
        """, file=f)

      for topic in theorem_topics:
        print(f"# {topic}", file=f)
        for infos in desc[topic]:
          for info in infos["items"]:
            print(info, end="\n\n", file=f)
    print("Done")
  except Exception as e:
    print(e)

