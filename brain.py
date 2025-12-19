import os
from pathlib import Path
from google import genai
from dotenv import load_dotenv

script_dir = Path(__file__).parent

load_dotenv(script_dir / ".env")
load_dotenv()

def get_brain_command(user_input, cwd_context):
    """
    Sends the user's natural language intent to Gemini Flash
    and returns a macOS shell command.
    """
    
    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

    system_instruction = (
        "You are a text-to-command translator for a macOS (Darwin) terminal. "
        "The user will give you a natural language request. "
        "1. Output ONLY the shell command executable in zsh/bash. "
        "2. Do NOT use markdown formatting (no ```bash wrapper). "
        "3. Do NOT provide explanations. "
        "4. If the request is dangerous (like delete all files), prefix the command with '# WARNING: '. "
        f"5. The user is currently in this directory: {cwd_context}"
    )

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=user_input,
            config={
                "system_instruction": system_instruction,
                "temperature": 0.1 
            }
        )
        return response.text.strip()
    except Exception as e:
        return f"# ERROR: Connection failed - {str(e)}"