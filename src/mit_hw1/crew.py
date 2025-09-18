from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class MitHw1():
    """MitHw1 crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
   
    @agent
    def graduate_student_advisor(self) -> Agent:
        return Agent(
            config=self.agents_config['graduate_student_advisor'], # type: ignore[index]
            verbose=True
        ) 
    @agent
    def graduate_student_novice(self) -> Agent:
        return Agent(
            config=self.agents_config['graduate_student_novice'], # type: ignore[index]
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def introduction_task(self) -> Task:
        return Task(
            config=self.tasks_config['introduction_task'], # type: ignore[index]
            output_file="./outputs/advisor_introduction.md"
        )
    
    @task
    def background_explanation_task(self) -> Task:
        return Task(
            config=self.tasks_config['background_explanation_task'], # type: ignore[index]
            output_file="./outputs/novice_background.md" 
        )

    @task
    def practical_task(self) -> Task:
        return Task(
            config=self.tasks_config['practical_task'], # type: ignore[index]
            output_file="./outputs/advisor_interview_prep.md"
        )
    
    @task
    def novice_study_notes_task(self) -> Task:
        return Task(
            config=self.tasks_config['novice_study_notes_task'], # type: ignore[index]
            output_file="./outputs/novice_study_guide.md" 
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the MitHw1 crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
