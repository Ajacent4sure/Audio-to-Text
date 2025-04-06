# 🗣️ OpenAI Whisper Speech-to-Text Formatter 🎧

This project provides a simple and elegant interface for transcribing audio files into readable text using OpenAI's Whisper model. Built with Python and Gradio, it offers a streamlined workflow where users can upload audio files, input their API key, and instantly receive structured, speaker-labeled transcripts — especially tailored for courtroom or dialogue-heavy settings.

---

## 🚀 Features

- 🎙️ **Audio Upload**: Upload your own audio recordings.
- 🤖 **OpenAI Whisper Integration**: Utilizes OpenAI’s `whisper-1` model for high-quality transcription.
- 🧠 **Custom Speaker Labeling**:
  - Sentences with a question (`?`) are labeled as:
    ```
    Q	 What is your name?
    A	 John Doe.
    ```
  - Default fallback labeling as `THE COURT:` if no Q/A logic applies.
- 🛡️ **Secure API Handling**: Enter your OpenAI API key securely through a masked input.
- 🌐 **Gradio Web UI**: User-friendly interface to interact with the transcription engine directly in your browser.

---

## 📁 Project Structure

```
├── .gitignore           # Ignores 'venv/' and 'Others/' folders
├── requirements.txt     # All Python dependencies
├── speech_to_text.py    # Main Python script containing logic & interface
├── venv/                # (Ignored) Your Python virtual environment
├── Others/              # (Ignored) Any additional unused resources
```

---

## 🧪 Dependencies

Install all required dependencies using:

```bash
pip install -r requirements.txt
```

---

## 🔑 Setup & Usage

1. **Clone the repository:**

```bash
git clone https://github.com/Ajacent4sure/Audio-to-Text
```

2. **Create a `.env` file** *(optional but recommended)* to store your OpenAI key:

```
OPENAI_API_KEY=your-api-key-here
```

3. **Run the app:**

```bash
python speech_to_text.py
```

4. **In the Gradio interface:**
   - Upload an audio file.
   - Enter your OpenAI API key.
   - Click "Transcribe" to get your Q/A-labeled transcript.

---

## 🧠 Example Output

```
Q	 What time did you arrive at the scene?
A	 I arrived around 10:30 AM.
THE COURT: Thank you, Counsel.
Q	 Were there any witnesses present?
A	 Yes, a bystander was present.
```

---

## 🛠️ Tech Stack

- Python 🐍
- OpenAI Whisper API 🧠
- Gradio 🎨

---

## ✅ To-Do

- [ ] Add audio playback with transcript syncing
- [ ] Export transcript to `.docx` or `.pdf`
- [ ] Add support for batch audio processing

---


---

## 🙌 Acknowledgments

Built with ❤️ for voice transcription enthusiasts and legal tech developers, powered by OpenAI's Whisper model and Gradio.
