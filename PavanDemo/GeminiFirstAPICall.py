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

# Selectin gemini-pro for text based services and used print to confirm the model selected
model = genai.GenerativeModel('gemini-pro')
print(model.model_name)

# The below line is where you can put the prompt for response
response = model.generate_content("Hi,Waht is a Walnut?")

# The below line ccatches the repsonse and print, OTOH you use markdown for formatting.
#print(response.text)
to_markdown(response.text)

# Feedback for each  prompt
#print(response.prompt_feedback)

# The model gemerates multiple responses for a single prompt, you can see them using candidates
#print(response.candidates)

# STREAMING the response for a completion




