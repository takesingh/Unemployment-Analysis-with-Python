# Unemployment Analysis
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data (download from Kaggle first)
df = pd.read_csv("Unemployment in India.csv")  # Change file name as per your local file

# Preview
print(df.head())
print(df.columns)

# Clean Data
df.columns = ['States', 'Date', 'Frequency', 'Estimated Unemployment Rate (%)',
              'Estimated Employed', 'Estimated Labour Participation Rate (%)', 'Region']

# Convert Date
df["Date"] = pd.to_datetime(df["Date"])

# Visualization
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x="Date", y="Estimated Unemployment Rate (%)", hue="Region")
plt.title("Unemployment Rate Over Time by Region")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
