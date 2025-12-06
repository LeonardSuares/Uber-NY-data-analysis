import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

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

print(uber_15.shape)
print(dupdrop.shape)
# print(dupdrop)

#TO find the number of null values in the CSV
isnullitems = dupdrop.isnull().sum()
print(isnullitems)

#TO find the datatypes and update the datatypes of columns
csvdata = dupdrop.dtypes
print(csvdata)

# print(dupdrop.head(1))
dupdrop["Pickup_date"] = pd.to_datetime(dupdrop["Pickup_date"])
print(dupdrop.dtypes)