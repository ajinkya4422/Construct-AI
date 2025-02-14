import pandas as pd
import numpy as np

def get_energy_data():
    # Generate random energy data
    data = {
        'Equipment': ['Crane', 'Excavator', 'Generator', 'Drill'],
        'Usage (hours)': np.random.randint(1, 24, size=4),
        'Energy (kWh)': np.random.randint(50, 500, size=4)
    }
    return pd.DataFrame(data)