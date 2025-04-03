from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Testv3():
    """Testv3 crew"""

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools

#    @agent
#    def imageanalyser(self) -> Agent:
#        return Agent(
#            config=self.agents_config['imageanalyser'],
#            verbose=True,
#            multimodal=True,
             # Multimodal allows the agent to read text and non-text inputs
#        )

    @agent
    def causefinder(self) -> Agent:
        return Agent(
            config=self.agents_config['causefinder'],
            verbose=True,
        )

    @agent
    def causedistinguisher(self) -> Agent:
        return Agent(
            config=self.agents_config['causedistinguisher'],
            verbose=True,
        )

    @agent
    def effectfinder(self) -> Agent:
        return Agent(
            config=self.agents_config['effectfinder'],
            verbose=True,
        )

    @agent
    def solutionfinder(self) -> Agent:
        return Agent(
            config=self.agents_config['solutionfinder'],
            verbose=True,
        )

    @agent
    def integrator(self) -> Agent:
        return Agent(
            config=self.agents_config['integrator'],
            verbose=True,
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
#    @task
#    def analyseimage_task(self) -> Task:
#        return Task(
#            config=self.tasks_config['analyseimage_task'],
#        )

    @task
    def findcause_task(self) -> Task:
        return Task(
            config=self.tasks_config['findcause_task'],
        )

    @task
    def distinguishcause_task(self) -> Task:
        return Task(
            config=self.tasks_config['distinguishcause_task'],
            output_file='report.md'
        )

    @task
    def findeffect_task(self) -> Task:
        return Task(
            config=self.tasks_config['findeffect_task'],
            output_file='report.md'
        )

    @task
    def findsolution_task(self) -> Task:
        return Task(
            config=self.tasks_config['findsolution_task'],
        )

    @task
    def integrateinfo_task(self) -> Task:
        return Task(
            config=self.tasks_config['integrateinfo_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Testv3 crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
