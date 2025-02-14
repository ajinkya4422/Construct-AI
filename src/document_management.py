import streamlit as st
import os

def document_management_page():
    st.title("ConstructAI: Document Management")

    # Upload Document
    st.write("### Upload Document")
    uploaded_file = st.file_uploader("Choose a file", type=["pdf", "docx", "xlsx"])
    if uploaded_file is not None:
        file_path = os.path.join("documents", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"File '{uploaded_file.name}' uploaded successfully!")

    # View Documents
    st.write("### View Documents")
    if os.path.exists("documents"):
        documents = os.listdir("documents")
        for doc in documents:
            st.write(f"- {doc}")
            with open(os.path.join("documents", doc), "rb") as f:
                st.download_button(f"Download {doc}", f, file_name=doc)
    else:
        st.write("No documents available.")

    # Navigation
    if st.button("Go to Home"):
        st.session_state.page = "Home"
    if st.button("Go to Project Insights"):
        st.session_state.page = "Project Insights"