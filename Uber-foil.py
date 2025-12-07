import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

import  chart_studio.plotly as py
import plotly.graph_objs as go
import plotly.express as px

from plotly.offline import download_plotlyjs, init_notebook_mode, plot


pd.set_option('display.max_columns', None)

import  warnings
from warnings import filterwarnings
filterwarnings("ignore")

directory = r"C:\Users\leona\PycharmProjects\Python Data Analysis Projects\UberNYAnalysis 2\DataAnalysisProjects\uber-raw-data-janjune-15_sample.csv"
uber_15 = pd.read_csv(directory)
# print(uber_15.columns)

directory2 = r"C:\Users\leona\PycharmProjects\Python Data Analysis Projects\UberNY-dataAnalysis\Uber-Jan-Feb-FOIL.csv"
uber_foil = pd.read_csv(directory2)
# print(uber_foil.head(5))

# init_notebook_mode(connected=True)

# fig = px.box(x='dispatching_base_number', y='active_vehicles', data_frame= uber_foil)
# fig.show()

figviolin = px.violin(x='dispatching_base_number', y='active_vehicles', data_frame= uber_foil)
figviolin.show()



