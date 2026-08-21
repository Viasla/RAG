import os
import json

import tools

topics_json_response = {}

if os.path.exists("topics_output.json"):
  topics_json_response = json.load(open("topics_output.json", "r"))
else:
  for filename in sorted(os.listdir("parseoutput")):
    topics_json_response[filename] = None

def save_topics():
  with open("topics_output.json", "w") as f:
    json.dump(topics_json_response, f, indent = 4)

topics_response_format = {
        "type": "json_schema",
        "json_schema":{
            "name": "math_concepts",
            "schema": {
                "type": "object",
                "properties": {
                    "items": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "type": {
                                    "type": "string",
                                    "enum": ["definition", "theorem"]
                                },
                                "name": {
                                    "type": "string"
                                }
                        },
                            "required": ["type", "name"],
                            "additionalProperties": False
                        }
                    }
                },
                "required": ["items"],
                "additionalProperties": False
            }
        }
    }

try:
  print("Completing topics_json_response...")
  for filename in sorted(os.listdir("parseoutput")):
    if topics_json_response[filename] != None:
      continue
    filepath = os.path.join("parseoutput", filename, filename + ".md")
    content = None
    with open(filepath, "r", encoding="utf-8") as f:
      content = f.read()
    known_topics = []
    for values in topics_json_response.values():
      if values == None:
        continue
      for item in values["items"]:
        if item["name"] in known_topics:
          continue
        known_topics.append(item["name"])

# Extract only explicit difinitions and theorems. Do not infer or invent new ones.
#1. Extract only explicit difinitions and theorems names. Do not infer or invent new ones.
#2. Return one item per unique concept.
#3. Do not include section titles, chapter names, or general topics unless they are themselves definitions or theorems.
    topics_messages = [
        {
            "role": "user",
            "content": f"""Task:
Extract every definition and theorem name stated in the provided text.

Rules:
1. Compare each extracted item against the Existing Topics list.
  - If an extracted item is the same concept or a very close synonym of an existing topics, then use name provided by Existing Topics list.
  - Treat minor wording differences as duplicates (e.g. "Associative Law" vs "Associativity").
2. Give each extracted item a short, descriptive, canonical name (2-8 words when possible).
  - Prefer standard mathematical names.
  - Remove unnecessary context such as "Definition of", "The theorem states that", ect.
3. Extract only explicit and implicit definition and theorem names. Do not invent or infer new ones.
4. Do not include section titles, chapter names, or general topics unless they are themselves definitions or theorems.
5. Use only ASCII symbols. Do not use any LATEX nor unicode symbols.

Existing Topics:
- {"\n- ".join(known_topics)}

Text:
{content}
"""
        }
    ]

    response = tools.get_definite_response(topics_messages, topics_response_format)

    if response == None:
      print("[Empty] " + filename)
      topics_json_response[filename] = None
    else:
      print("[Full] " + filename)
      topics_json_response[filename] = json.loads(response.choices[0].message.content)
    save_topics()
  print("Done")
except KeyboardInterrupt:
  save_topics()
  pass