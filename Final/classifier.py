from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Define the list of possible classes
classes = [
    "Coach - Maintenance/Facilities",
    "Electrical Equipment",
    "Medical Assistance",
    "Catering / Vending Services",
    "Passengers Beahviour",
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

model = OllamaLLM(model="llama3.2")
prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model

def classify_input(input_text):
    result = chain.invoke({"input_text": input_text, "classes": "\n".join(classes)})
    return result

# if __name__ == "__main__":
#     classify_input("some other passengers are attacking me")
