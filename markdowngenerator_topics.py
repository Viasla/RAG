from pathlib import Path

import os
import json

from datasets import datasets

from datasets import definition_topics, theorem_topics

Path("markdown_topics_output").mkdir(parents=True, exist_ok=True)

def generate_files_theme(theme, theme_topics):
  for name, desc in datasets[theme].items():
    for topic in theme_topics:
      isEmpty = True
      for infos in desc[topic]:
        for info in infos["items"]:
          if len(info) > 0:
            isEmpty = False
      if(isEmpty):
        continue
      try:
        print(f"Creating file \"{name} - {topic}.md\"")
        with open(Path("markdown_topics_output") / (f"{name} - {topic}.md"), "w", encoding="utf-8") as f:
          print(f"# {topic}", file=f)
          for infos in desc[topic]:
            for info in infos["items"]:
              print(info, end="\n\n", file=f)
        print("Done")
      except Exception as e:
        print(e)

generate_files_theme("definitions", definition_topics)
generate_files_theme("theorems", theorem_topics)