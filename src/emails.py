import vertexai
from vertexai.preview.generative_models import GenerativeModel, ChatSession
import os 
from dotenv import load_dotenv, find_dotenv


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
    return response.text, response



# response = generative_multimodal_model.generate_content(["What is shown in this image?", image])

# print(response)

prompt = "You're a helpful assistant. Write a short email in json format about sports. Always use 'Subject' and 'Body' as the keys in the answer"
ans, response = get_chat_response(chat, prompt)
#print(ans, response)

# prompt = "What are all the colors in a rainbow?"
# print(get_chat_response(chat, prompt))

# prompt = "Why does it appear when it rains?"
# print(get_chat_response(chat, prompt))

#----------------------------------------------------------------

# client = openai.OpenAI(
#     base_url=f"https://{MODEL_LOCATION}-aiplatform.googleapis.com/v1beta1/projects/{PROJECT_ID}/locations/{MODEL_LOCATION}/endpoints/openapi/chat/completions?",
#     api_key=credentials.token,
# )




text = "```json\n{\n  \"Subject\": \"Sports Roundup\",\n  \"Body\": \"## 🏀⚾🏈⚽ 🎾🏓🏸🏏🏒\n\nThis week in sports, there were some exciting developments across various disciplines. Here\'s a quick rundown:\n\n**🏀 NBA:** \n* The Golden State Warriors clinched their 8th NBA championship in their history, defeating the Boston Celtics in a thrilling six-game series. Stephen Curry was once again phenomenal, earning Finals MVP honors.\n\n**⚾ MLB:** \n* Shohei Ohtani continues to dominate both at the plate and on the mound. He recently hit his 30th home run of the season and is also among the league leaders in wins and ERA as a pitcher.\n* The New York Yankees are running away with the American League East, holding a comfortable lead over their rivals. Aaron Judge is on pace for a historic season, chasing Roger Maris\'s 61-homer record.\n\n**🏈 NFL:** \n* Preseason NFL games are underway, giving fans a glimpse of what to expect in the upcoming season. Several rookies have impressed so far, including quarterbacks Trevor Lawrence and Zach Wilson.\n* The reigning Super Bowl champion Los Angeles Rams are looking to repeat, but they face stiff competition from other contenders like the Kansas City Chiefs and Tampa Bay Buccaneers.\n\n**⚽ FIFA World Cup:** \n* With less than a year to go until the FIFA World Cup in Qatar, excitement is building across the globe. Several nations have already qualified, including host Qatar, Brazil, and Argentina.\n* Fans are eagerly anticipating the performance of star players like Lionel Messi, Cristiano Ronaldo, and Kylian Mbappé.\n## Other Sports News\n\n* In tennis, Novak Djokovic continues his reign at the top of the men\'s rankings. He recently won his 21st Grand Slam title at Wimbledon, tying the record held by Roger Federer and Rafael Nadal.\n* The Tokyo Olympics were a resounding success, showcasing incredible athletic performances across diverse sports.\n* Cricket fans around the world are looking forward to the upcoming ICC Men\'s T20 World Cup in Australia. India and England are among the favorites to win the tournament.\n\nLet me know if you\'d like more in-depth information on any specific sport or event.\"\n}\n```"

