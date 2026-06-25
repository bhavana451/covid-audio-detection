# COVID-19 Detection using Audio Data using Deep Learning

## Overview

This project aims to detect COVID-19 from respiratory audio signals using Deep Learning techniques. The system processes audio recordings, extracts relevant features, and classifies whether the audio sample is associated with COVID-19. The project demonstrates the application of Artificial Intelligence and Deep Learning in healthcare and audio signal analysis.

## Objectives

* Preprocess and clean raw audio recordings
* Extract meaningful features from audio signals
* Develop and train deep learning models for classification
* Evaluate model performance and generate predictions
* Build an end-to-end audio classification pipeline

## Methodology

1. Audio data preprocessing and cleaning
2. Feature extraction from audio recordings
3. Model development using CNN and LSTM architectures
4. Model training and validation
5. Prediction and performance evaluation

## Project Architecture

Audio Data → Preprocessing → Feature Extraction → CNN-LSTM Model → Prediction & Evaluation

## Technologies Used

* Python
* TensorFlow / Keras
* Pandas
* NumPy
* Deep Learning (CNN, LSTM)
* Audio Signal Processing

## Project Structure

```text
covid-audio-detection/
│
├── preprocess.py      # Audio preprocessing and feature extraction
├── training.py        # Model training and validation pipeline
├── Predict.py         # Prediction and inference pipeline
├── CNNLSTM.py         # CNN-LSTM model architecture
├── README.md
```

## How to Run

### 1. Install Dependencies

```bash
pip install tensorflow pandas numpy
```

### 2. Preprocess the Audio Data

```bash
python preprocess.py
```

### 3. Train the Model

```bash
python training.py
```

### 4. Generate Predictions

```bash
python Predict.py
```

## Key Learning Outcomes

* Deep Learning for audio classification
* Data preprocessing and feature engineering
* CNN and LSTM model development
* Model training and evaluation workflows
* Building end-to-end machine learning pipelines

## Note

Large datasets and generated model files are not included in this repository due to GitHub file size limitations.
