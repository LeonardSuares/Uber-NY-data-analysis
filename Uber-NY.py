import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# print(os.getcwd())

# path = r"C:\Users\leona\PycharmProjects\Python Data Analysis Projects\UberNYAnalysis 2\DataAnalysisProjects\uber-raw-data-janjune-15_sample.csv"
# uber_15 = pd.read_csv(path)
# uber_15.head(5)

directory = r"C:\Users\leona\PycharmProjects\Python Data Analysis Projects\UberNYAnalysis 2\DataAnalysisProjects\uber-raw-data-janjune-15_sample.csv"
# for i in directory:
#     print(i)

uber_15 = pd.read_csv(directory)
print(uber_15)