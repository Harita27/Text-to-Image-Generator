
# 🖼️ Text-to-Image Generator (Stable Diffusion + Streamlit)

A simple **Streamlit web app** that uses **Stable Diffusion** (via Hugging Face Diffusers) to generate images from text prompts.  
Built with **PyTorch**, **Diffusers**, and **Streamlit**.

---

## 🚀 Features

- ✍️ Enter any text prompt and generate an AI image  
- ⚡ Uses **Stable Diffusion** from Hugging Face  
- 🖥️ GPU acceleration with CUDA (if available)  
- 🎨 Automatically resizes output to **512x512**  
- 🌐 Clean, interactive **Streamlit UI**  

---

## 🛠 Tech Stack

- **Frontend:** Streamlit  
- **Backend / ML:** Hugging Face Diffusers, PyTorch, Stable Diffusion  
- **Image Handling:** PIL (Pillow)  

---

## 📂 Project Structure

```

text-to-image-generator/
├── app.py          # Main Streamlit app
├── requirements.txt # Dependencies
└── README.md       # Documentation

````

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/text-to-image-generator.git
cd text-to-image-generator
````

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, install manually:

```bash
pip install streamlit pillow diffusers torch torchvision
```

---

## ▶️ Running the App

```bash
streamlit run app.py
```

Then open the link provided (usually: `http://127.0.0.1:8501`).

---

## 🖥️ Usage

1. Enter a **text prompt** (e.g., *"A futuristic cityscape at sunset"*)
2. Click **Generate Image**
3. Wait while the model generates the image
4. View your AI-generated image in the app 🎉

---

## 🔮 Future Improvements

* Support for **multiple generated images per prompt**
* Add **image download button**
* Customize **image resolution** (e.g., 768x768)
* Use **other Stable Diffusion checkpoints** (anime, realistic, etc.)
* Deploy to **Streamlit Cloud / Hugging Face Spaces / Azure**

---

## 📜 License

Open-source for learning and personal use.

---

## 🙌 Acknowledgements

* [Hugging Face Diffusers](https://github.com/huggingface/diffusers)
* [PyTorch](https://pytorch.org/)
* [Streamlit](https://streamlit.io/)


