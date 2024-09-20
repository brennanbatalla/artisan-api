import json
import os

from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)


async def get_chat_response(message: str, context: str):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": f"You are a helpful assistant that helps answer a users questions regarding the context {context}. Return any recommended topics if it makes sense. Always return a JSON object with the parameters 'response' and 'quickOptions' in which response is a string and quickOptions is an array of strings.",
            },
            {
                "role": "user",
                "content": message,
            }
        ],
        model="gpt-4o-mini",
        response_format={"type": "json_object"},
    )

    return json.loads(chat_completion.choices[0].message.content)
