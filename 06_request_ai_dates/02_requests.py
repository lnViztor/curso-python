# pylint: disable=W0311
# pylint: disable=W0120
# pylint: disable=W0120
# pylint: disable=C0103
# pylint: disable=C0321
# pylint: disable=C0301
# pylint: disable=C0114
# pylint: disable=C0304
# pylint: disable=C0303
# pylint: disable=C2401
# pylint: disable=C0116
# pylint: disable=W0621
# pylint: disable=C0413
# pylint: disable=W0105
# pylint: disable=W3101

# Cómo hacer peticiones a APIs con Python
# con y sin dependencias

#  1. Sin dependencias (díficil y sin dependencias)

import urllib.request
import json
import requests

DEEPSEEK_API_KEY = "xxx"

api_posts = "https://jsonplaceholder.typicode.com/posts/"

try:
    response = urllib.request.urlopen(api_posts)
    data = response.read()
    json_data = json.loads(data.decode('utf-8'))
    print(json_data)
    response.close()
except urllib.error.URLError as e:
    print(f"Error en la solicitud: {e}")


# 2. Con dependencia (requests)
print("\nGET:")
api_posts = "https://jsonplaceholder.typicode.com/posts/"
response = requests.get(api_posts)
response_json = response.json()
print(response_json[0])


# 3. Un POST
print("\nPOST:")
try:
    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json={
            "title": "foo",
            "body": "bar",
            "userId": 1
        })
    print(response.status_code)
except requests.exceptions.RequestException as e:
    print(f"Error en la solicitud: {e}")

# 4. Un PUT
print("\nPUT:")
try:
    response = requests.put(
        "https://jsonplaceholder.typicode.com/posts/1",
        json={
            "title": "foo",
            "body": "bar",
            "userId": 1,
        })

    print(response.status_code)
except requests.exceptions.RequestException as e:
    print(f"Error en la solicitud: {e}")

# Usar la API de GPT-4o de OpenAI
# Ref: https://platform.openai.com/docs/api-reference/making-requests

OPENAI_KEY = "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"


def call_openai_gpt(api_key, prompt):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(url, json=data, headers=headers)
    return response.json()


api_response = call_openai_gpt(
    OPENAI_KEY, "Escribe un breve poema sobre la programación")

# print(json.dumps(api_response, indent=2))

print(api_response["choices"][0]["message"]["content"])

# Llamar a la API de DEEPSEEK


def call_deepseek(api_key, prompt):
    url = "https://api.deepseek.com/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(url, json=data, headers=headers)
    print(response.json())
    return response.json()


api_response = call_deepseek(
    DEEPSEEK_API_KEY, "Escribe un breve poema sobre la programación")

# print(json.dumps(api_response, indent=2))

print(api_response["choices"][0]["message"]["content"])
