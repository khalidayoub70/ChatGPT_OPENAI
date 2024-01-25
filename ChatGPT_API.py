import gradio as gr
import os
from langchain.llms import OpenAI
import tensorflow as tf


os.environ["OPENAI_API_KEY"] = "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"


llm = OpenAI(temperature=0.9)


def process_input(input_text):
   
    response_openai = llm(input_text)
    
   
    processed_output = your_tensorflow_operation(response_openai)

    return f"OpenAI Response: {response_openai}\nProcessed Output: {processed_output}"


def your_tensorflow_operation(response_openai):
   
    return tf.strings.upper(response_openai)


iface = gr.Interface(fn=process_input, inputs="text", outputs="text")
iface.launch()
