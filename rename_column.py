import pandas as pd

# Read the CSV file
df = pd.read_csv('gsm8k_tr_classified_merged.csv')

# Rename the column
df = df.rename(columns={'answer_method': 'solution_method'})

# Save the updated CSV file
df.to_csv('gsm8k_tr_classified_merged.csv', index=False)

print("Column 'answer_method' has been renamed to 'solution_method' successfully!")
print("Updated columns:", list(df.columns)) 