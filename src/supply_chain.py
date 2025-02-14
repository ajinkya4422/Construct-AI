import pandas as pd
import numpy as np

def get_supply_chain_data():
    # Generate random supply chain data
    data = {
        'Material': ['Steel', 'Cement', 'Wood', 'Glass'],
        'Delivery Time (days)': np.random.randint(1, 30, size=4),
        'Cost (USD)': np.random.randint(100, 1000, size=4)
    }
    return pd.DataFrame(data)