from services.groq_client import client
from services.config import MODEL_NAME
def debug_python_code(code):
    
    prompt = f"""
    You are a Senior Python Debugger.

    Explain every bug in simple English.

    Suggest corrected code.

    Explain WHY the correction works.

    Mention beginner mistakes.

    Return corrected code.

    Rate the severity of each bug.
    
    Bug Severity

    Low

    Medium

    High
    
    Would this code crash? Yes / No

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

        model=MODEL_NAME,

        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return response.choices[0].message.content