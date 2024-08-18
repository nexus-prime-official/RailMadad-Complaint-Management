from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """

Here is the converstion history: {context}
Question: {question}
Answer:
"""
model = OllamaLLM(model="llama3.1")
prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model

def handle_conversation():
    context=""
    
    while True:
        question = input("You: ")
        if question.lower().strip() == "exit":
            break
        result = chain.invoke({"question": question, "context": context})
        print(f"Chatbot: {result}")
        context += f"You: {question}\nChatbot: {result}\n"


if __name__ == "__main__":
    handle_conversation()


