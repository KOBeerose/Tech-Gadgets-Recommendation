# Dataframe
import dask.bag as db
from scipy import stats
import warnings
from datetime import datetime
import pandas as pd

# Array
import numpy as np

# Decompress the file
import gzip

# Visualizations
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import seaborn as sns
import matplotlib.colors as colors
%matplotlib inline

# Datetime

# Warnings
warnings.filterwarnings('ignore')

# Large dataset

# IMPORT ELECTRONICS PRODUCT REVIEW DATA IN PANDAS
##########################################

review_df = pd.read_json('C:\Users\tahae\OneDrive - ine.inpt.ma\Coding\Data Science\Tech-Gadgets-Recommendation\Data/reviews_Electronics_5.json', orient='records', lines=True)
