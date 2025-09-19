import pandas as pd

df = pd.read_csv("C:/Users/zionz/OneDrive/Cyclistic Case Study/Raw Data/Divvy_Trips_2019_Q1.csv.csv")
print(df.head())

print(df.isnull().sum())

df["start_time"] = pd.to_datetime(df["start_time"])
df["end_time"] = pd.to_datetime(df["end_time"])
df["birthyear"] = df["birthyear"].fillna(0).astype(int)

print(df.describe())
print(df["gender"].value_counts())

df = df[df["birthyear"] > 1900] # Remove unrealistic birth years

import pandas as pd

df["gender"] = df["gender"].fillna("Unknown")

df["birthyear"] = df["birthyear"].apply(lambda x: x if 1990 <= x <= 2010 else None)
df["birthyear"] = df["birthyear"].astype('Int64')

df["start_time"] = pd.to_datetime(df["start_time"])
df["end_time"] = pd.to_datetime(df["end_time"])

print(df.isnull().sum())
print(df['gender'].value_counts())
print(df['birthyear'].describe())

import datetime as dt 

current_year = 2019 # Assuming the data is from 2019
df['age'] = current_year - df['birthyear']

print(df[['birthyear', 'age']].head())
print(df['age'].describe())

df.to_csv("C:/Users/zionz/OneDrive/Cyclistic Case Study/Cleaned_data.csv", index=False)
print("Cleaned data saved as cleaned_data.csv")