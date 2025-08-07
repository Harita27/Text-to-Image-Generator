# Text-to-Image Generator (Stable Diffusion)

This project is a simple Text-to-Image Generative AI application using a pre-trained Stable Diffusion model.  
You can generate images from text prompts using a Python GUI (Tkinter) or Streamlit frontend.

## Features

- Generate images from text prompts using Stable Diffusion
- Easy-to-use interface (Streamlit or Tkinter)
- Load your own fine-tuned model from the `my-model` directory

## Setup

1. **Clone this repository**  
2. **Install dependencies:**  
   ```
   pip install -r requirements.txt
   ```
3. **Download or fine-tune your model and save it to `my-model/`**  
   (See `train.py` for an example.)

4. **Run the app:**  
   - For Streamlit:  
     ```
     streamlit run app.py
     ```
   - For Tkinter GUI:  
     ```
     python app.py
     ```

## Directory Structure

```
Brainwave_Matrix_Internn/
│
├── app.py
├── train.py
├── requirements.txt
├── my-model/
│   ├── config.json
│   ├── model.bin
│   └── ...
└── data/ (optional)
```
