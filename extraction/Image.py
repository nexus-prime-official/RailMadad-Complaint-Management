import base64
from io import BytesIO
from langchain_ollama import OllamaLLM
from PIL import Image

# Converting the image to base64
def convert_to_base64(uploaded_file):
    """
    Convert the uploaded image file (BytesIO) to Base64 encoded strings.

    :param uploaded_file: Uploaded image file from Streamlit
    :return: Base64 string
    """
    image = Image.open(uploaded_file)
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str

def describe_image(image_path) -> str:
    """
    Describe the image using the Ollama model.
    """
    pil_img = Image.open(image_path)
    img_base64 = convert_to_base64(pil_img)

    # New template focused on human interaction and observable issues inside a train coach
    template = """
    You are an AI model specialized in analyzing images taken inside railway coaches. 
    Your task is to provide a clear and concise two-line description of the primary problem or complaint that a user might have based on the visible interactions or issues among the people in the image.
    Focus on observable interactions, staff behavior, passenger comfort, or any visible problems within the coach. Ignore any irrelevant aspects and do not generate information about unrelated settings like train platforms.

    Image context: Based on the provided image, summarize the main issue or complaint in two lines.
    Problem Description:
    """

    llm = OllamaLLM(model="llava:7b")

    llm_with_image_context = llm.bind(images=[img_base64])
    result = llm_with_image_context.invoke(template)
    return result

# Running the description function
description = describe_image("extraction/sample.jpg")
print(description)
