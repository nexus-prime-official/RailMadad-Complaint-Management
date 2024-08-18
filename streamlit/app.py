import streamlit as st
from PIL import Image


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
            uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg", "bmp", "gif", "tiff"], key="image_uploader", disabled=False)
            if uploaded_file is not None:
                image_uploaded = True
                st.image(Image.open(uploaded_file), caption='Preview of the uploaded image.')
                st.write("Image successfully uploaded and previewed!")
            
        # Description Function for Image
        
        # Audio upload
    with col2:
            uploaded_audio = st.file_uploader("Choose an audio...", type=["mp3", "wav", "ogg", "flac", "aac"], key="audio_uploader", disabled=image_uploaded)
            if uploaded_audio is not None:
                audio_uploaded = True
                st.audio(uploaded_audio, format=uploaded_audio.type)
                st.write("Audio successfully uploaded and previewed!")

        # Transcript for Audio

    if st.button("Submit"):
            st.write("Mobile Number:", number)
            st.write("Complaint:", complaint)

def main():
    st.title("Rail Madad Complaint Management")
    # page_name = display_sidebar()
    # load_page(page_name)
    input()

if __name__ == "__main__":
    main()

#"smart routing": "smart_routing",
#"severity analysis": "severity_analysis",

