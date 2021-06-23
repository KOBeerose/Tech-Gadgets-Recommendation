# Dataframe
import pandas as pd

# Decompressing the file
import gzip


# Imporing a sample of Electronics Dataset with Pandas

with open('Data Science/Tech-Gadgets-Recommendation/Datasets/Sample_Cell_Phones_and_Accessories_5.json') as data:
    review_df = pd.read_json(data, orient='records', lines=True)

    """file_object = open("Tech-Gadgets-Recommendation/Data/test.json",'r')
for a in file_object:
    print(a)"""

# loads(json, precise_float=self.precise_float), dtype=None)

'''with open('Tech-Gadgets-Recommendation/Data/test.json') as json_file:      
    data = json_file.readlines()
    # this line below may take at least 8-10 minutes of processing for 4-5 million rows. It converts all strings in list to actual json objects. 
    data = list(map(json.loads, data)) 

print(pd.DataFrame(data))'''


# Indexing by the asin column

# Changing the the column name`
review_df = (review_df.rename(columns={'overall': 'Rating'})).set_index("asin")


# Checking the reviews sample

print("Total data:", str(review_df.shape))
print(review_df.head())


# Importing the Metadata of Electronics Dataset

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


dfmeta = getDF(
    'Data Science/Tech-Gadgets-Recommendation/Datasets/Sample_meta_Cell_Phones_and_Accessories.json.gz')


# Indexing by the asin column

#meta_df = dfmeta.set_index("asin")
meta_df = dfmeta.set_index("asin")

# Checking the metadata sample
print("Total metadata:", str(meta_df.shape))
print(meta_df.head())

## Merging Reviews with Metadata

product_reviews=pd.merge(review_df,meta_df,on='asin', how='left')

print(product_reviews.head())

print ("Total products:", str(product_reviews.shape))

product_reviews.info()




## Extracting Cell Phones from title column

# Drop null values in proudct title column 
product_reviews=product_reviews.dropna(subset=['title'])

phone_reviews = product_reviews[product_reviews["title"].str.contains("phone|phones|Phone|Phones|cell|Cell|mobile ")]

print("Total products:", phone_reviews.shape)

# cheking the missing values

print(phone_reviews.isnull().sum())

# Dropping some columns from the Dataset

phone_reviews=phone_reviews.drop(['style','image','vote','reviewerID','reviewTime','verified','reviewerName','tech1','tech2','main_cat','also_view','also_buy','unixReviewTime','date','imageURL'],axis=1)


# Dropping null value columns

phone_reviews=phone_reviews.dropna(subset=['reviewText','summary'])

# Last check

print(phone_reviews.isnull().sum())

print(phone_reviews.info())