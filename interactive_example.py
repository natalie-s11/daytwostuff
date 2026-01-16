# %% Cell 1: Import libraries
import numpy as np
import pandas as pd

print("Libraries imported successfully")

# %% Cell 2: Create sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Score': [85, 90, 88]
}

df = pd.DataFrame(data)
print("Sample DataFrame created:")
print(df)

# %% Cell 3: Perform analysis
average_score = df['Score'].mean()
print(f"Average score: {average_score}")

# %% Cell 4: Visualize data
import matplotlib.pyplot as plt

plt.bar(df['Name'], df['Score'])
plt.title('Scores by Name')
plt.xlabel('Name')
plt.ylabel('Score')
plt.show()