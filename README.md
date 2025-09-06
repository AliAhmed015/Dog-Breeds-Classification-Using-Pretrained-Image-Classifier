# Dog Breed Classifier Using Pretrained CNN Models

**This project was developed as part of the Future AWS AI Scientist Nanodegree.**

This is a Python command-line application that classifies pet images using pretrained Convolutional Neural Networks (CNNs). The tool compares the predicted labels with true labels extracted from image filenames, identifies whether the image represents a dog, and evaluates the performance of different model architectures.

This project demonstrates practical use of **transfer learning**, **modular programming**, and **command-line interface (CLI) design**, and was developed as part of an AI curriculum.

---

## Table of Contents

- [Project Overview](#project-overview)  
- [Key Features](#key-features)  
- [How It Works](#how-it-works)  
- [Supported CNN Architectures](#supported-cnn-architectures)  
- [Usage](#usage)  
  - [Command-Line Arguments](#command-line-arguments)  
- [Requirements](#requirements)  
- [Installation](#installation) 
- [Evaluation Metrics](#evaluation-metrics)  

---

## Project Overview

This application allows you to classify pet images by:

1. Extracting labels from image filenames.
2. Using a pretrained CNN model to classify each image.
3. Comparing predicted labels with true labels.
4. Determining whether the true and predicted labels refer to actual dog breeds.
5. Calculating performance metrics for classification accuracy.

The program supports three widely used CNN architectures — **VGG**, **ResNet**, and **AlexNet** — which are loaded from the `torchvision` library.

This project provides a hands-on understanding of:

- Applying transfer learning for image classification.
- Parsing and validating command-line inputs.
- Evaluating model performance.
- Designing modular, maintainable code.

---

## Key Features

- Classifies images using pretrained CNN models (VGG, ResNet, AlexNet).
- Automatically extracts labels from filenames.
- Verifies whether the labels refer to dog breeds using a custom list.
- Calculates multiple classification accuracy metrics.
- Clean and modular code structure for maintainability.
- Dynamically handles file paths using Python’s `os` module.
- Includes optional runtime tracking.
- Works with any compatible image dataset.

---

## How It Works

1. **Input Parsing**: CLI arguments are parsed using `argparse`.
2. **Label Extraction**: Filenames like `golden_retriever_00123.jpg` are converted to labels like `"golden retriever"`.
3. **Classification**: Each image is passed through the selected CNN model, and the predicted label is retrieved.
4. **Label Comparison**: The predicted label is compared to the true label for correctness.
5. **Dog Verification**: A dictionary of valid dog names (`dognames.txt`) is used to verify whether both true and predicted labels refer to dogs.
6. **Statistical Evaluation**: Performance statistics are computed including accuracy for dog detection and breed matching.
7. **Results Output**: Results are printed to the terminal including counts and accuracy metrics.

---

## Supported CNN Architectures

The following pretrained models are supported via `torchvision.models`:

| Model    | Description |
|----------|-------------|
| **VGG**     | Deep CNN with uniform architecture, commonly used for transfer learning. |
| **ResNet**  | Incorporates residual connections, enabling very deep networks without vanishing gradients. |
| **AlexNet** | Earlier deep CNN, lightweight and suitable for quick testing. |

---

## Usage

### Command-Line Arguments

| Argument       | Description                                      | Default         |
|----------------|--------------------------------------------------|-----------------|
| `--dir`        | Path to the folder containing images             | `pet_images/`   |
| `--arch`       | CNN model to use: `vgg`, `resnet`, or `alexnet`  | `vgg`           |
| `--dogfile`    | Text file with list of valid dog breed names     | `dognames.txt`  |

---

## Requirements

- Python 3.6 or higher  
- PyTorch  
- torchvision  
- numpy  
- pillow  
- argparse  
- time  

---

## Installation

### Clone the repository:

```bash
git clone https://github.com/yourusername/dog-breed-classifier.git
cd dog-breed-classifier
pip install torch torchvision numpy pillow
```

---


## Evaluation Metrics

The program computes the following statistics:

- Total number of images
- Number of dog images
- Number of non-dog images
- Correctly classified dogs
- Correctly classified non-dogs
- Correctly classified dog breeds

Accuracy percentages for:

- Dog identification
- Non-dog classification
- Dog breed match
- Overall label match


