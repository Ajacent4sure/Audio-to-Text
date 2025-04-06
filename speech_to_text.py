import gradio as gr
import openai
import re

def transcribe_audio(audio, api_key):
    """
    Transcribe the provided audio file to text using the OpenAI API's Whisper model.
    
    Parameters:
    - audio (str): The path to the audio file to transcribe.
    - api_key (str): The API key for authenticating with OpenAI.

    Returns:
    - str: The transcribed text, formatted for readability.
    """

    # Check if API key is provided
    if not api_key:
        return "❌ Error: Please enter your OpenAI API key."

    # Check if a valid audio file was uploaded
    if not audio:
        return "❌ Error: Please upload a valid audio file."

    try:
        # Set OpenAI API key
        openai.api_key = api_key

        with open(audio, "rb") as audio_file:
            # Corrected: Use openai.Audio.transcribe instead of openai.Audio.transcriptions.create
            transcription = openai.Audio.transcribe(
                model="whisper-1",
                file=audio_file
            )

        transcript_text = transcription["text"]

        # Format the output: Split into readable sentences
        formatted_transcript = re.sub(r'([.!?])\s+', r'\1\n', transcript_text)

        # Refined speaker labeling with "Q" and "A"
        sentences = formatted_transcript.split("\n")
        labeled_transcript = []

        # Add Q for questions and A for answers
        for i, sentence in enumerate(sentences):
            sentence = sentence.strip()
            if "?" in sentence:  # For questions
                labeled_transcript.append(f"Q\t {sentence}")
            elif i > 0 and "?" not in sentences[i-1]:  # For answers
                labeled_transcript.append(f"A\t {sentence}")
            else:  # Default to "THE COURT" for other sentences
                labeled_transcript.append(f"THE COURT: {sentence}")

        return "\n".join(labeled_transcript)

    except Exception as e:
        return f"⚠️ Error: {str(e)}"

def gradio_interface():
    """
    Create and launch a Gradio interface for the speech-to-text application.
    """

    with gr.Blocks() as demo:
        gr.Markdown("# <center>🎤 OpenAI Speech-to-Text with Formatting</center>")

        with gr.Row():
            api_key_input = gr.Textbox(
                label="🔑 OpenAI API Key", type="password", 
                placeholder="Enter your OpenAI API key"
            )

        audio_input = gr.Audio(sources="upload", type="filepath", label="🎵 Upload Audio File")

        transcribe_button = gr.Button("🎧 Transcribe")

        transcription_output = gr.Textbox(label="📝 Transcription", lines=15)

        transcribe_button.click(
            fn=transcribe_audio,
            inputs=[audio_input, api_key_input],
            outputs=transcription_output
        )

    demo.launch(share=True)

if __name__ == "__main__":
    gradio_interface()
