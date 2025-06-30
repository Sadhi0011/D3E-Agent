import os
import requests
import json

# Helper to load a file from a given folder
def load_file(folder, file_name):
    path = os.path.join(f'./{folder}/', f'{file_name}.md')
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as file:
            return file.read()
    return ''

# List of modules to load
modules = [
    'Model', 'optionSets', 'Widget', 'Page', 'WidgetTestData', 'Struct', 'UserType',
    'StyleTheme', 'Style', 'ScheduleActions', 'QueryUsage', 'resources'
]

# Load all context, prompt, and description files for each module
all_contexts = {}
all_prompts = {}
all_descriptions = {}
for module in modules:
    all_contexts[module] = load_file('Context', f'{module}-Context')
    all_prompts[module] = load_file('Prompt', f'{module}-Prompt')
    all_descriptions[module] = load_file('Description', f'{module}-Description')

# Load the D3E core context
core_ctx = {
    'Specification': load_file('Context', 'specification'),
    'Architecture': load_file('Context', 'architecture'),
    'List': load_file('Context', 'list'),
    'Backend': load_file('Context', 'backend'),
    'Frontend': load_file('Context', 'frontend'),
    'Document': load_file('Context', 'document'),
    'Backend Code': load_file('Context', 'd3e_backend_code'),
    'Frontend Code': load_file('Context', 'd3e_frontend_code')
}

API_URL = "https://jnpai.d3e.studio/api/chat"

# Compose the system message
system_message = """
You are a D3E expert. You ONLY generate output in valid D3E framework syntax.

Below is the full context and rules of D3E. Use ONLY the provided D3E code examples as templates for your output. Never use HTML, Markdown, or any other format. Always respond using valid D3E code blocks, matching the structure and style of the examples.

# Core Context
"""
system_message += str(core_ctx) + "\n\n"
for module in modules:
    system_message += f"# {module} Context\n{all_contexts[module]}\n\n"
    system_message += f"# {module} Prompts\n{all_prompts[module]}\n\n"
    system_message += f"# {module} Descriptions\n{all_descriptions[module]}\n\n"
system_message += """
# D3E Model Example (use this format for all models):
```d3e
Model {
    name 'Example'
    properties [
        {
            name 'Property'
            type String
        }
    ]
}
```

Always output only a single valid D3E code block for the requested model, following the above format and the detailed examples in the context.
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
