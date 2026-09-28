# Airline Arrival Delay Analysis

# Project Overview:
# This project compares the arrival delays of two airlines, Alaska and AM West, across five major cities. The goal is to determine which airline has a higher percentage of delayed flights overall.

# Data Acquisition:
# The raw data was gotten from Project1.pdf chart that was provided and then formatted into a csv file in the repo

import pandas as pd

# Loading the csv data
df = pd.read_csv('AirlineInfo.csv')

# Calculate the total flights across all 5 cities for each row
df['Total_Flights'] = df['Los Angeles'] + df['Phoenix'] + df['San Diego'] + df['San Francisco'] + df['Seattle']

# Group the data by Airline and Status, and add the totals
summary = df.groupby(['Airline', 'Status'])['Total_Flights'].sum().reset_index()

print("--- Total Flights by Status ---")
print(summary)
print("\n")

# Calculate the delay % for ALASKA
alaska_delayed = summary[(summary['Airline'] == 'ALASKA') & (summary['Status'] == 'delayed')]['Total_Flights'].sum()
alaska_total = summary[summary['Airline'] == 'ALASKA']['Total_Flights'].sum()
alaska_rate = (alaska_delayed / alaska_total) * 100

# Calculate the delay % for AM WEST
amwest_delayed = summary[(summary['Airline'] == 'AM WEST') & (summary['Status'] == 'delayed')]['Total_Flights'].sum()
amwest_total = summary[summary['Airline'] == 'AM WEST']['Total_Flights'].sum()
amwest_rate = (amwest_delayed / amwest_total) * 100

print("--- Delay % ---")
print(f"Alaska Airlines Delay Rate: {alaska_rate:.2f}%")
print(f"AM West Airlines Delay Rate: {amwest_rate:.2f}%")
