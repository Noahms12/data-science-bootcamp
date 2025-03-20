import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys

# QUESTION 1
url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"
df = pd.read_csv(url)

# Convert 'hour_beginning' to datetime
df['hour_beginning'] = pd.to_datetime(df['hour_beginning'])

# Extract days of the week and select only monday-friday
df['Weekday'] = df['hour_beginning'].dt.weekday
weekday_df = df[df['Weekday'] < 5]

# Group by weekday and sum pedestrian counts
weekday_counts = weekday_df.groupby('Weekday')['Pedestrians'].sum()

# Plot
plt.figure(figsize=(10, 5))
plt.plot(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'], weekday_counts, marker='o')
plt.xlabel('Day of the Week')
plt.ylabel('Total Pedestrian Count')
plt.title('Pedestrian Counts Per Weekday')
plt.grid()
plt.show()

#QUESTION 2


# Filter data for 2019
df_2019 = df[df['hour_beginning'].dt.year == 2019]

# Select desired columns
df_2019_weather = df_2019[['Pedestrians', 'weather_summary']]

# Use one-hot encoding on 'weather_summary'
df_2019_weather_encoded = pd.get_dummies(df_2019_weather, columns=['weather_summary'])

# Calculate correlation matrix
corr_matrix = df_2019_weather_encoded.corr()

# Plot correlation heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Between Weather and Pedestrian Counts (2019)')
plt.show()


#QUESTION 3
# Function to categorize time of day
def categorize_time_of_day(hour):
    if 6 <= hour < 12:
        return "Morning"
    elif 12 <= hour < 18:
        return "Afternoon"
    elif 18 <= hour < 22:
        return "Evening"
    else:
        return "Night"

# Extract hour run it through categorize_time_of_day
df['time_of_day'] = df['hour_beginning'].dt.hour.apply(categorize_time_of_day)

# Group by time of day and sum pedestrian counts
time_of_day_analysis = df.groupby("time_of_day")["Pedestrians"].sum().reset_index()


# Plot pedestrian activity by time of day
plt.figure(figsize=(8, 5))
sns.barplot(x="time_of_day", y="Pedestrians", data=time_of_day_analysis)
plt.title("Pedestrian Activity by Time of Day")
plt.xlabel("Time of Day")
plt.ylabel("Total Pedestrians")
plt.show()