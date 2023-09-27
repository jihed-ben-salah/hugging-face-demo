from transformers import pipline
import gradio as gr


model = pipeline("summarization")

def predict(prompt):
    summary = model(prompt)[0]["summary_text"]
    return summary

with gr.Blocks() as demo:
    textbox = gr.Textbox(placeholder="ENTER text block to summarize",lines=4)
    gr.Interface(fn=predict,inputs=texbox,outputs="text")

demo.lunch()