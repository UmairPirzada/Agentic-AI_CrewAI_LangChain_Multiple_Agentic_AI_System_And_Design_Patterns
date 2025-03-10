from crewai.flow.flow import Flow, start, listen

from dotenv import load_dotenv,  find_dotenv

from litellm import completion
import os


_: bool = load_dotenv(find_dotenv())


class PanaFlow(Flow):

@start
def generate_topic (self):
    self.topic = completion(
        model="gemini-2.0-flash",
        messages=[
