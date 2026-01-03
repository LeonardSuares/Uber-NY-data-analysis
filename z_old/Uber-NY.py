import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
pd.set_option('display.max_columns', None)
import  warnings
from warnings import filterwarnings
filterwarnings("ignore")

# print(os.getcwd())

# path = r"C:\Users\leona\PycharmProjects\Python Data Analysis Projects\UberNYAnalysis 2\DataAnalysisProjects\uber-raw-data-janjune-15_sample.csv"
# uber_15 = pd.read_csv(path)
# uber_15.head(5)

directory = r"C:\Users\leona\PycharmProjects\Python Data Analysis Projects\UberNYAnalysis 2\DataAnalysisProjects\uber-raw-data-janjune-15_sample.csv"
# for i in directory:
#     print(i)

uber_15 = pd.read_csv(directory)

# print(uber_15.head(5))
#TO find the number of duplicate values in the CSV
dup1 = uber_15.duplicated().sum()

#TO drop the number of duplicate values in the CSV
dupdrop = uber_15.drop_duplicates()

# print(uber_15.shape)
# print(dupdrop.shape)
# print(dupdrop)

#TO find the number of null values in the CSV
isnullitems = dupdrop.isnull().sum()
# print(isnullitems)

#TO find the datatypes and update the datatypes of columns
csvdata = dupdrop.dtypes
# print(csvdata)

# print(dupdrop.head(1))
dupdrop["Pickup_date"] = pd.to_datetime(dupdrop["Pickup_date"])
# print(dupdrop.dtypes)

dupdrop['month'] = dupdrop['Pickup_date'].dt.month_name()
# print(dupdrop['month'])

#To Plot a graph = Bar chart
# dupplot = dupdrop['month'].value_counts().plot(kind = 'bar')
# # dupplot.plot(dupplot)
# plt.ylabel("# of Rides")
#
# # Optional: Add x-axis label and a main title
# plt.xlabel("Month")
# plt.title("Uber NY Analysis")
# plt.show()
dupdrop['weekday'] = dupdrop['Pickup_date'].dt.day_name()
dupdrop['day'] = dupdrop['Pickup_date'].dt.day
dupdrop['hour'] = dupdrop['Pickup_date'].dt.hour
dupdrop['minute'] = dupdrop['Pickup_date'].dt.minute
# print(dupdrop.head(5))

#To plot the weekly ride analysis
pivot = pd.crosstab(index = dupdrop['month'], columns= dupdrop['weekday'])
pivotplot = pivot.plot(kind = 'bar', figsize = (8,6))
plt.ylabel("# of Rides")
plt.xlabel("Month")
plt.title("Uber NY weekday Analysis")
plt.show()
#To confirm the file is up-to-date
