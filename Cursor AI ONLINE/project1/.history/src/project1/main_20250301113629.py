from crewai.flow.flow import Flow, start, listen
from 

from dotenv import load_dotenv,  find_dotenv

from litellm import completion
import os


_: bool = load_dotenv(find_dotenv())


class PanaFlow(Flow):

@start
def generate_topic (self):
    self.topic = completion(
        model="gemini/gemini-2.0-flash",
        messages=[
            
            {"role": "user", "content": """Generate a topic for a new blog post"}
        ],

        prompt="Generate a topic for a new blog post",
        max_tokens=100,
        temperature=0.5,
      
