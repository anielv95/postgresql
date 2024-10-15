import vertexai
from vertexai.preview.generative_models import GenerativeModel, Image, ChatSession
import os 
from dotenv import load_dotenv, find_dotenv
import openai
from langchain import PromptTemplate
from langchain_openai import ChatOpenAI


_ = load_dotenv(find_dotenv())

PROJECT_ID = os.environ["PROJECT_ID"]
REGION = os.environ["REGION"]
vertexai.init(project=PROJECT_ID, location=REGION)

# IMAGE_FILE = "images/download.jpg"
# image = Image.load_from_file(IMAGE_FILE)

# generative_multimodal_model = GenerativeModel("gemini-1.5-flash-002")
model = GenerativeModel("gemini-1.0-pro")#Meta-Llama-3-8B-Instruct
# model = GenerativeModel("Llama3-405b-instruct-maas")#Meta-Llama-3-8B-Instruct
chat = model.start_chat()

def get_chat_response(chat: ChatSession, prompt: str):
    response = chat.send_message(prompt)
    return response.text



# response = generative_multimodal_model.generate_content(["What is shown in this image?", image])

# print(response)

prompt = "Hello."
print(get_chat_response(chat, prompt))

prompt = "What are all the colors in a rainbow?"
print(get_chat_response(chat, prompt))

prompt = "Why does it appear when it rains?"
print(get_chat_response(chat, prompt))

#----------------------------------------------------------------

# client = openai.OpenAI(
#     base_url=f"https://{MODEL_LOCATION}-aiplatform.googleapis.com/v1beta1/projects/{PROJECT_ID}/locations/{MODEL_LOCATION}/endpoints/openapi/chat/completions?",
#     api_key=credentials.token,
# )