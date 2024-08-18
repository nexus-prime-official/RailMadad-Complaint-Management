from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Define the list of possible classes
classes = [
    "Coach - Maintenance/Facilities",
    "Electrical Equipment",
    "Medical Assistance",
    "Catering / Vending Services",
    "Water Availability",
    "Punctuality",
    "Security",
    "Unreserved / Reserved Ticketing",
    "Coach - Cleanliness",
    "Staff Behaviour",
    "Refund of Tickets",
    "Passenger Amenities",
    "Bed Roll",
    "Corruption / Bribery",
    "Miscellaneous",
    "none"
]

# Updated template for strict classification
template = """
You are a one-shot classification model designed to categorize complaints specifically related to railways and railway services.
Your task is to accurately classify the given complaint into one of the following predefined categories.
The classification must be precise, and you must output only one category without any additional text or explanation.
Ensure that the output is a single category that best fits the complaint. There should be no ambiguity or overlap between categories.

Categories:
{classes}

User input: {input_text}
Category:
"""

model = OllamaLLM(model="llama3.1")
prompt = ChatPromptTemplate.from_template(template)

# Define the chain
chain = prompt | model

def classify_input():
    input_text = input("You: ")
    result = chain.invoke({"input_text": input_text, "classes": "\n".join(classes)})
    print(f"Classified as: {result}")

if __name__ == "__main__":
    classify_input()
