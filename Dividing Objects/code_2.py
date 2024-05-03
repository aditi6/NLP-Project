import pandas as pd
import itertools

# Load the scenario data
scenarios_df = pd.read_csv('.\scenarios.csv')

# Load the character data
characters_df = pd.read_csv('.\characters.csv')

# Initialize a list to store all the new rows before creating the DataFrame
all_combinations = []

# Generate all combinations of two different characters
character_pairs = list(itertools.permutations(characters_df.index, 2))

# Iterate over each scenario and each pair of characters
for index, scenario in scenarios_df.iterrows():
    for pair in character_pairs:
        char1 = characters_df.iloc[pair[0]]
        char2 = characters_df.iloc[pair[1]]
        # Prepare the data as a dictionary and append to the list
        all_combinations.append({
            'scenario': scenario['Scenario'],
            'character1': char1['Description'],
            'goal1': scenario['Character1'],
            'character2': char2['Description'],
            'goal2': scenario['Character2'],
            'points1': scenario['Points1'],
            'points2': scenario['Points2'],
            'gender1': char1['Gender'],
            'race1': char1['Race'],
            'gender2': char2['Gender'],
            'race2': char2['Race'],
        })

# Convert the list of dictionaries to a DataFrame
combinations_df = pd.DataFrame(all_combinations)

# Save the DataFrame to a new CSV file
combinations_df.to_csv('combinations.csv', index=False)
