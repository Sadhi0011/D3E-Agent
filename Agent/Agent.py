import requests
import json

# Load your complete D3E context (rules + examples)
def load_context(file_name):
    with open('./context/' + file_name + '.md', 'r') as file:
        return file.read()

API_URL = "https://jnpai.d3e.studio/api/chat"

# Load the D3E context

all_ctx = {
    # 'Specification': load_context('specification'),
    # 'Architecture': load_context('architecture'),
    # "List": load_context('list'),
    # 'Backend': load_context('backend'),
    'Frontend': load_context('frontend'),
    # 'Document': load_context('document'),
    # 'Backend Code': load_context('d3e_backend_code'),
    # 'Frontend Code': load_context('d3e_frontend_code')
}

frontend_types = [
    'Page',
    'Widget'
]

# Add any additional context or rules as needed
# If you have more context files, you can load them similarly
# Load the D3E context and examples
# d3e_context = load_context('additional_rules')  # Uncomment if you have more context files

# This system message ensures the model stays in D3E world
system_message = f"""
```d3e
{all_ctx}
```
You are a D3E expert. You ONLY generate output in valid D3E framework syntax.

Here is the full context and rules of D3E:
{all_ctx}

Never use HTML, Markdown, or other formats. Always respond using valid D3E code blocks.
"""

print("🤖 D3E AI Assistant (type 'exit' to quit)")

while True:
    user_prompt = input("\n🧑 You: ")

    if user_prompt.strip().lower() in ['exit', 'quit']:
        print("👋 Exiting D3E AI Assistant.")
        break

    payload = {
        "system": system_message,
        "prompt": user_prompt
    }

    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(API_URL, data=json.dumps(payload), headers=headers)
        if response.status_code == 200:
            try:
                json_response = response.json()
                if isinstance(json_response, dict):
                    result = json_response.get("response", "⚠️ 'response' field missing.")
                elif isinstance(json_response, str):
                    result = json_response
                else:
                    result = str(json_response)
            except json.JSONDecodeError:
                result = response.text
        else:
            result = f"❌ Error {response.status_code}: {response.text}"

    except Exception as e:
        result = f"❗ Exception occurred: {str(e)}"

    print(f"\n🤖 D3E AI:\n{result}")
 