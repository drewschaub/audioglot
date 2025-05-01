# Audioglot

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Detailed Usage](#detailed-usage)
  - [Transcription](#transcription)
  - [Translation](#translation)
  - [Dataset Creation](#dataset-creation)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview

**Audioglot** is a Python library for transcribing and translating your personal media library. It provides a suite of tools for processing audio files, extracting speech content, and translating it to your desired language. Whether you need to transcribe lectures, create subtitles for videos, or build training datasets for speech recognition models, Audioglot offers the functionality you need.

## Features

### **Audio Processing**
- **Voice Activity Detection (VAD)**: Precisely detect speech segments in audio files
- **Audio Format Support**: Process various audio formats, including extraction from video files

### **Transcription Engines**
- **Faster-Whisper**: Optimized Whisper implementation for improved performance
- **Whisper.cpp**: C++ port of OpenAI's Whisper model for efficient CPU-based transcription

### **Translation Services**
- **DeepL**: High-quality translations using DeepL's API
- **Google Translate**: Translation via Google's translation services

### **Dataset Creation**
- **Training Data Generation**: Tools to create and organize datasets for fine-tuning speech recognition models
- **Data Augmentation**: Methods to enhance and expand training datasets

### **Utilities**
- **Subtitle Generation**: Create subtitle files in various formats (SRT, VTT, etc.)
- **Batch Processing**: Efficiently process multiple files in sequence

## Installation

Install the package via PyPI using `pip`:

```bash
pip install audioglot
```
*Note: Ensure that you have Python 3.8 or higher installed.*

### Core Dependencies

Install the core dependencies using `pip`:

```bash
pip install -e .
```

### Optional Dependencies

For additional functionality:

```bash
# For DeepL translation support
pip install -e .[deepl]

# For Faster-Whisper support
pip install -e .[faster-whisper]

# For all features
pip install -e .[all]
```

## Quick Start

Here's a quick example to get you started with Audioglot:

```python
from audioglot.transcriber import create_transcriber
from audioglot.translator import create_translator
from audioglot.audio import extract_audio

# Extract audio from a video file
audio_path = extract_audio("path/to/video.mp4")

# Create a transcriber using Faster-Whisper
transcriber = create_transcriber("faster-whisper", model_size="base")

# Transcribe the audio
transcription = transcriber.transcribe(audio_path)
print(f"Transcription: {transcription}")

# Create a translator using DeepL
translator = create_translator("deepl", api_key="your-api-key")

# Translate the transcription to German
translation = translator.translate(transcription, target_language="DE")
print(f"Translation: {translation}")
```

## Detailed Usage

### Transcription

Audioglot supports multiple transcription engines:

```python
from audioglot.transcriber import create_transcriber

# Faster-Whisper
transcriber = create_transcriber("faster-whisper", model_size="large-v2")
result = transcriber.transcribe("audio.mp3")

# Whisper.cpp
transcriber = create_transcriber("whisper-cpp", model_path="/path/to/model.bin")
result = transcriber.transcribe("audio.mp3")
```

### Translation

Translate transcriptions using various services:

```python
from audioglot.translator import create_translator

# DeepL translation
translator = create_translator("deepl", api_key="your-api-key")
translation = translator.translate("Hello, world!", target_language="FR")

# Google Translate
translator = create_translator("google-translate")
translation = translator.translate("Hello, world!", target_language="ES")
```

### Dataset Creation

Build datasets for fine-tuning speech recognition models:

```python
from audioglot.dataset import DatasetBuilder

# Initialize a dataset builder
builder = DatasetBuilder(output_dir="whisper_dataset")

# Add files with transcriptions
builder.add_file("lecture1.mp3", transcript="path/to/transcript1.txt")
builder.add_file("interview.wav", transcript="path/to/transcript2.txt")

# Process and split the dataset
builder.process(test_split=0.2)
```

## Examples

### Transcribing a Video File

```python
from audioglot.transcriber import create_transcriber
from audioglot.audio import extract_audio
from audioglot.vad import segment_audio

# Extract audio from video
audio_path = extract_audio("lecture.mp4")

# Segment audio to find speech parts
segments = segment_audio(audio_path)

# Create transcriber
transcriber = create_transcriber("faster-whisper", model_size="medium")

# Transcribe each segment
for i, segment in enumerate(segments):
    start, end = segment
    text = transcriber.transcribe_segment(audio_path, start, end)
    print(f"Segment {i+1}: {text}")
```

### Creating Subtitles with Translation

```python
from audioglot.transcriber import create_transcriber
from audioglot.translator import create_translator
from audioglot.merger import create_subtitles

# Transcribe the audio
transcriber = create_transcriber("faster-whisper", model_size="base")
transcription = transcriber.transcribe("movie.mp3", with_timestamps=True)

# Translate the transcription
translator = create_translator("deepl", api_key="your-api-key")
translation = translator.translate(transcription, target_language="FR")

# Create subtitles
create_subtitles(transcription, "movie_en.srt")
create_subtitles(translation, "movie_fr.srt")
```

## Contributing

Contributions are welcome! Whether you're fixing bugs, improving documentation, or adding new features, your help is greatly appreciated.

1. **Fork the Repository**: Click the "Fork" button at the top right of the repository page.
2. **Clone Your Fork**:
    ```bash
    git clone https://github.com/your-username/audioglot.git
    ```
3. **Create a New Branch**:
    ```bash
    git checkout -b feature/YourFeatureName
    ```
4. **Make Your Changes**: Implement your feature or fix.
5. **Commit Your Changes**:
    ```bash
    git commit -m "Add feature: YourFeatureName"
    ```
6. **Push to Your Fork**:
    ```bash
    git push origin feature/YourFeatureName
    ```
7. **Create a Pull Request**: Go to the original repository and create a pull request from your fork.

For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.

## Contact

For any questions, suggestions, or contributions, please reach out:
- **Author**: Andrew Schaub
- **Linkedin**: https://www.linkedin.com/in/andrewjschaub
- **GitHub**: https://github.com/drewschaub/audioglot

---

Thank you for using Audioglot! We hope it serves as a valuable tool for your audio transcription and translation needs.
