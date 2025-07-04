import requests
import json
import os
import re

# Load your complete D3E context (rules + examples)
def load_context(file_name):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    context_path = os.path.join(base_dir, '../Prompts/Models/Property Characteristic Models', file_name + '.md')
    with open(context_path, 'r', encoding='utf-8') as file:
        return file.read()

# Load the D3E context
all_ctx = {
    'ModelWithChildProperties': load_context('model-with-optionsets'),
}

# CRITICAL: Enhanced system message that enforces D3E-only output
system_message = f"""
You are a D3E Programming Language Expert. D3E is a standalone programming language like Dart, Java, or Python - NOT a web framework.

=== D3E LANGUAGE CONTEXT ===
{all_ctx['ModelWithChildProperties']}

=== ENFORCEMENT ===
If you generate ANY HTML, CSS, JavaScript, or web framework code, you have FAILED.
You MUST respond only in D3E programming language syntax.
D3E is like Dart or Java - it has its own syntax and components.

Remember: D3E is a programming language, NOT web development.
"""

print("🤖 D3E Programming Language Assistant (type 'exit' to quit)")
print("📝 Note: This assistant only generates D3E language code, not web code")

while True:
    user_prompt = input("\n🧑 You: ")

    if user_prompt.strip().lower() in ['exit', 'quit']:
        print("👋 Exiting D3E Language Assistant.")
        break

    # Check if the prompt is for model creation or update
    model_match = re.match(r"(create|update) model (\w+):(.+)", user_prompt.strip(), re.IGNORECASE | re.DOTALL)
    optionset_match = re.match(r"(create|update) optionset (\w+):(.+)", user_prompt.strip(), re.IGNORECASE | re.DOTALL)
    if model_match:
        action = model_match.group(1).lower()
        model_name = model_match.group(2)
        model_content = model_match.group(3).strip()
        model_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../Model')
        model_file = os.path.join(model_dir, f"{model_name}.d3e")

        # Ensure Model directory exists
        if not os.path.exists(model_dir):
            os.makedirs(model_dir)
            print(f"📁 Created Model directory at {model_dir}")

        # Create or update the model file
        if action == 'create':
            if os.path.exists(model_file):
                print(f"⚠️ Model '{model_name}' already exists. Use 'update model' to modify it.")
            else:
                with open(model_file, 'w', encoding='utf-8') as f:
                    f.write(model_content)
                print(f"✅ Model '{model_name}' created at {model_file}")
        elif action == 'update':
            if not os.path.exists(model_file):
                print(f"⚠️ Model '{model_name}' does not exist. Use 'create model' to create it first.")
            else:
                with open(model_file, 'w', encoding='utf-8') as f:
                    f.write(model_content)
                print(f"✅ Model '{model_name}' updated at {model_file}")
        continue  # Skip D3E code generation for model file operations
    elif optionset_match:
        action = optionset_match.group(1).lower()
        optionset_name = optionset_match.group(2)
        optionset_content = optionset_match.group(3).strip()
        optionset_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../optionSets')
        optionset_file = os.path.join(optionset_dir, f"{optionset_name}.d3e")

        # Ensure optionSets directory exists
        if not os.path.exists(optionset_dir):
            os.makedirs(optionset_dir)
            print(f"📁 Created optionSets directory at {optionset_dir}")

        # Create or update the OptionSet file
        if action == 'create':
            if os.path.exists(optionset_file):
                print(f"⚠️ OptionSet '{optionset_name}' already exists. Use 'update optionset' to modify it.")
            else:
                with open(optionset_file, 'w', encoding='utf-8') as f:
                    f.write(optionset_content)
                print(f"✅ OptionSet '{optionset_name}' created at {optionset_file}")
        elif action == 'update':
            if not os.path.exists(optionset_file):
                print(f"⚠️ OptionSet '{optionset_name}' does not exist. Use 'create optionset' to create it first.")
            else:
                with open(optionset_file, 'w', encoding='utf-8') as f:
                    f.write(optionset_content)
                print(f"✅ OptionSet '{optionset_name}' updated at {optionset_file}")
        continue  # Skip D3E code generation for OptionSet file operations

    # Enhanced prompt that reinforces D3E-only output
    enhanced_prompt = f"""
Generate D3E programming language code for: {user_prompt}

IMPORTANT REMINDERS:
- Use D3E language syntax only (Widget/Page objects)
- Use D3E UI components (Column, Row, TextView, Button, etc.)
- NO HTML tags, NO CSS styles, NO JavaScript code
- D3E is a programming language like Dart or Java

Request: {user_prompt}
"""

    payload = {
        "system": system_message,
        "prompt": enhanced_prompt
    }

    headers = {
        "Content-Type": "application/json"
    }

    try:
        API_URL = "https://jnpai.d3e.studio/api/chat"
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
                
                # Check if the response contains web code and warn
                if any(tag in result.lower() for tag in ['<div>', '<span>', '<button>', '<html>', 'function', '.class', '#id']):
                    print("⚠️ WARNING: AI generated web code instead of D3E language code!")
                    print("🔄 Try rephrasing your request to be more specific about D3E syntax.")
                    
            except json.JSONDecodeError:
                result = response.text
        else:
            result = f"❌ Error {response.status_code}: {response.text}"

    except Exception as e:
        result = f"❗ Exception occurred: {str(e)}"

    print(f"\n🤖 D3E Language AI:\n{result}")

    # --- New logic: Save models to files ---
    def save_models_from_d3e_output(d3e_output):
        import re
        def extract_model_blocks(text):
            blocks = []
            pattern = re.compile(r'Model\s*\{', re.MULTILINE)
            for match in pattern.finditer(text):
                start = match.start()
                brace_count = 0
                i = start
                while i < len(text):
                    if text[i] == '{':
                        brace_count += 1
                    elif text[i] == '}':
                        brace_count -= 1
                        if brace_count == 0:
                            blocks.append(text[start:i+1])
                            break
                    i += 1
            return blocks

        def extract_optionset_blocks(text):
            blocks = []
            pattern = re.compile(r'OptionSet\s*\{', re.MULTILINE)
            for match in pattern.finditer(text):
                start = match.start()
                brace_count = 0
                i = start
                while i < len(text):
                    if text[i] == '{':
                        brace_count += 1
                    elif text[i] == '}':
                        brace_count -= 1
                        if brace_count == 0:
                            blocks.append(text[start:i+1])
                            break
                    i += 1
            return blocks

        model_blocks = extract_model_blocks(d3e_output)
        for block in model_blocks:
            # Extract model name
            name_match = re.search(r"name ['\"]([^'\"]+)['\"]", block)
            if not name_match:
                continue
            model_name = name_match.group(1)
            model_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../Model')
            model_file = os.path.join(model_dir, f"{model_name}.d3e")
            if not os.path.exists(model_dir):
                os.makedirs(model_dir)
            # Write or update the model file
            with open(model_file, 'w', encoding='utf-8') as f:
                f.write(block)
            print(f"📄 Model '{model_name}' saved/updated at {model_file}")

        # --- New logic: Save OptionSets to files ---
        optionset_blocks = extract_optionset_blocks(d3e_output)
        for block in optionset_blocks:
            # Extract OptionSet name
            name_match = re.search(r"name ['\"]([^'\"]+)['\"]", block)
            if not name_match:
                continue
            optionset_name = name_match.group(1)
            optionset_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../optionSets')
            optionset_file = os.path.join(optionset_dir, f"{optionset_name}.d3e")
            if not os.path.exists(optionset_dir):
                os.makedirs(optionset_dir)
            # Write or update the OptionSet file
            with open(optionset_file, 'w', encoding='utf-8') as f:
                f.write(block)
            print(f"📄 OptionSet '{optionset_name}' saved/updated at {optionset_file}")

    save_models_from_d3e_output(result)

# Additional function to validate D3E output
def validate_d3e_output(output):
    """Check if output is valid D3E code"""
    web_indicators = [
        '<div>', '<span>', '<button>', '<html>', '<head>', '<body>',
        'function(', 'const ', 'let ', 'var ', 'document.',
        '.class', '#id', 'display:', 'padding:', 'margin:'
    ]
    
    d3e_indicators = [
        'Widget {', 'Page {', 'Column {', 'Row {', 'TextView {',
        'Button {', 'name \'', 'properties [', 'build ', 'eventHandlers ['
    ]
    
    has_web_code = any(indicator in output for indicator in web_indicators)
    has_d3e_code = any(indicator in output for indicator in d3e_indicators)
    
    if has_web_code and not has_d3e_code:
        return False, "Contains web code instead of D3E"
    elif has_d3e_code:
        return True, "Valid D3E code detected"
    else:
        return False, "No recognizable D3E code found"