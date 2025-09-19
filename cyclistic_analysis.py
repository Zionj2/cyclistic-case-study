import pandas as pd
import matplotlib.pyplot as plt 


df = pd.read_csv("C:/Users/zionz/OneDrive/Cyclistic Case Study/cyclistic_analysis.csv")

print("Ride counts by usertype:")
print(df['usertype'].value_counts())


df['usertype'].value_counts().plot(kind='bar', color=['blue', 'yellow'])
plt.title("Numbers of Rides: Subscribers vs Customers")
plt.xlabel("User Typre")
plt.ylabel("Count")
plt.show()


print("\nAverage trip duration (minutes) by usertype:")
print(df.groupby('usertype')['tripduration'].mean() / 60) # Convert seconds to minutes

df['start_time'] = pd.to_datetime(df['start_time'])
df['day_of_week'] = df['start_time'].dt.day_name()
rides_by_day = df.groupby(['usertype', 'day_of_week']).size().unstack()

rides_by_day = rides_by_day.plot(kind='bar')
plt.tile("Rides by Day of week (Subscribes vs Customers)")
plt.xlabel("user Type")
plt.ylabel("Number of Rides")
plt.show()

df['hour_of_day'] = df['start_time'].dt.hour
rides_by_hour = df.grouphy(['usertype', 'hour']).size().unstack()

rides_by_hour.T.plot(kind='line')
plt.title("Rides by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("Number od Rides")
plt.show()


          

           