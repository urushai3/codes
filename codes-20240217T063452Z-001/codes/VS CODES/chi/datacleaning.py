import pandas as pd
import re
from fuzzywuzzy import fuzz

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('Cancer type_data cleanup  - Lung cancer.csv')

# Function to remove titles and degrees
def remove_titles(name):
    # Convert to string if the input is not already a string
    name_str = str(name)

    # Apply the regular expression to remove titles
    return re.sub(r'\b(?:MD|Ph\.?D|Prof\.?|M\.?D\.?|BSc)\b', '', name_str, flags=re.IGNORECASE)
 
# Function to standardize capitalization
def standardize_capitalization(name):
    return name.title()

# Apply the cleaning functions to the 'Name' column
df['Cleaned_Name'] = df['PIs'].apply(remove_titles)
df['Cleaned_Name'] = df['Cleaned_Name'].apply(standardize_capitalization)

# Function to merge similar names using fuzzy matching
def merge_similar_names(names):
    merged_names = []

    for name in names:
        found = False
        for merged_name in merged_names:
            if fuzz.ratio(name, merged_name) > 80:
                found = True
                break

        if not found:
            merged_names.append(name)

    return merged_names

# Apply the function to the 'Cleaned_Name' column
df['Final_Name'] = merge_similar_names(df['Cleaned_Name'])

# Save the cleaned data to a new CSV file
df.to_csv('cleaned_data.csv', index=False)
