import pandas as pd
import numpy as np

def get_risk_data():
    # Generate random risk data
    data = {
        'Task': ['Site Prep', 'Foundation', 'Structural', 'Finishing'],
        'Risk Level': np.random.choice(['Low', 'Medium', 'High'], size=4),
        'Completion (%)': np.random.randint(0, 100, size=4)
    }
    return pd.DataFrame(data)