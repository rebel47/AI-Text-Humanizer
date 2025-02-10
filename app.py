import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Configure Google Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-flash')

def humanize_text(text, tone="neutral"):
    """
    Rewrites the input text to make it sound more human-like.
    """
    prompt = f"Rewrite the following text in a {tone} tone to make it sound more human-like.Use natural language, add variety in sentence structure, and include subtle conversational elements.  Ensure the length and meaning remain unchanged:\n\n{text}"
    response = model.generate_content(prompt)
    return response.text

def split_text(text, max_tokens=500):
    """
    Splits the input text into smaller chunks for processing.
    """
    words = text.split()
    chunks = [' '.join(words[i:i + max_tokens]) for i in range(0, len(words), max_tokens)]
    return chunks

def humanize_large_text(text, tone="neutral"):
    """
    Processes large texts by splitting them into chunks and humanizing each chunk.
    """
    chunks = split_text(text)
    humanized_chunks = []
    for chunk in chunks:
        humanized_chunks.append(humanize_text(chunk, tone))
    return ' '.join(humanized_chunks)

# Streamlit UI
st.set_page_config(page_title="AI Text Humanizer", page_icon="✍️", layout="centered")
st.title("AI Text Humanizer")
st.write("Paste your AI-generated text below to make it more human-like.")

# Input text area
user_input = st.text_area("Paste your text here:", height=200)

# Tone selection
tone = st.selectbox("Select Tone:", ["Casual", "Formal", "Persuasive", "Neutral"])

# Humanize button
if st.button("Humanize Text"):
    if user_input:
        with st.spinner("Processing..."):
            humanized_text = humanize_large_text(user_input, tone.lower())
            st.success("Done!")
            
            # Display humanized text
            st.text_area("Humanized Text:", humanized_text, height=200)
            
            # Display text length
            st.write(f"Input Length: {len(user_input.split())} words")
            st.write(f"Output Length: {len(humanized_text.split())} words")
            
            # Download button
            st.download_button(
                label="Download Humanized Text",
                data=humanized_text,
                file_name="humanized_text.txt",
                mime="text/plain"
            )
    else:
        st.error("Please enter some text to humanize.")