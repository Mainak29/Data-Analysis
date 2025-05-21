import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
df = pd.read_csv('customer_feedback.csv')

# Display basic info
print("First 5 records:")
print(df.head())
print("\nFeedback Value Counts:")
print(df['feedback'].value_counts())

# Set up the visual style
sns.set(style="whitegrid")

# Plot the feedback distribution
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='feedback', palette='viridis')
plt.title('Customer Feedback Distribution')
plt.xlabel('Feedback Type')
plt.ylabel('Count')
plt.tight_layout()

# Save and show the plot
plt.savefig('feedback_distribution.png')
plt.show()
