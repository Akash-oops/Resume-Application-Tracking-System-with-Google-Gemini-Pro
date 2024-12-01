import google.generativeai as genai

# Authenticate (requires API key)
'''genai.configure(api_key="AIzaSyDDCHjyX0kEo1I-CLwKGSlNFuAp1B1fRmg")

response = genai.models.text.generate(
    model="text-bison-001",  # Specify the model
    prompt="Tell me a story about AI",
    max_output_tokens=256
)

print(response.result)'''

from langchain_google_genai import PaLM
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the API key
api_key = os.getenv("AIzaSyDDCHjyX0kEo1I-CLwKGSlNFuAp1B1fRmg")
model = PaLM(api_key=api_key)

prompt = "Tell me a story about AI."
response = model.complete(prompt)
print(response)

