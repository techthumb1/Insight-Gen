import openai
from transformers import T5ForConditionalGeneration, AutoTokenizer
import torch
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize T5 for summarization
t5_model_name = "t5-small"
t5_tokenizer = AutoTokenizer.from_pretrained(t5_model_name)
t5_model = T5ForConditionalGeneration.from_pretrained(t5_model_name)

# Check for GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
t5_model.to(device)

def generate_structured_content(prompt, section):
    """
    Generates structured content for a specific section using the OpenAI Completion API.
    """
    full_prompt = f"{prompt}\n\nPlease provide a detailed section on '{section}':"
    try:
        response = openai.Completion.create(
            model="text-davinci-003",    # Replace with other models if available
            prompt=full_prompt,
            max_tokens=800,
            temperature=0.7
        )
        content = response.choices[0].text.strip()
        print(f"Generated Content for {section}:\n", content)
        return content
    except Exception as e:
        print(f"Error generating content for {section}:", e)
        return None

def summarize_section(text, max_length=100, min_length=50):
    """
    Summarizes a specific section using T5 with defined min/max length.
    """
    inputs = t5_tokenizer(text, return_tensors="pt").to(device)
    summary_ids = t5_model.generate(
        inputs.input_ids,
        max_length=max_length,
        min_length=min_length,
        num_beams=5,
        early_stopping=True
    )
    summary = t5_tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    print("Section Summary:", summary)
    return summary

# Example Usage
if __name__ == "__main__":
    # General prompt for structured output
    prompt = "Provide a comprehensive overview of advancements in generative AI for 2025, including key sections."

    # Define sections
    sections = ["Introduction", "Key Innovations", "Applications", "Challenges", "Future Trends"]

    structured_content = {}
    structured_summaries = {}

    for section in sections:
        # Step 1: Generate content for each section
        section_content = generate_structured_content(prompt, section)
        if section_content:
            structured_content[section] = section_content

            # Step 2: Summarize each section
            structured_summaries[section] = summarize_section(section_content)
    
    # Print final structured content and summaries
    print("\nFinal Structured Content:", structured_content)
    print("\nFinal Summaries:", structured_summaries)
