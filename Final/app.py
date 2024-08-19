import streamlit as st
from PIL import Image
from io import BytesIO
from Audio import convert_audio_to_np_array, save_np_array_to_tempfile, transcribe_audio
from Image import convert_to_base64
from classifier import classify_input
from EmailSender import send_email
from sms import send_sms

def input():
    st.title("Grievance Details")
    
    # Mobile Number
    number = st.text_input("Mobile Number")
    # Complaint Text
    complaint = st.text_area("Grievance Description")
    
    col1, col2 = st.columns([1, 1])
        
    # Flags to track which file has been uploaded
    image_uploaded = False
    audio_uploaded = False
        
    # Image upload
    with col1:
        uploaded_image = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg", "bmp", "gif", "tiff"], key="image_uploader")
        if uploaded_image is not None:
            image_uploaded = True
            st.image(Image.open(uploaded_image), caption='Preview of the uploaded image.')
            st.write("Image successfully uploaded and previewed!")
        
    # Audio upload
    with col2:
        uploaded_audio = st.file_uploader("Choose an audio...", type=["mp3", "wav", "ogg", "flac", "aac"], key="audio_uploader")
        if uploaded_audio is not None:
            audio_uploaded = True
            st.audio(uploaded_audio, format=uploaded_audio.type)
            st.write("Audio successfully uploaded and previewed!")

    # Store data for further processing
    if st.button("Submit"):
        if not number or not complaint:
            st.warning("Please provide all the required fields.")
            return

        data = {
            "mobile_number": number,
            "complaint": complaint,
            "image_uploaded": image_uploaded,
            "audio_uploaded": audio_uploaded
        }
        
        # Display stored data for debugging purposes
        st.write("Stored Data:", data)
        
        # Further processing
        if image_uploaded:
            # Convert the image to base64
            image_path = convert_to_base64(uploaded_image)
            
        if audio_uploaded:
            # Convert the audio to a NumPy array
            audio_np_array = convert_audio_to_np_array(uploaded_audio)
            # Save the NumPy array to a temporary file
            temp_audio_path = save_np_array_to_tempfile(audio_np_array)
            # Process the audio using the transcribe_audio function
            audio_transcription = transcribe_audio(temp_audio_path)
            st.write("Audio Transcription:", audio_transcription)
        
        # Apply classify_input to the complaint text
        if complaint:
            st.write("Complaints Text:", complaint)  # Debugging step
            classification_result = classify_input(complaint)
            st.write("Complaint Classification Result:", classification_result)
        else:
            st.write("No complaint text provided.")
        
        if image_uploaded and audio_uploaded:
            st.write("Both Image and Audio have been successfully processed!")

def main():
    st.title("Rail Madad Complaint Management")
    input()

if __name__ == "__main__":
    main()
