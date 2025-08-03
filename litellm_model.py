import os
import litellm

class LiteLLMWrapper:
    def __init__(self):
        self.model = os.getenv("LITELLM_MODEL", "openrouter/qwen/qwen-2.5-72b-instruct:free")
        self.api_key = os.getenv("LITELLM_API_KEY")
        self.api_base = os.getenv("LITELLM_API_BASE", "https://openrouter.ai/api/v1")


    def __call__(self, messages):
        try:
            response = litellm.completion(
                model=self.model,
                api_key=self.api_key,
                api_base=self.api_base,
                messages=messages,
                
            )
            content = response.get("choices", [{}])[0].get("message", {}).get("content", "")
            return content if content else "No response from model."
        except Exception as e:
            print("⚠️ LLM Error:", e)
            return "Sorry, I encountered an error while processing your request."

# Expose it as the model CrewAI uses
llm = LiteLLMWrapper()











