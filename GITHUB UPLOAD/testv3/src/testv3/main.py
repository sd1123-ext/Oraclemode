#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from testv3.crew import Testv3

from PIL import Image

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

file = open(r"C:\Users\sd1123\testv3\src\testv3\crewaibriefv2_(notnetworkx).txt")
info = file.read()
file.close()

alarm = 'PDT105 has a reading of 0.42'


def run():
    """
    Run the crew.
    """
    inputs = {
        'process': info,
        'anomaly': alarm,
    }

    try:
        Testv3().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'process': info,
        'anomaly': alarm,
    }
    try:
        Testv3().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Testv3().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'process': info,
        'anomaly': alarm,
    }
    try:
        Testv3().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
