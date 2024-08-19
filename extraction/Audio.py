import whisper

model = whisper.load_model("base")


def transcribe_audio(audio_path: str) -> str:
    """
    Translate the audio file to text
    """
    result = model.transcribe(audio_path)
    return result["text"]


description = transcribe_audio("extraction/sample.mp3")
print(description)