# litellm_model.py (Corrected for Gemma on OpenRouter)

import os
import litellm
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

class LiteLLMWrapper:
    def __init__(self):
        # <<< FIX: Add the 'openrouter/' prefix to the model string.
        self.model = "openrouter/mistralai/mistral-7b-instruct:free" 
        
        self.api_key = "YOUR_OPENROUTER_API_KEY"
        self.api_base = "https://openrouter.ai/api/v1"

    def __call__(self, messages):
        if not self.api_key:
            raise ValueError("OPENROUTER_API_KEY not found in environment variables.")
            
        try:
            response = litellm.completion(
                # You are correctly specifying the provider here, but the model string also needs to be specific.
                provider="openrouter",
                model=self.model,
                api_key=self.api_key,
                api_base=self.api_base,
                messages=messages,
            )
            
            content = response.get("choices", [{}])[0].get("message", {}).get("content", "")
            return content if content else "No response from model."
        except Exception as e:
            # The error you received was caught here.
            print(f"⚠ LLM Error: {e}")
            return "Sorry, I encountered an error while processing your request with the LLM."

# Expose the initialized class instance as 'llm' for CrewAI to use
llm = LiteLLMWrapper()