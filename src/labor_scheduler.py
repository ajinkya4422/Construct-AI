import pandas as pd
import numpy as np

def get_workforce_data():
    # Generate random workforce data
    data = {
        'Skill': ['Carpenter', 'Electrician', 'Plumber', 'Mason'],
        'Workers Available': np.random.randint(1, 20, size=4),
        'Productivity (%)': np.random.randint(50, 100, size=4)
    }
    return pd.DataFrame(data)