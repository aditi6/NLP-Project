import pandas as pd
import re

# Load the CSV file
df = pd.read_csv('combinations.csv')  # Replace 'path_to_your_file.csv' with the path to your CSV

# Function to extract the numerical value from the goal description
def extract_price(goal_text):
    # Using regex to find the numerical value following the dollar sign
    match = re.search(r'\$\s*(\d+)', goal_text)
    return int(match.group(1)) if match else None

# Extract price for goal1 and goal2
df['price1'] = df['goal1'].apply(extract_price)
df['price2'] = df['goal2'].apply(extract_price)

# Save the updated DataFrame back to CSV
df.to_csv('updated_combinations.csv', index=False)
