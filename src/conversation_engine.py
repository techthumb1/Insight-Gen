import openai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_conversational_response(query):
    """
    Generates a conversational response to a given query.
    Example queries include requests for algorithm explanations, tutorials, use cases, etc.
    """
    prompt = f"You are a highly knowledgeable AI assistant that explains topics in an engaging and educational way. Answer the following query in a clear, detailed manner:\n\nQuery: {query}\n\nResponse:"
    
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Use a conversational model
        messages=[{"role": "user", "content": prompt}],
        max_tokens=700,
        temperature=0.7
    )
    
    return response.choices[0].message["content"].strip()

#Run the conversational response generation
if __name__ == "__main__":
    query = "Explain the Random Forest algorithm and its applications."
    response = get_conversational_response(query)
    print("Generated Response:", response)
