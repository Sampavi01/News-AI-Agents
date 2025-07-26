# test_llm.py

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

print("--- Starting direct LLM test ---")
load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")

if not google_api_key:
    print("\n!!! ERROR: Google API Key not found. Check your .env file. !!!")
else:
    print(f"--- API Key found, starting with '{google_api_key[:4]}...' ---")
    try:
        # 1. Create the LLM instance
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=google_api_key)
        print("--- LLM object created successfully. ---")
        
        # 2. Invoke the LLM directly
        print("--- Invoking the LLM... ---")
        response = llm.invoke("Tell me a one-sentence fact about Jupiter.")
        
        # 3. Print the result
        print("--- LLM invoked successfully! ---")
        print("\nResponse from Gemini:")
        print(response.content)
        
    except Exception as e:
        print("\n!!! An error occurred during the direct LLM test. !!!")
        print(f"Error Type: {type(e).__name__}")
        print(f"Error Details: {e}")

print("\n--- LLM test finished. ---")