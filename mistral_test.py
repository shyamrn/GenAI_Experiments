from langchain_community.llms import Ollama

llm_model = Ollama(base_url='http://localhost:11434', model='mistral')

print("==========================================================================================")
print(llm_model("Can you categorize the following email: I need help with porting my old number."))
print("==========================================================================================")
#print(llm_model("Which are the top 5 companies to invest in New Zealand for intraday trading?"))
