from diffusers import StableDiffusionPipeline
import torch

# Check if CUDA is available
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# Load the model (fp16 for speed if GPU supports it)
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5", 
    torch_dtype=torch.float16 if device == "cuda" else torch.float32,
    safety_checker=None  # Disable safety checker for more creative generations
).to(device)

# Enable memory efficient attention if available
if hasattr(pipe, "enable_attention_slicing"):
    pipe.enable_attention_slicing()

# This will be imported by app.py
__all__ = ['pipe']
