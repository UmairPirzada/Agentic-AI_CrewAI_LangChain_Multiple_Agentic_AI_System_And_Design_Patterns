from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class DevCrew:
    """Dev Crew"""
    
    @agent
    def junior_python_developer(self) -> Agent:
        return Agent(
            
        )
        
    @agent
    def senior_python_developer(self) -> Agent:
        return Agent(
            config=self.agents_config["senior_python_developer"],
        )
        
        
    @task
    def write_code(self) -> Task:
        return Task(
            config=self.tasks_config["write_code"],
        )
    @task
    def review_code(self) -> Task:
        return Task(
            config=self.tasks_config["review_code"],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Research Crew"""

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
