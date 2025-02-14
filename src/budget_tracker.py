import pandas as pd
import numpy as np

def get_budget_data():
    # Generate random budget data
    data = {
        'Category': ['Materials', 'Labor', 'Equipment', 'Misc'],
        'Planned (USD)': np.random.randint(1000, 5000, size=4),
        'Actual (USD)': np.random.randint(800, 4500, size=4)
    }
    return pd.DataFrame(data)