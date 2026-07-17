import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key) if api_key else None


def explain_python_code(code):
    if not code:
        return "No code provided."

    prompt = f"""
    You are an expert Python mentor.

    Analyze the following Python code.

    Your response MUST follow this format exactly.

    # Function Name

    # Purpose

    # Parameters

    # Return Value

    # Line-by-Line Explanation

    Explain every line separately.

    # Time Complexity

    # Space Complexity

    # Best Practices

    # Common Beginner Mistakes

    # Interview Questions
    Explain for a beginner.

    # Use simple English.

    # Never skip any line.

    # Use bullet points.

    # Give examples.

    # Mention mistakes beginners make.

    # End with one interview question.
    
    #Difficulty Level.

    # Easy

    # Medium

    # Hard

    Code:

    {code}

    Give a beginner-friendly explanation.
    """

    if client is None:
        return (
            "GROQ_API_KEY is not configured. "
            "This is a placeholder explanation for development."
        )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return response.choices[0].message.content
