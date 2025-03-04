#!/usr/bin/env python
import sys
import warnings

from summarize_docs_project.crew import SummarizeDocsProject

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run(file_path):
    """
    Run the crew.
    """
    inputs = {
        #You can input a Doc path or URL
        'filepath': file_path,
    }
    
    try:
        result = SummarizeDocsProject().crew().kickoff(inputs=inputs)
        print(result)
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train(file_path):
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
            #You can input a Doc path or URL
            'filepath': file_path,
        }
    try:
        SummarizeDocsProject().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        SummarizeDocsProject().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test(file_path):
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        #You can input a Doc path or URL
        'filepath': file_path,
    }
    try:
        SummarizeDocsProject().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

# if __name__ == "__main__":
#     run()  # Só executa se o script for rodado diretamente