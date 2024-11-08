from transformers import LongT5ForConditionalGeneration, AutoTokenizer, pipeline
import torch

# Initialize LongT5 model and tokenizer for generating long-form content
model_name = "google/long-t5-tglobal-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = LongT5ForConditionalGeneration.from_pretrained(model_name)

def generate_long_text(prompt, max_length=1024):
    inputs = tokenizer(prompt, return_tensors="pt")
    output = model.generate(inputs.input_ids, max_length=max_length, num_beams=4, early_stopping=True)
    text = tokenizer.decode(output[0], skip_special_tokens=True)
    return text

# Using BERT for Summarization
summarizer = pipeline("summarization", model="bert-large-uncased")

def summarize_text(text):
    summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
    return summary[0]['summary_text']

def generate_blog_post(topic, structure=["Introduction", "Key Points", "Conclusion"]):
    """
    Generates a blog post on a given topic with the specified structure.
    """
    prompt = f"Write a blog post on the topic: {topic}. The structure should include the following sections:\n\n"
    for section in structure:
        prompt += f"## {section}\n\n"
    long_text = generate_long_text(prompt)
    return long_text

# Function to generate a blog post on a specific topic
prompt = "Explain the advancements in generative AI for 2025."
long_text = generate_long_text(prompt)
summary = summarize_text(long_text)
print("Generated Long Text:", long_text)
print("Summary:", summary)
