import requests
import json
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

#print(json.dumps(api_response, indent=2))

print(api_response["choices"][0]["message"]["content"])