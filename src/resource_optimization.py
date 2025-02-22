# src/resource_optimization.py
import pandas as pd
import pulp

def optimize_resources():
    # Load data
    data = pd.read_csv('data/resource_allocation_data.csv')
    
    # Define problem
    prob = pulp.LpProblem("Resource_Allocation", pulp.LpMaximize)
    
    # Variables
    projects = list(data['project'])
    x = pulp.LpVariable.dicts("Project", projects, 0, 1, cat='Binary')  # 1 if project is selected
    
    # Objective: Maximize priority-weighted projects
    prob += pulp.lpSum([data.loc[i, 'priority'] * x[proj] for i, proj in enumerate(projects)])
    
    # Constraints
    total_workers = 70  # Total available workers
    total_machines = 15 # Total available machines
    prob += pulp.lpSum([data.loc[i, 'workers_needed'] * x[proj] for i, proj in enumerate(projects)]) <= total_workers
    prob += pulp.lpSum([data.loc[i, 'machines_needed'] * x[proj] for i, proj in enumerate(projects)]) <= total_machines
    
    # Solve
    prob.solve()
    
    # Extract results
    results = []
    for proj in projects:
        results.append({
            'Project': proj,
            'Selected': x[proj].value() == 1
        })
    
    return pd.DataFrame(results)