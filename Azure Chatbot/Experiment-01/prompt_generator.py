# Padma | v2.0

#* Import libraries
import streamlit as st
import google.generativeai as genai
from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv

#* Load environment variables
load_dotenv()

#* Declare LLM model
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
llm_model = genai.GenerativeModel(model_name='models/gemini-1.5-pro-latest')

#* Function: Get response from Gemini
def generate_prompt(question, tones):    
    prompt = f"""
    Persona: You are Padma, an expert AI assistant.
    Task: 
    - Generate an effective prompt to be fed to an LLM application for the following requirement {question}.
    - Exclusively mention the tone in the prompt as {tones}. 
    Format: 
    - Prompt (in bold): (in non-bold)
    """
    response = llm_model.generate_content(prompt)
    return response

app = Flask(__name__)

@app.route('/prompt', methods=['POST'])
def greet():
    data = request.get_json()
    if 'request' and 'tones' in data:
        prompt_generated = generate_prompt(data['request'], data['tones'])
        return jsonify({'response': prompt_generated.candidates[0].content.parts[0].text})
        st.write(blog.candidates[0].content.parts[0].text)
        #return jsonify({'response': f"I am {data['text']}, pleasure meeting you!"})
    else:
        return jsonify({'error': 'Text input is required'}), 400

if __name__ == '__main__':
    app.run(debug=True)
