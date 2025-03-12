import pandas as pd
import json

def json_to_dataframe(json_input):
    # Parse the JSON input
    data = json.loads(json_input)
    
    # Convert to DataFrame
    df = pd.DataFrame(data)
    
    # Convert 'Datetime' column to pandas datetime type if it exists
    if 'Datetime' in df.columns:
        df['Datetime'] = df['Datetime'].astype(str)  # Ensure it's read as string first
        df['Datetime'] = pd.to_datetime(df['Datetime'], format='%Y-%m-%dT%H:%M:%S.%f')
    
    return df

# Example JSON input
json_input = '[{"id": 1, "name": "Alice", "created": "2024-02-18T10:00:00.00000"}]'

df = json_to_dataframe(json_input)
print(df)

# Write DataFrame to CSV
df.to_csv("output.csv", index=False)
