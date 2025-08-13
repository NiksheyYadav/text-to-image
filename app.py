import gradio as gr
from texttoimage import pipe as text_to_image_pipe

def generate(prompt):
    try:
        image = text_to_image_pipe(prompt).images[0]
        return image
    except Exception as e:
        print(f"Error generating image: {e}")
        return None

# Create a more user-friendly interface
with gr.Blocks(title="Text to Image Generator", theme=gr.themes.Soft()) as demo:
    gr.Markdown("# Text to Image Generator")
    with gr.Row():
        with gr.Column():
            prompt = gr.Textbox(label="Enter your prompt", placeholder="A beautiful landscape with mountains and a lake...")
            generate_btn = gr.Button("Generate Image")
        with gr.Column():
            output_image = gr.Image(label="Generated Image")
    
    generate_btn.click(fn=generate, inputs=prompt, outputs=output_image)

# Launch with CORS enabled and better error handling
if __name__ == "__main__":
    demo.launch(server_name="localhost", server_port=5000, share=False, show_error=True)
