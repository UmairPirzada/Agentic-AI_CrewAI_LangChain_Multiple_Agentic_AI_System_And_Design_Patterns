
from crewai.flow.flow import Flow, listen, start
from dotenv import load_dotenv
from litellm import completion

# model = "gemini/gemini-1.5-flash"
# API_KEY = "AIzaSyBWHFFWFZxjgw454xDJ7Av_Af_7HVrFf4M"
class ExampleFlow(Flow):
    model = "gemini/gemini-1.5-flash"

    @start()
    def generate_city(self):
        print("Starting flow")
        # Each flow state automatically gets a unique ID
        print(f"Flow State ID: {self.state['id']}")

        response = completion(
            model=self.model,
            api_key=API_KEY,
            messages=[
                {
                    "role": "user",
                    "content": "Return the name of a random city in the world.",
                },
            ],
        )

        random_city = response["choices"][0]["message"]["content"]
        # Store the city in our state
        self.state["city"] = random_city
        print(f"Random City: {random_city}")

        return random_city

    @listen(generate_city)
    def generate_fun_fact(self, random_city):
        response = completion(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": f"Tell me a fun fact about {random_city}",
                },
            ],
        )

        fun_fact = response["choices"][0]["message"]["content"]
        # Store the fun fact in our state
        self.state["fun_fact"] = fun_fact
        return fun_fact

def kickoff():
    """ Starts the City Routing Workflow """
    obj = ExampleFlow()
    obj.kickoff()

def plot():
    """ Generates a visualization of the workflow """
    obj = ExampleFlow()
    obj.plot()



# flow = ExampleFlow()
# result = flow.kickoff()

# print(f"Generated fun fact: {result}")
