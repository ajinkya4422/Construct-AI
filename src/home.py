import streamlit as st

def home_page():
    st.title("ConstructAI: Home Page")

    # Notifications Tab
    st.write("### Notifications")
    if "notifications" not in st.session_state:
        st.session_state.notifications = [
            "New safety guidelines have been issued. Please review them.",
            "The project deadline has been extended by 2 weeks.",
            "Upcoming maintenance on equipment scheduled for next Monday."
        ]

    # Display notifications
    for i, notice in enumerate(st.session_state.notifications):
        st.write(f"{i + 1}. {notice}")

    # Add new notification (admin-only)
    st.write("### Add New Notification (Admin Only)")
    new_notice = st.text_input("Enter a new notification:")
    if st.button("Post Notification"):
        if new_notice:
            st.session_state.notifications.append(new_notice)
            st.success("Notification posted successfully!")
        else:
            st.warning("Please enter a notification.")

    # Quick Links
    st.write("### Quick Links")
    if st.button("Go to Project Insights"):
        st.session_state.page = "Project Insights"
    if st.button("Go to Document Management"):
        st.session_state.page = "Document Management"
    if st.button("Go to Smart Scheduling"):
        st.session_state.page = "Smart Scheduling"

    # Text Content
    st.write("### About ConstructAI")
    st.write("""
    ConstructAI is an advanced project management platform designed to optimize large-scale engineering and construction projects. 
    It provides real-time insights into risk analysis, supply chain resilience, workforce optimization, budget tracking, and energy consumption monitoring.
    """)