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

# print(final.head(5))
# print(groupLL)
avg_lat = final['Lat'].mean()
avg_lon = final['Lon'].mean()

basemap = folium.Map(location=[avg_lat, avg_lon], zoom_start=11)
rush_uber = final.groupby(['Lat','Lon'], as_index=False).size()

data = rush_uber[['Lat','Lon', 'size']].values.tolist()

from folium.plugins import HeatMap
HeatMap(data).add_to(basemap)

# print(basemap)
#
map_file_path = "index.html"
basemap.save(map_file_path)

webbrowser.open_new_tab(os.path.abspath(map_file_path))
