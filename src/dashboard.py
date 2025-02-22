# src/dashboard.py
import streamlit as st
from home import home_page
from project_insights import project_insights_page
from document_management import document_management_page
from smart_scheduling import smart_scheduling_page
from chatbot import initialize_chatbot
from predictive_maintenance import train_predictive_model
from resource_optimization import optimize_resources
import plotly.express as px
import pandas as pd
import numpy as np
import joblib

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
        if response:
            st.sidebar.write(f"**Bot:** {response}")
        else:
            st.sidebar.write("**Bot:** I'm sorry, I didn't understand that.")

    # Navigation
    if st.session_state.page == "Home":
        home_page()
    elif st.session_state.page == "Project Insights":
        project_insights_page()
    elif st.session_state.page == "Document Management":
        document_management_page()
    elif st.session_state.page == "Smart Scheduling":
        smart_scheduling_page()
    elif st.session_state.page == "Equipment Health":
        equipment_health_page()
    elif st.session_state.page == "Resource Allocation":
        resource_allocation_page()

# New Pages
def equipment_health_page():
    st.title("Predictive Maintenance Dashboard")
    
    # Load model
    model = joblib.load('models/predictive_maintenance.pkl')
    
    # Simulate real-time sensor data
    sensor_data = pd.DataFrame({
        'vibration': [np.random.uniform(0, 1)],
        'temperature': [np.random.randint(40, 90)],
        'usage_hours': [np.random.randint(200, 400)]
    })
    
    # Predict failure probability
    prediction = model.predict_proba(sensor_data)[:, 1][0]
    st.write(f"### Failure Probability: {prediction:.2f}")
    
    # Display recommendations
    if prediction > 0.5:
        st.error("**Alert:** High risk of equipment failure. Schedule maintenance!")
    else:
        st.success("**Status:** Equipment is healthy.")

def resource_allocation_page():
    st.title("Resource Allocation Optimization")
    
    # Run optimization
    results = optimize_resources()
    st.write("### Optimal Resource Allocation")
    st.write(results)
    
    # Visualize
    fig = px.bar(results, x='Project', y='Selected', title="Selected Projects")
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()