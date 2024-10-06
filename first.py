import os
from openai import OpenAI

def callAPI(arg) :
    client = OpenAI(
        # This is the default and can be omitted
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

    completion = client.chat.completions.create(
        messages=[
            {
        "role": "system",
        "content": [
            {
            "type": "text",
            "text": "you are a study tutor that gives out neat explanations and notes"
            }
        ]
        },
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": arg
            }
        ]
        }
        ],
        model="gpt-3.5-turbo",
    )
    return completion.choices[0].message.content
    

#print(completion.choices[0].message)