
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
    
with open('Data Science/Tech-Gadgets-Recommendation/Datasets/Sample_Electronics.json') as data:
    review_df = pd.read_json(data, orient='records', lines=True)


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


##########################################
## IMPORT ELECTRONICS PRODUCT METADATA IN PANDAS
##########################################

import gzip

def parse(path):
  g = gzip.open(path, 'rb')
  for l in g:
    yield eval(l)

def getDF(path):
  i = 0
  df = {}
  for d in parse(path):
    df[i] = d
    i += 1
  return pd.DataFrame.from_dict(df, orient='index')

dfmeta = getDF('Data Science/Tech-Gadgets-Recommendation/Datasets/meta_Electronics.json.gz')

print(dfmeta.head())

