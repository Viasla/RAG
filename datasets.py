import os
import json

from topics import topics_json_response
from tools import get_definite_response

datasets = {}

def save_datasets():
  with open("datasets.json", "w") as f:
    json.dump(datasets, f, indent = 4)


#Loading datasets

if os.path.exists("datasets.json"):
  datasets = json.load(open("datasets.json", "r"))
  print("Datasets loaded from memory")
else:
  datasets["theorems"] = {}
  datasets["definitions"] = {}

  for key, items in topics_json_response.items():
    for item in items["items"]:
      if item["type"] == "definition":
        if item["name"] in datasets["definitions"]:
          datasets["definitions"][item["name"]]["source"].append(key)
        else:
          datasets["definitions"][item["name"]] = {
              "source": [key],
              "Historical Notes": [],
              "Intuition": [],
              "Formal Definition": [],
              "Examples": [],
              "Notation":[],
              "Interpretation":[],
              "Properties": [],
          }
      if item["type"] == "theorem":
        if item["name"] in datasets["theorems"]:
          datasets["theorems"][item["name"]]["source"].append(key)
        else:
          datasets["theorems"][item["name"]] = {
              "source": [key],
              "Historical Notes": [],
              "Intuition": [],
              "Statement": [],
              "Proof": [],
              "Examples": [],
              "Notation":[],
              "Interpretation":[],
          }

  save_datasets()
  print("Created datasets")







definition_text_extraction_response_format = {
        "type": "json_schema",
        "json_schema": {
            "name": "concept_explanation",
            "schema": {
                "type": "object",
                "properties": {
                    "Historical Notes": {
                        "type": "array",
                        "items": {"type": "string"}
                    },
                    "Intuition": {
                        "type": "array",
                        "items": {"type": "string"}
                    },
                    "Formal Definition": {
                        "type": "array",
                        "items": {"type": "string"}
                    },
                    "Examples": {
                        "type": "array",
                        "items": {"type": "string"}
                    },
                    "Notation": {
                        "type": "array",
                        "items": {"type": "string"}
                    },
                    "Interpretation": {
                        "type": "array",
                        "items": {"type": "string"}
                    },
                    "Properties": {
                        "type": "array",
                        "items": {"type": "string"}
                    }
                },
                "required": [
                    "Historical Notes",
                    "Intuition",
                    "Formal Definition",
                    "Examples",
                    "Notation",
                    "Interpretation",
                    "Properties"
                ],
                "additionalProperties": False
            }
        }
    }

theorem_text_extraction_response_format = {
        "type": "json_schema",
        "json_schema": {
            "name": "concept_explanation",
            "schema": {
                "type": "object",
                "properties": {
                    "Historical Notes": {
                        "type": "array",
                        "items": {"type": "string"}
                    },
                    "Intuition": {
                        "type": "array",
                        "items": {"type": "string"}
                    },
                    "Statement": {
                        "type": "array",
                        "items": {"type": "string"}
                    },
                    "Proof": {
                        "type": "array",
                        "items": {"type": "string"}
                    },
                    "Examples": {
                        "type": "array",
                        "items": {"type": "string"}
                    },
                    "Notation": {
                        "type": "array",
                        "items": {"type": "string"}
                    },
                    "Interpretation": {
                        "type": "array",
                        "items": {"type": "string"}
                    }
                },
                "required": [
                    "Historical Notes",
                    "Intuition",
                    "Statement",
                    "Proof",
                    "Examples",
                    "Notation",
                    "Interpretation"
                ],
                "additionalProperties": False
            }
        }
    }



