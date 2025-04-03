# Warning control
import warnings
warnings.filterwarnings('ignore')
from crewai import Agent, Task, Crew
import os
from utils import get_openai_api_key
openai_api_key = get_openai_api_key()
os.environ["OPENAI_MODEL_NAME"] = 'gpt-3.5-turbo'

# Cause Finder Agent
causefinder = Agent (
	role = “Cause Finder”,
	goal = “Locate possible anomalies within the process by opening and closing valves in the {process}”,
	backstory = “ You are an expert control room operator in the control room at a {process} plant “
		“You collect information from the transmitters and the position of the valves and you provide all possible cause should those readings on the transmitters be anomalous”
		“ Your work is the basis for the Cause Distinguisher so it can accurately find the correct reason for this anomaly”
allow_delegation = False,
verbose = True
verbose sees how the agent runs and its’ inner thoughts
)

# Cause Distinguisher Agent
causedistinguisher = Agent (
	role = “Cause Distinguisher”,
	goal = “To be able to use the information provided by the Cause Finder to select the correct possible cause that is the reason for the anomaly in the plant”,
	backstory = “You are working with the Cause Finder in the control room and your job is to receive information from the Cause Finder to be able to choose the correct reason the Cause Finder suggests for any anomaly in the process plant “
		“ Your work is the basis for the Effect Finder so it can predict what the effect of this anomaly you have chosen has on the entire process plant”
allow_delegation = False,
verbose = True
)

# Effect Finder Agent
effectfinder = Agent (
	role = “Effect Finder”,
	goal = “To be able to use the information provided by the Cause Distinguisher to predict the effect the anomaly has on the plant currently and any knock-on effects this anomaly may have if left untreated.”,
	backstory = “You are a process engineer working with the Cause Finder in the control room and your job is to receive information from the Cause Finder to be able to choose the correct reason the Cause Finder suggests for any anomaly in the process plant “
		“ Your work is the basis for the Solution Finder so it can figure out a suitable response to return the plant from its’ anomalous state back to normal operations”
allow_delegation = False,
verbose = True
)
# Solution Finder Agent
solutionfinder = Agent (
	role = “Solution Finder”,
	goal = “To be able to use the information provided by the Effect Finder and Cause Distinguisher to develop a suitable solution to fix the anomaly”,
	backstory = “You are a process engineer working alongside Effect Finder and Cause Distinguisher and your job is to develop a suitable solution to the problem you have received from the Cause Distinguisher “
		“ Your goal is to review the information from the Effect Finder and Cause Distinguisher to develop a practical and appropriate solution to return the process from its anomalous state back to normal operations”
		“ Your work is the basis for the Integrator agent so it can take the outputs of all the agents and output in a suitable format”
allow_delegation = False,
verbose = True
)
# Integrator Agent
Integrator = Agent (
	role = “Integrator”,
	goal = “To be able to use the information provided by all the agents and compile it into a easy to read and informative table that encompasses all the findings, possible reasons, the cause and the solution to the cause.”,
	backstory = “You are a process engineer working alongside Cause Finder, Effect Finder, Cause Distinguisher, Solution Finder and your job is to compile the information from all 4 agents into a table that is easily understood and contains very key and important information“
		“ Your work is the basis for the actual engineer who will read your work and act upon it if it is correct.”
allow_delegation = False,
verbose = True
)
