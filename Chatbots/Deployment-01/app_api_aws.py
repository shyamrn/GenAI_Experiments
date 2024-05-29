# Query Categorizer | AWS Lambda Deployment | v1.2

#* Import libraries
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
import boto3
import botocore.config
import json
import os
from dotenv import load_dotenv

#* Load environment variables
load_dotenv()

#* Function: Query categorizer
def query_categorizer(query):
    #* Declare llm model
    llm = OpenAI(temperature=0.0)
    prompt_template = """
    Persona: You are an expert AI agent who is capable of classifying user query into appropriate category.
    
    Context: You should classify {query} into an appropriate category based on the context of customer support system.
    
    Task: Analyze and categorize {query}. The category should be between less than 4 words.
    
    Format:
    Category: 
    
    Exemplar:
    Query: I am unable to access the portal.
    Category: Portal help
    
    Query: I need to transfer my broadband to my new address
    category: Transfer service
    
    Tone: Formal
    """
    prompt = PromptTemplate.from_template(template=prompt_template)
    llm_chain = prompt | llm
    response = llm_chain.invoke(query)
    return response

#* Function: Lambda handler
def lambda_handler(event, context):
    event = json.loads(event['body'])
    query = event['query']
    blog_data = query_categorizer(query)
