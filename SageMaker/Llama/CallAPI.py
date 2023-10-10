import requests

api_url = 'https://hy6pzm1v6e.execute-api.us-east-1.amazonaws.com/default/PSD-LlamaRequest'

json_body = {
 "inputs": [
  [
   {"role": "system", "content": "You are chat bot who writes songs"},
   {"role": "user", "content": "Write a rap about Barbie"}
  ]
 ],
 "parameters": {"max_new_tokens":256, "top_p":0.9, "temperature":0.6}
}

r = requests.post(api_url, json=json_body)

print(r.json())

