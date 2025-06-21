import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('covid_data.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Filter by country
india = df[df['Country'] == 'India']
usa = df[df['Country'] == 'USA']
italy = df[df['Country'] == 'Italy']

# Plot: Confirmed Cases Trend
plt.figure(figsize=(10,6))
plt.plot(india['Date'], india['Confirmed'], label='India', marker='o')
plt.plot(usa['Date'], usa['Confirmed'], label='USA', marker='o')
plt.plot(italy['Date'], italy['Confirmed'], label='Italy', marker='o')
plt.title('COVID-19 Confirmed Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Confirmed Cases')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('trend_plot.png')
plt.show()

# Pivot and Heatmap of Deaths
pivot = df.pivot_table(values='Deaths', index='Country', columns='Date')
plt.figure(figsize=(8,5))
sns.heatmap(pivot, cmap='Reds', annot=True, fmt=".0f")
plt.title('COVID-19 Deaths Heatmap')
plt.tight_layout()
plt.savefig('heatmap.png')
plt.show()
