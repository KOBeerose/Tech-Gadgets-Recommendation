
# Dataframe
import pandas as pd
import json
# Array
import numpy as np

# Decompress the file
import gzip

# Visualizations
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import seaborn as sns
import matplotlib.colors as colors


# Datetime
from datetime import datetime

## Warnings
import warnings
from scipy import stats
warnings.filterwarnings('ignore')

# Large dataset
import dask.bag as db




##########################################
## IMPORT ELECTRONICS PRODUCT REVIEW DATA IN PANDAS
##########################################

"""file_object = open("Tech-Gadgets-Recommendation/Data/test.json",'r')
for a in file_object:
    print(a)"""

    #loads(json, precise_float=self.precise_float), dtype=None)
    
with open('Tech-Gadgets-Recommendation/Data/test.json') as data:
    review_df = pd.read_json(data, orient='records', lines=True, encoding='utf-8')


'''with open('Tech-Gadgets-Recommendation/Data/test.json') as json_file:      
    data = json_file.readlines()
    # this line below may take at least 8-10 minutes of processing for 4-5 million rows. It converts all strings in list to actual json objects. 
    data = list(map(json.loads, data)) 

print(pd.DataFrame(data))'''



##########################################
## CHECK DATA IN PANDAS
##########################################

# change column name 
review_df = review_df.rename(columns={'overall': 'Rating'})

print ("Total data:", str(review_df.shape))
print(review_df.head())
