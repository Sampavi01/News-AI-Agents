# tools.py (Final and Correct Version)

# --- CORRECTED IMPORTS ---
# We only need the @tool decorator and SerperDevTool
from crewai.tools import tool
from crewai_tools import SerperDevTool

# Import the necessary libraries for the tool's logic
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
import logging

# --- TOOL DEFINITION ---

# Initialize the standard SerperDevTool for general web searches
search_tool = SerperDevTool()

# Define our custom tool using the @tool decorator
@tool("Website Content Search Tool")
def website_content_search_tool(search_input: str) -> str:
    """
    Use this tool to search for specific information within the content of a single webpage.
    The input should be a comma-separated string of the website URL and the search query.
    Example: 'https://example.com, What are the key features of the product?'
    """
    try:
        # Split the input string into URL and search query
        website_url, search_query = search_input.split(",", 1)
        website_url = website_url.strip()
        search_query = search_query.strip()
    except ValueError:
        return "Error: Invalid input format. Please provide the website URL and the search query separated by a comma."

    logging.info(f"--- Searching content on {website_url} for '{search_query}' ---")

    # 1. Load website content
    try:
        loader = WebBaseLoader(website_url)
        docs = loader.load()
        if not docs:
            return f"Error: Could not load any content from {website_url}."
    except Exception as e:
        return f"Error loading website content: {e}"

    # 2. Split the documents into smaller chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    splits = text_splitter.split_documents(docs)

    # 3. Create the embedding model (free, runs locally)
    embedder = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # 4. Create a FAISS vector store (in-memory searchable database)
    try:
        vectorstore = FAISS.from_documents(splits, embedder)
    except Exception as e:
        return f"Error creating vector store: {e}"

    # 5. Perform a similarity search
    try:
        relevant_docs = vectorstore.similarity_search(search_query, k=5)
    except Exception as e:
        return f"Error during similarity search: {e}"


    # 6. Format and return the results
    if not relevant_docs:
        return f"No relevant information found on {website_url} for the query '{search_query}'."

    result_texts = [doc.page_content for doc in relevant_docs]
    return "\n\n---\n\n".join(result_texts)