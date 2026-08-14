import os
import json

datasets = {}

def save_datasets():
  with open("datasets.json", "w") as f:
    json.dump(datasets, f, indent = 4)

if os.path.exists("datasets.json"):
  datasets = json.load(open("datasets.json", "r"))
  print("Loaded from memory datasets")
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
