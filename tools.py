from groq import Groq
from groq import RateLimitError, BadRequestError

#tools for groq API

api_keys = []

with open(".\\APIKeys.txt", "r") as f:
  for line in f:
    api_keys.append(line[0:line.find('#')].strip())

clients = []
client_index = 0

for key in api_keys:
  clients.append(Groq(
      api_key = key
  ))

def swap_client():
  global client_index
  client_index += 1
  if client_index == len(clients):
    client_index = 0

#Models which support structured output
models = [
    "openai/gpt-oss-20b",
    "openai/gpt-oss-120b",
    "openai/gpt-oss-safeguard-20b"
]
model_index = 0

def swap_model():
  global model_index
  model_index += 1
  if model_index == len(models):
    model_index = 0

def get_response(messages, response_format):
  try:
    return clients[client_index].chat.completions.create(
          model = models[model_index],
          messages = messages,
          response_format = response_format
      )
  except RateLimitError as e:
    if hasattr(e, "response") and e.response:
      print("Status:", e.response.status_code)
      print("Headers:", e.response.headers)

      retry_after = e.response.headers.get("Retry-After")
      print("Retry-After:", retry_after)
    else:
      print("unable to get retry-after time")
    return None
  except BadRequestError as e:
    print(e)
    return None

def get_definite_response(messages, response_format):
  for _ in range(len(clients)):
    for _ in range(len(models)):
      response = get_response(messages, response_format)
      if response != None:
        return response
      swap_model()
    if response != None:
      return response
    swap_client()
  return None