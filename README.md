# Image Caption Generator

This repository implements an Image Caption Generator using a deep learning model with attention mechanisms. The model is developed in Python using TensorFlow and TensorFlow Hub. The primary goal is to generate descriptive captions for images.

## Prerequisites

- Python 3.6 or higher
- TensorFlow 2.15.0
- TensorFlow Datasets
- TensorFlow Hub
- Matplotlib
- Numpy

## Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/singhsourav0/Image_Caption
   cd Image_Caption
## Training

The model is trained on a dataset of images, each paired with corresponding captions. The captions undergo preprocessing to include start and end tokens.

### Tokenization

The captions are tokenized using the `TextVectorization` layer from TensorFlow. Special tokens `<start>` and `<end>` are added to each caption.

### Model Architecture

#### Encoder

- Utilizes a pre-trained image feature extractor (Inception ResNet V2).
- Extracted features are reshaped and passed through a dense layer to obtain the encoder output.

#### Decoder

- Embedding layer for word inputs.
- Gated Recurrent Unit (GRU) layer with attention mechanism.
- Layer normalization and dense layer for output.

### Training

- Sparse categorical cross-entropy loss.
- Adam optimizer.

## Training Process

The model is trained using a batched dataset. The training process involves one epoch to demonstrate the workflow.
![badge](<https://miro.medium.com/v2/resize:fit:1000/format:webp/1*ENx4JZhq_9rwN2gYsuvHAQ.png>)

