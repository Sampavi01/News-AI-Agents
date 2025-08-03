import litellm
import os

response = litellm.completion(
    model="openrouter/qwen/qwen-2.5-72b-instruct:free",               # add `openai/` prefix to model so litellm knows to route to OpenAI
    api_key="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",                  # api key to your openai compatible endpoint
    api_base="https://openrouter.ai/api/v1",     # set API Base of your Custom OpenAI Endpoint
    messages=[
                {
                    "role": "user",
                    "content": "Hey, how's it going?",
                }
    ],
    
)
print(response)


