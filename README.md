# OpenAI Speech-to-Text with Formatting

This project utilizes the **OpenAI Whisper** model for speech-to-text transcription. The goal of this project is to convert audio files into readable text with appropriate formatting, including labeling questions and answers, and differentiating between the court and other speakers.

## Features

- Transcribe audio files using OpenAI Whisper API.
- Format transcriptions with readable sentence splits.
- Label **questions** with `Q` and **answers** with `A`.
- Label other speech with `THE COURT`.

## Requirements

To run this project, make sure you have the following Python libraries installed:

```bash
openai
gradio
dotenv
pydub
sounddevice
scipy
transformers
datasets
torch
python-docx
