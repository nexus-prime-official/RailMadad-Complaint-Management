import streamlit as st

# Define a function to display the sidebar and handle page selection
def display_sidebar():
    st.sidebar.title("Navigation")
    pages = {
        "Complaint Recognition": "complaint_recognition",
        "Complaint Classification": "complaint_classification",
        "Preliminary Response": "preliminary_response",
        # Add more pages here as needed
    }
    selection = st.sidebar.radio("Select a page", list(pages.keys()))
    return pages[selection]

# Load the selected page
def load_page(page_name):
    # Dynamic import of the page module
    page = __import__(f'pages.{page_name}', fromlist=[''])
    page.app()

def main():
    st.title("Rail Madad Complaint Management")
    page_name = display_sidebar()
    load_page(page_name)

if __name__ == "__main__":
    main()

#"smart routing": "smart_routing",
#"severity analysis": "severity_analysis",

