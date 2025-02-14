import streamlit as st
import pandas as pd
import plotly.express as px
from src.risk_analysis import get_risk_data
from src.supply_chain import get_supply_chain_data
from src.labor_scheduler import get_workforce_data
from src.budget_tracker import get_budget_data
from src.energy_monitor import get_energy_data

def project_insights_page():
    st.title("ConstructAI: Project Insights")

    # Risk Analysis
    st.write("### Risk Analysis")
    risk_data = get_risk_data()
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Description:**")
        st.write("""
        Risk analysis helps identify potential delays and hazards in the project. 
        The graph shows the completion percentage and risk level for each task.
        """)
    with col2:
        fig_risk = px.bar(risk_data, x='Task', y='Completion (%)', color='Risk Level', title="Risk Analysis")
        st.plotly_chart(fig_risk, use_container_width=True)

    # Supply Chain Resilience
    st.write("### Supply Chain Resilience")
    supply_chain_data = get_supply_chain_data()
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Description:**")
        st.write("""
        Supply chain resilience ensures timely delivery of materials. 
        The graph shows the cost and delivery time for each material.
        """)
    with col2:
        fig_supply = px.line(supply_chain_data, x='Material', y='Cost (USD)', title="Supply Chain Cost")
        st.plotly_chart(fig_supply, use_container_width=True)

    # Workforce Optimization
    st.write("### Workforce Optimization")
    workforce_data = get_workforce_data()
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Description:**")
        st.write("""
        Workforce optimization ensures efficient allocation of labor. 
        The pie chart shows the distribution of workers by skill.
        """)
    with col2:
        fig_workforce = px.pie(workforce_data, names='Skill', values='Workers Available', title="Workforce Distribution")
        st.plotly_chart(fig_workforce, use_container_width=True)

    # Budget Tracking
    st.write("### Budget Tracking")
    budget_data = get_budget_data()
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Description:**")
        st.write("""
        Budget tracking helps monitor project expenses. 
        The bar chart compares planned vs. actual costs.
        """)
    with col2:
        fig_budget = px.bar(budget_data, x='Category', y=['Planned (USD)', 'Actual (USD)'], barmode='group', title="Budget Tracking")
        st.plotly_chart(fig_budget, use_container_width=True)

    # Energy Consumption Monitoring
    st.write("### Energy Consumption Monitoring")
    energy_data = get_energy_data()
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Description:**")
        st.write("""
        Energy consumption monitoring helps reduce costs. 
        The scatter plot shows energy usage by equipment.
        """)
    with col2:
        fig_energy = px.scatter(energy_data, x='Usage (hours)', y='Energy (kWh)', color='Equipment', title="Energy Usage")
        st.plotly_chart(fig_energy, use_container_width=True)

    # Navigation
    if st.button("Go to Home"):
        st.session_state.page = "Home"
    if st.button("Go to Document Management"):
        st.session_state.page = "Document Management"