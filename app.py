import gradio as gr
from transformers import AutoImageProcessor, SiglipForImageClassification
from PIL import Image
import torch

# Load model and processor
model_name = "strangerguardhf/nsfw_image_detection"  # Replace with your model path if needed
model = SiglipForImageClassification.from_pretrained(model_name)
processor = AutoImageProcessor.from_pretrained(model_name)

# ID to Label mapping
id2label = {
    "0": "Anime Picture",
    "1": "Hentai",
    "2": "Normal",
    "3": "Pornography",
    "4": "Enticing or Sensual"
}

def classify_explicit_content(image):
    image = Image.fromarray(image).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probs = torch.nn.functional.softmax(logits, dim=1).squeeze().tolist()

    prediction = {
        id2label[str(i)]: round(probs[i], 3) for i in range(len(probs))
    }

    return prediction

# Gradio Interface
iface = gr.Interface(
    fn=classify_explicit_content,
    inputs=gr.Image(type="numpy"),
    outputs=gr.Label(num_top_classes=5, label="Predicted Content Type"),
    title="nsfw-image-detection",
    description="Classifies images into explicit, suggestive, or safe categories (e.g., Hentai, Pornography, Normal)."
)

if __name__ == "__main__":
    iface.launch()
