from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import pathlib
import textwrap
import os

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
#I have set the environmental key through control panel
GEMINI_API_KEY=os.getenv('GEMINI_API_KEY')
genai.configure(api_key=GEMINI_API_KEY)

# Selecting gemini-pro for text based services and used print to confirm the model selected
model = genai.GenerativeModel('gemini-pro')
print(model.model_name)

# The below line is where you can pu the prompt for response
response = model.generate_content("Hi, HOW ARE YOU?")
print(response.text)
#to_markdown(response.text)

# Feedback for each  prompt
response.prompt_feedback



