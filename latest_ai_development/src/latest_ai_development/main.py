#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from latest_ai_development.crew import LatestAiDevelopmentCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information
topic = input("Enter the topic you want news on:")

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': topic,
        'current_year': str(datetime.now().year)
    }
    
    try:
        LatestAiDevelopmentCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": topic
    }
    try:
        LatestAiDevelopmentCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        LatestAiDevelopmentCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": topic
    }
    try:
        LatestAiDevelopmentCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
	
def run_search_task(topic):
    """
    Run the research task using the provided topic.
    """
    try:
        # Create an instance of the crew and invoke the research task
        crew_instance = LatestAiDevelopmentCrew()
        inputs = {
            'topic': topic,
            'current_year': str(datetime.now().year)
        }
        # Trigger the task
        crew_instance.before_kickoff_function(inputs)
        result = crew_instance.research_task()  # Assuming this triggers the actual task
        crew_instance.after_kickoff_function(result)
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the search task: {e}")

# Optionally, include a block to allow running from command line
if __name__ == "__main__":
    topic = input("Enter the topic you want news on:")
    run_search_task(topic)
