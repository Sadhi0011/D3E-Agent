import requests
import json
import os

# Load your complete D3E context (rules + examples)
def load_context(file_name):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    context_path = os.path.join(base_dir, '../Prompts/Models/Property Characteristic Models', file_name + '.md')
    with open(context_path, 'r', encoding='utf-8') as file:
        return file.read()

# Load the D3E context
all_ctx = {
    'ModelWithChildProperties': load_context('model-with-computed-properties'),
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