from crewai.flow.flow import Flow, start, listen
from dotenv import load_dotenv,  find_dotenv
from litellm import completion

_: bool = load_dotenv(find_dotenv())

class PanaFlow(Flow):

    @start()
    def generate_topic (self):
        response = completion(
            model="gemini/gemini-2.0-flash",
            messages=[
                
                {"role": "user",
                 "content": "Share the most trending topic for 2025"
                 }
            ],

            # max_tokens=100,
            # temperature=0.5,
      
        )
        self.state["topic"] = response['choices'][0]['message']['content']

        print(f"Step 1 Topic: {self.state['topic']}")


def kickoff();
flow = PanaFlow()
response = flow.kickoff()
print("RESPONSE", response)

if __name__ == "__main__":
  