import numpy as np
import io
import soundfile as sf
import whisper
import tempfile

# Load the model
model = whisper.load_model("base")

def convert_audio_to_np_array(uploaded_audio):
    """
    Convert the uploaded audio file to a NumPy array.
    """
    audio_bytes = uploaded_audio.read()
    audio_np_array, _ = sf.read(io.BytesIO(audio_bytes))
    
    # Ensure the dtype is float32
    if audio_np_array.dtype != np.float32:
        audio_np_array = audio_np_array.astype(np.float32)
    
    return audio_np_array

def save_np_array_to_tempfile(audio_np_array):
    """
    Save the NumPy array to a temporary WAV file.
    """
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
        sf.write(temp_file.name, audio_np_array, 16000)  # Assuming 16000 Hz sample rate
        return temp_file.name

def transcribe_audio(audio_path: str) -> str:
    """
    Transcribe the audio file at the given path to text.
    """
    result = model.transcribe(audio_path)
    return result["text"]

