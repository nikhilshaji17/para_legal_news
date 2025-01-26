import gradio as gr
#import sambanova_gradio
#gr.load("Meta-Llama-3.3-70B-Instruct", src=sambanova_gradio.registry, accept_token=True).launch()

import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

# Get the SambaNova model and API key from environment variables
MODEL_NAME = os.getenv("MODEL")
SAMBANOVA_API_KEY = os.getenv("SAMBANOVA_API_KEY")


from latest_ai_development.main import run #run_search_task  # Import the run_search_task function from main.py

if not MODEL_NAME or not SAMBANOVA_API_KEY:
    raise ValueError("MODEL or SAMBANOVA_API_KEY not set in the .env file.")

def run_gradio_search_task(topic):
    """
    Gradio function to run the search task and display the result.
    """
    try:
        result = run(topic) #run_search_task(topic)  # Call the function from main.py
        return result
    except Exception as e:
        return f"Error: {e}"

# Create the Gradio interface
interface = gr.Interface(
    fn=run_gradio_search_task,  # The function that Gradio will call
    inputs=gr.Textbox(label="Enter Topic for Research Task"),  # User input
    outputs=gr.Textbox(label="Task Output")  # Display the result
)

# Launch the Gradio app
if __name__ == "__main__":
	topic = input("Enter the topic you want news on:")
	interface.launch(share=True)  # share=True for a public link