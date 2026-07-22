
from services.groq_client import client

from services.config import MODEL_NAME

def review_python_code(code):
    prompt = f"""
    Review this code like a Senior Python Developer.

    Give constructive feedback.

    Do not rewrite the code immediately.

    Explain WHY each suggestion is useful.

    Mention industry best practices.
    Finally,

    Return

    Corrected Code

    inside a Markdown code block.

    Your review MUST contain:

    1. Code Quality
    2. Readability
    3. Naming Convention
    4. Best Practices
    5. Possible Bugs
    6. Performance Improvements
    7. Security Issues
    8. Suggested Improvements
    9. Overall Rating (1-10)
    
    

    Code:

    {code}
    """
    response = client.chat.completions.create(

        model=MODEL_NAME,

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content  