try:
  print("Completing definitions in datasets...")
  for name, desc in datasets["definitions"].items():
    if len(desc["source"]) == 0:
      continue
    for source in desc["source"][:]:
      filepath = os.path.join("parseoutput", source, source + ".md")
      content = None
      with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
      messages = [
          {
              "role": "user",
              "content": f"""Role:
You are an information extraction system.

Task:
Given the input text and a target topic, extract all pieces of information from the text that are relevant to the target topic.
The goal is exhaustive extraction, not summarization.

Rules:
1. Include information that is:
- directly about the target topic;
- indirectly relevant because it describes causes, effects, properties, relationships, events, decisions, constraints, examples, evidence, or context concerning the topic;
- repeated in different parts of the text when the repetitions contain different details;
- expressed using different terminology, synonyms, abbreviations, or references to the topic.
2. Do not include information that has no meaningful connection to the target topic.
3. Do not invent, assume, or supplement information that is not present in the source text.
4. Preserve the meaning of the original text.
5. Preserve important details such as names, dates, numbers, conditions, qualifications, relationships, and exceptions.
6. Keep relationships between facts explicit.
7. Distinguish facts from opinions, claims, hypotheses, and uncertainty when the source does so.
8. If the source contradicts itself, preserve both statements and identify the contradiction.
9. If the same entity or concept appears under different names, connect them when the text makes that relationship clear.
10. Do not merge separate facts merely because they seem related.
11. Prefer completeness over brevity.

Important:
Make each piece of information to be complete self contained paragraph.

Target topic: {name}.
Text: {content}
"""
          }
      ]

      response = get_definite_response(messages, definition_text_extraction_response_format)

      if response != None:
        objresponse = json.loads(response.choices[0].message.content)
        if "Historical Notes" in objresponse:
          datasets["definitions"][name]["Historical Notes"].extend(objresponse["Historical Notes"])
        if "Intuition" in objresponse:
          datasets["definitions"][name]["Intuition"].extend(objresponse["Intuition"])
        if "Formal Definition" in objresponse:
          datasets["definitions"][name]["Formal Definition"].extend(objresponse["Formal Definition"])
        if "Examples" in objresponse:
          datasets["definitions"][name]["Examples"].extend(objresponse["Examples"])
        if "Notation" in objresponse:
          datasets["definitions"][name]["Notation"].extend(objresponse["Notation"])
        if "Interpretation" in objresponse:
          datasets["definitions"][name]["Interpretation"].extend(objresponse["Interpretation"])
        if "Properties" in objresponse:
          datasets["definitions"][name]["Properties"].extend(objresponse["Properties"])
        desc["source"].remove(source)
        print(f"{name} : {source} [Full]")
        save_datasets()
      else:
        print(f"{name} : {source} [Empty]")
  print("Completing theorems in datasets...")
  for name, desc in datasets["theorems"].items():
    if len(desc["source"]) == 0:
      continue
    for source in desc["source"][:]:
      filepath = os.path.join("parseoutput", source, source + ".md")
      content = None
      with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
      messages = [
          {
              "role": "user",
              "content": f"""Role:
You are an information extraction system.

Task:
Given the input text and a target topic, extract all pieces of information from the text that are relevant to the target topic.
The goal is exhaustive extraction, not summarization.

Rules:
1. Include information that is:
- directly about the target topic;
- indirectly relevant because it describes causes, effects, properties, relationships, events, decisions, constraints, examples, evidence, or context concerning the topic;
- repeated in different parts of the text when the repetitions contain different details;
- expressed using different terminology, synonyms, abbreviations, or references to the topic.
2. Do not include information that has no meaningful connection to the target topic.
3. Do not invent, assume, or supplement information that is not present in the source text.
4. Preserve the meaning of the original text.
5. Preserve important details such as names, dates, numbers, conditions, qualifications, relationships, and exceptions.
6. Keep relationships between facts explicit.
7. Distinguish facts from opinions, claims, hypotheses, and uncertainty when the source does so.
8. If the source contradicts itself, preserve both statements and identify the contradiction.
9. If the same entity or concept appears under different names, connect them when the text makes that relationship clear.
10. Do not merge separate facts merely because they seem related.
11. Prefer completeness over brevity.

Important:
Make each piece of information to be complete self contained paragraph.

Target topic: {name}.
Text: {content}
"""
          }
      ]

      response = get_definite_response(messages, theorem_text_extraction_response_format)

      if response != None:
        objresponse = json.loads(response.choices[0].message.content)
        if "Historical Notes" in objresponse:
          datasets["theorems"][name]["Historical Notes"].extend(objresponse["Historical Notes"])
        if "Intuition" in objresponse:
          datasets["theorems"][name]["Intuition"].extend(objresponse["Intuition"])
        if "Statement" in objresponse:
          datasets["theorems"][name]["Statement"].extend(objresponse["Statement"])
        if "Examples" in objresponse:
          datasets["theorems"][name]["Examples"].extend(objresponse["Examples"])
        if "Notation" in objresponse:
          datasets["theorems"][name]["Notation"].extend(objresponse["Notation"])
        if "Interpretation" in objresponse:
          datasets["theorems"][name]["Interpretation"].extend(objresponse["Interpretation"])
        if "Proof" in objresponse:
          datasets["theorems"][name]["Proof"].extend(objresponse["Proof"])
        desc["source"].remove(source)
        print(f"[Full] {name} : {source}")
        save_datasets()
      else:
        print(f"[Empty] {name} : {source}")
  print("Done")
except KeyboardInterrupt:
  save_datasets()
  pass