import streamlit as st
from src.home import home_page
from src.project_insights import project_insights_page
from src.document_management import document_management_page
from src.smart_scheduling import smart_scheduling_page
from src.chatbot import initialize_chatbot

def main():
    # Initialize session state for page navigation
    if "page" not in st.session_state:
        st.session_state.page = "Home"

    # Chatbot in Sidebar
    st.sidebar.title("ConstructAI Chatbot")
    user_input = st.sidebar.text_input("Ask me anything about the project:")
    if user_input:
        chatbot = initialize_chatbot()
        response = chatbot.respond(user_input)
        if response:  # Ensure response is not None
            st.sidebar.write(f"**Bot:** {response}")
        else:
            st.sidebar.write("**Bot:** I'm sorry, I didn't understand that. Can you please rephrase your question?")

    # Page navigation
    if st.session_state.page == "Home":
        home_page()
    elif st.session_state.page == "Project Insights":
        project_insights_page()
    elif st.session_state.page == "Document Management":
        document_management_page()
    elif st.session_state.page == "Smart Scheduling":
        smart_scheduling_page()

if __name__ == "__main__":
    main()