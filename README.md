![cCWXMAl30EqsKqFXPIfC9.png](https://cdn-uploads.huggingface.co/production/uploads/65bb837dbfb878f46c77de4c/3cnuydT5poHDy8AUI7nl4.png)

# **nsfw-image-detection**

nsfw-image-detection is a vision-language encoder model fine-tuned from siglip2-base-patch16-256 for multi-class image classification. Built on the SiglipForImageClassification architecture, the model is trained to identify and categorize content types in images, especially for explicit, suggestive, or safe media filtering.

Original Model : https://huggingface.co/prithivMLmods/siglip2-x256-explicit-content

---

## **Evals**

```py
Classification Report:
                     precision    recall  f1-score   support

      Anime Picture     0.8940    0.8718    0.8827      5600
             Hentai     0.8961    0.8935    0.8948      4180
             Normal     0.9100    0.8895    0.8997      5503
        Pornography     0.9496    0.9654    0.9574      5600
Enticing or Sensual     0.9132    0.9429    0.9278      5600

           accuracy                         0.9137     26483
          macro avg     0.9126    0.9126    0.9125     26483
       weighted avg     0.9135    0.9137    0.9135     26483
```

![download.png](https://cdn-uploads.huggingface.co/production/uploads/65bb837dbfb878f46c77de4c/psonZ0OXSjqgLRDkFtRTh.png)

---

# **Quick Start with Transformers🤗**


## **Install Dependencies**

```bash
!pip install transformers torch pillow gradio hf_xet
```

---

## **Inference Code**

```python
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
```



---
## **Demo Inference**

![Screenshot 2025-05-01 at 22-34-31 nsfw-image-detection.png](https://cdn-uploads.huggingface.co/production/uploads/65bb837dbfb878f46c77de4c/v_nyPFei3rdeQJBVn56Ku.png)
![Screenshot 2025-05-01 at 22-37-39 nsfw-image-detection.png](https://cdn-uploads.huggingface.co/production/uploads/65bb837dbfb878f46c77de4c/e3CQaCqVQHGSCoElYAF2O.png)
![Screenshot 2025-05-01 at 22-36-41 nsfw-image-detection(1).png](https://cdn-uploads.huggingface.co/production/uploads/65bb837dbfb878f46c77de4c/G33PB2O5l1hBu1vpQrUJ5.png)
![Screenshot 2025-05-01 at 22-39-08 nsfw-image-detection(1).png](https://cdn-uploads.huggingface.co/production/uploads/65bb837dbfb878f46c77de4c/4dcdejxTtTlbwcKf4z-Ck.png)
![Screenshot 2025-05-01 at 22-42-45 nsfw-image-detection(1).png](https://cdn-uploads.huggingface.co/production/uploads/65bb837dbfb878f46c77de4c/cCAOpVATVLDG470Yhcwvd.png)
![Screenshot 2025-05-01 at 22-43-35 nsfw-image-detection(1).png](https://cdn-uploads.huggingface.co/production/uploads/65bb837dbfb878f46c77de4c/gC8EkppCTBP-EsPbCNGtJ.png)

---

The model classifies each image into one of the following content categories:

```
Class 0: "Anime Picture"  
Class 1: "Hentai"  
Class 2: "Normal"  
Class 3: "Pornography"  
Class 4: "Enticing or Sensual"
```
---

## **Trained Models on This Dataset**

Several models have been trained using the NSFW\_MultiDomain dataset:

Dataset Used : https://huggingface.co/datasets/strangerguardhf/NSFW-MultiDomain

* 🔗 [https://huggingface.co/prithivMLmods/Mature-Content-Detection](https://huggingface.co/prithivMLmods/Mature-Content-Detection)
* 🔗 [https://huggingface.co/prithivMLmods/siglip2-x256-explicit-content](https://huggingface.co/prithivMLmods/siglip2-x256-explicit-content)
* 🔗 [https://huggingface.co/prithivMLmods/siglip2-x256p32-explicit-content](https://huggingface.co/prithivMLmods/siglip2-x256p32-explicit-content)
* 🔗 [https://huggingface.co/strangerguardhf/nsfw\_image\_detector](https://huggingface.co/strangerguardhf/nsfw_image_detector)

These models are fine-tuned on various architectures including SigLIP variants and custom classifiers for NSFW detection.
