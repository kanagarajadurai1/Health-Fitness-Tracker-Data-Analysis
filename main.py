import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("health_fitness_tracker_data_analysis.csv")  # Replace with actual path

# Basic overview
print(df.columns)
print(df.describe())

# Steps vs Sleep Duration
sns.scatterplot(data=df, x='TotalSteps', y='TotalMinutesAsleep')
plt.title('Steps vs Sleep Duration')
plt.xlabel('Steps')
plt.ylabel('Sleep (Minutes)')
plt.show()

# Weekly Step Pattern
df['ActivityDate'] = pd.to_datetime(df['ActivityDate'])
df['Day'] = df['ActivityDate'].dt.day_name()
sns.boxplot(x='Day', y='TotalSteps', data=df)
plt.title('Steps per Day of the Week')
plt.show()

# Average Calories Burnt
df['Calories'].plot(kind='line', figsize=(10, 4), title='Calories Burnt Over Time')
plt.xlabel("Index")
plt.ylabel("Calories")
plt.show()
