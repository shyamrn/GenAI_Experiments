from langchain_community.llms import Ollama

llm_model = Ollama(base_url='http://localhost:11434', model='BB-8')
generic_llm_model = Ollama(base_url='http://localhost:11434', model='llama2')

print(llm_model("Can you categorize the following email: I need help with porting my old number."))
print("==========================================================================================")
print(generic_llm_model("Can you categorize the following email: I need help with porting my old number."))
print("==========================================================================================")
print(generic_llm_model("Extract sentiment of the following email: I need help with porting my old number."))
print("==========================================================================================")
print(generic_llm_model("Extract sentiment of the following email: I am happy with the plans."))
