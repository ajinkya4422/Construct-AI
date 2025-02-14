import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def smart_scheduling_page():
    st.title("Smart Project Scheduling & Timeline Optimization")

    # Text Data: Introduction
    st.write("""
    ### What is Smart Scheduling?
    Smart Scheduling uses AI and optimization algorithms to:
    - **Suggest the best sequence of tasks** to avoid delays.
    - **Automatically adjust deadlines** if delays occur.
    - **Provide recovery plans** to get back on track.
    - **Manage multiple construction projects** efficiently.
    """)

    # Sample Data for Tasks
    tasks = [
        {"Task": "Site Preparation", "Duration (days)": 10, "Start Date": "2023-10-01", "Dependencies": []},
        {"Task": "Foundation Work", "Duration (days)": 15, "Start Date": "2023-10-11", "Dependencies": ["Site Preparation"]},
        {"Task": "Structural Work", "Duration (days)": 20, "Start Date": "2023-10-26", "Dependencies": ["Foundation Work"]},
        {"Task": "Finishing", "Duration (days)": 10, "Start Date": "2023-11-15", "Dependencies": ["Structural Work"]},
    ]
    df_tasks = pd.DataFrame(tasks)

    # Display Tasks
    st.write("### Project Tasks")
    st.write(df_tasks)

    # Gantt Chart for Task Timeline
    st.write("### Project Timeline (Gantt Chart)")
    df_gantt = df_tasks.copy()
    df_gantt["End Date"] = pd.to_datetime(df_gantt["Start Date"]) + pd.to_timedelta(df_gantt["Duration (days)"], unit="d")
    fig_gantt = px.timeline(
        df_gantt,
        x_start="Start Date",
        x_end="End Date",
        y="Task",
        title="Project Timeline"
    )
    fig_gantt.update_yaxes(autorange="reversed")  # Reverse y-axis to show tasks in order
    st.plotly_chart(fig_gantt, use_container_width=True)

    # Bar Chart for Task Durations
    st.write("### Task Durations (Bar Chart)")
    fig_bar = px.bar(
        df_tasks,
        x="Task",
        y="Duration (days)",
        title="Task Durations",
        labels={"Duration (days)": "Duration (in days)"}
    )
    st.plotly_chart(fig_bar, use_container_width=True)

    # Suggest Best Sequence of Tasks
    st.write("### Suggested Task Sequence")
    suggested_sequence = ["Site Preparation", "Foundation Work", "Structural Work", "Finishing"]
    st.write(suggested_sequence)

    # Simulate Delay and Adjust Deadlines
    st.write("### Delay Simulation")
    delay_task = st.selectbox("Select a task to simulate a delay:", df_tasks["Task"])
    delay_days = st.number_input("Enter the delay (in days):", min_value=1, max_value=30, value=5)

    if st.button("Apply Delay"):
        # Adjust deadlines
        st.write(f"**Delay Applied:** {delay_task} is delayed by {delay_days} days.")
        st.write("### Adjusted Task Sequence")
        adjusted_sequence = suggested_sequence.copy()
        st.write(adjusted_sequence)

        # Suggest Recovery Plan
        st.write("### Recovery Plan")
        recovery_plan = [
            f"1. **Increase workforce for {delay_task}:** Assign additional workers to complete the task faster.",
            f"2. **Allocate additional resources to dependent tasks:** Ensure dependent tasks have enough resources to avoid further delays.",
            f"3. **Extend working hours for critical tasks:** Implement overtime to catch up on lost time."
        ]
        for plan in recovery_plan:
            st.write(plan)

    # Manage Multiple Projects
    st.write("### Manage Multiple Projects")
    projects = ["Project A", "Project B", "Project C"]
    selected_project = st.selectbox("Select a project to view its timeline:", projects)
    st.write(f"**Timeline for {selected_project}:**")
    st.write(suggested_sequence)  # Replace with actual timeline for the selected project

    # Navigation
    if st.button("Go to Home"):
        st.session_state.page = "Home"
    if st.button("Go to Project Insights"):
        st.session_state.page = "Project Insights"
    if st.button("Go to Document Management"):
        st.session_state.page = "Document Management"