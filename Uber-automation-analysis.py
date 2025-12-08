import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import folium
import webbrowser
import  chart_studio.plotly as py
import plotly.graph_objs as go
import plotly.express as px

from plotly.offline import download_plotlyjs, init_notebook_mode, plot


pd.set_option('display.max_columns', None)

import  warnings
from warnings import filterwarnings
filterwarnings("ignore")

directory = r"C:\Users\leona\PycharmProjects\Python Data Analysis Projects\UberNY-dataAnalysis\DataAnalysisProjects"
files = os.listdir(directory)[-8:]
# print(len(uber_pickup))
# files1 = pd.read_csv(r"C:\Users\leona\PycharmProjects\Python Data Analysis Projects\UberNY-dataAnalysis\DataAnalysisProjects\uber-raw-data-janjune-15.csv")
# print(files1.head(5))
files.remove('uber-raw-data-janjune-15.csv')
files.remove('uber-raw-data-janjune-15_sample.csv')
# print(files)
#
final = pd.DataFrame()

path = r"C:\Users\leona\PycharmProjects\Python Data Analysis Projects\UberNY-dataAnalysis\DataAnalysisProjects"
for file in files:
    current_df = pd.read_csv(path+'/'+file)
    final = pd.concat([current_df, final])

# final.duplicated().sum()
# print(final.duplicated().sum())
final.drop_duplicates(inplace=True)
final['Date/Time'] = pd.to_datetime(final['Date/Time'], format="%m/%d/%Y %H:%M:%S")
final['day'] = final['Date/Time'].dt.day
final['hour'] = final['Date/Time'].dt.hour
# print(final.head(4))
def gen_pivot_table(df, col1, col2):
    pivot = final.groupby([col1, col2]).size().unstack()
    # pivotstyle = pivot.style.background_gradient()
    plt.figure(figsize=(6, 4))
    sns.heatmap(pivot, annot=True, cmap="coolwarm", fmt=".0f", linewidths=.5, annot_kws={"fontsize": 8})
    plt.title('Uber Hour and Day Pairwise Analysis')
    return plt.show()

gen_pivot_table(final, "day", "hour")

