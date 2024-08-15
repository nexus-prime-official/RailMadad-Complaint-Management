from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Define the list of possible classes
classes = [
    "Facilities for Women with Special needs",
    "Electrical Equipment",
    "Medical Assistance",
    "Catering / Vending Services",
    "Facilities for Persons with Disabilities",
    "Water Availability",
    "Goods",
    "Catering & Vending Services",
    "Punctuality",
    "Unreserved Ticketing",
    "Security",
    "Reserved Ticketing",
    "Luggage / Parcels",
    "Coach - Cleanliness",
    "Cleanliness",
    "Staff Behaviour",
    "Refund of Tickets",
    "Passenger Amenities",
    "Bed Roll",
    "Corruption / Bribery",
    "Coach - Maintenance",
    "Miscellaneous"
]

# Create a template for classification
template = """
Classify the user input into one of the following categories:
{classes}

User input: {input_text}
Category:
"""

model = OllamaLLM(model="llama3.1")
prompt = ChatPromptTemplate.from_template(template)

# Define the chain
chain = prompt | model

def classify_input():
    print("Welcome to the classification chatbot. Type 'exit' to quit.")
    while True:
        input_text = input("You: ")
        if input_text.lower().strip() == "exit":
            break
        result = chain.invoke({"input_text": input_text, "classes": "\n".join(classes)})
        print(f"Classified as: {result}")

if __name__ == "__main__":
    classify_input()
