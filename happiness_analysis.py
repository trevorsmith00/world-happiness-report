# This script analyzes the World Happiness Report data and creates visualizations
# for the top 10 happiest countries in 2021, global life ladder score over time,
# and the relationship between GDP per capita and life ladder score.
# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
df_2021 = pd.read_csv("world-happiness-report-2021.csv")
df_all_years = pd.read_csv("world-happiness-report.csv")

# Clean and prepare data
df_clean = df_all_years[['Country name', 'year', 'Life Ladder', 'Log GDP per capita', 
                         'Social support', 'Healthy life expectancy at birth']].dropna()

# Visualization 1: Top 10 Happiest Countries in 2021
top10_2021 = df_2021[['Country name', 'Ladder score']].sort_values(by='Ladder score', ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(data=top10_2021, x='Ladder score', y='Country name', hue='Country name', palette='viridis', dodge=False)
plt.title('Top 10 Happiest Countries (2021)')
plt.xlabel('Happiness Score')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig('top10_happiest_2021.png')
plt.show()

# Visualization 2: Global Life Ladder Score Over Time
global_avg = df_clean.groupby('year')['Life Ladder'].mean().reset_index()
plt.figure(figsize=(10, 6))
sns.lineplot(data=global_avg, x='year', y='Life Ladder', marker='o')
plt.title('Global Average Life Ladder Score Over Time')
plt.xlabel('Year')
plt.ylabel('Average Happiness Score')
plt.grid(True)
plt.tight_layout()
plt.savefig('global_life_ladder_trend.png')
plt.show()

# Visualization 3: GDP vs Life Ladder Score with Regression Line
plt.figure(figsize=(10, 6))
sns.regplot(data=df_clean, x='Log GDP per capita', y='Life Ladder', scatter_kws={'alpha':0.5})
plt.title('GDP per Capita vs. Life Ladder Score')
plt.xlabel('Log GDP per Capita')
plt.ylabel('Life Ladder Score')
plt.tight_layout()
plt.savefig('gdp_vs_life_ladder.png')
plt.show()
