import gradio as gr



from latest_ai_development.main import run_search_task  # Import the run_search_task function from main.py

def run_gradio_search_task(topic):
    """
    Gradio function to run the search task and display the result.
    """
    try:
        result = run_search_task(topic)  # Call the function from main.py
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
    interface.launch(share=True)  # share=True for a public link