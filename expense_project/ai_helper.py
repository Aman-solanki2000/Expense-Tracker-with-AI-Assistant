from groq import Groq

import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ai_suggestion(expenses):

    if not expenses:
        print("AI: No data available")
        return

    
    total = sum(e.amount for e in expenses)

    
    category_total = {}

    for e in expenses:
        category_total[e.category] = (
            category_total.get(e.category, 0) + e.amount
        )

    highest_category = max(
        category_total,
        key=category_total.get
    )

    
    user_question = input("\nAsk AI anything about your expenses: ")

    
    prompt = f"""
    You are a smart finance assistant.

    Total expense: {total}

    Highest spending category: {highest_category}

    Category wise spending:
    {category_total}

    User question:
    {user_question}

    Give a helpful and short response.
    """

    try:

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        print("\n--- AI Assistant ---")
        print(response.choices[0].message.content)

    except Exception as e:
        print("AI Error:", e)
