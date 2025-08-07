import streamlit as st
from PIL import Image
from diffusers import StableDiffusionPipeline
import torch
@st.cache_resource
def load_model():
    pipe = StableDiffusionPipeline.from_pretrained(
        "my-model",
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    )
    if torch.cuda.is_available():
        pipe = pipe.to("cuda")
    return pipe
pipe = load_model()
st.set_page_config(page_title="Text-to-Image Generator", layout="centered")
st.title("Text-to-Image Generator (Stable Diffusion)")
prompt = st.text_input("Enter your prompt:", "A futuristic cityscape")
if st.button("Generate Image"):
    if not prompt.strip():
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Generating image..."):
            image = pipe(prompt).images[0]
            image.thumbnail((512, 512))  
            st.image(image, caption="Generated Image", use_column_width=True)
        st.success("Done!")

