import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key) if api_key else None

def debug_python_code(code):
    
    prompt = f"""
    You are an Expert Python Debugger.

    Analyze the following Python code.

    Your response MUST contain:

    1. Bugs Found
    2. Error Type
    3. Why the Bug Occurred
    4. Corrected Code
    5. Explanation of Fix
    6. Best Practices
    7. Similar Mistakes Beginners Make

    Return the corrected code inside a Python code block.

    Code:

    {code}
    """

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return response.choices[0].message.content