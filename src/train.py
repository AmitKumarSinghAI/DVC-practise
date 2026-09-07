import pandas as pd
from pathlib import Path

# Create the dataframe
df = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan'],
    'age': [25, 30, 35, 28, 22],
    'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
})

# Create the "data" folder if it doesn't exist
Path("data").mkdir(exist_ok=True)

# Save to CSV inside the data folder
df.to_csv('data/sample_data.csv', index=False)