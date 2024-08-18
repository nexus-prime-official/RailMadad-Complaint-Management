import base64
from io import BytesIO

from langchain_ollama import OllamaLLM
from PIL import Image


# Converting the immage to base64
def convert_to_base64(pil_image):
    """
    Convert PIL images to Base64 encoded strings

    :param pil_image: PIL image
    :return: Re-sized Base64 string
    """

    buffered = BytesIO()
    pil_image.save(buffered, format="JPEG")  # You can change the format if needed
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str


def describe_image(image_path) -> str:
    """
    Describe the image using the Ollama model
    """

    pil_img = Image.open(image_path)
    img_base64 = convert_to_base64(pil_img)

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
        "none",
    ]

    # Template for accurate indoor analysis focused on genuine negative aspects
    template = """
    You are an advanced image analysis model designed to thoroughly examine images of the interiors of railway coaches.
    Your task is to accurately identify and describe only real and observable negative aspects or potential issues inside the coach. Avoid exaggeration or hallucination—focus solely on genuine problems, and describe them with the appropriate level of severity.
    Analyze issues related to seating, passenger discomfort, disturbances, cleanliness, and other indoor aspects of railway services. Disregard any positive observations.

    Categories:
    {classes}

    Image context: Analyze the provided image and describe only real, observable negative aspects or potential issues inside the railway coach. For each problem identified, specify the severity and the most appropriate category. Ensure the description is precise and grounded in what is visible, without overstatement.
    Detailed Description:
    Category:
    Severity:
    """

    llm = OllamaLLM(model="llava:7b")

    llm_with_image_context = llm.bind(images=[img_base64])
    result = llm_with_image_context.invoke(template)
    return result
