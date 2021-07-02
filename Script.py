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

# Changing the the column name
review_df = (review_df.rename(columns={'overall': 'Rating'})).set_index("asin")


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


## Merging Reviews with Metadata

product_reviews=pd.merge(review_df,meta_df,on='asin', how='left')


## Extracting Cell Phones from title column

# Drop null values in proudct title column 
product_reviews=product_reviews.dropna(subset=['title'])

phone_reviews = product_reviews[product_reviews["title"].str.contains("phone|phones|Phone|Phones|cell|Cell|mobile ")]



# Dropping some columns from the Dataset


phone_reviews=phone_reviews.drop(['style','image','reviewerID','reviewTime','verified','reviewerName','tech1','tech2','main_cat','also_view','also_buy','unixReviewTime','date','imageURL'],axis=1)


# Dropping null value columns

phone_reviews=phone_reviews.dropna(subset=['reviewText','summary','vote'])




# Saving Dataframe in csv 

phone_reviews.to_csv('Datasets/phone_reviews.csv', sep=',', index = False)


# Concatenate reviewText and summary 

phone_reviews['review_text'] = phone_reviews[['summary', 'reviewText']].apply(lambda x: " ".join(str(y) for y in x if str(y) != 'nan'), axis = 1)
cln_phone_reviews = phone_reviews.drop(['reviewText', 'summary'], axis = 1)



# Apply a helpfullness ratio from votes

cln_phone_reviews['helpfulness'] = cln_phone_reviews['vote'].apply(lambda x: x/100)
cln_phone_reviews = cln_phone_reviews.drop('vote', axis = 1)

# adding a classification of the rating


cln_phone_reviews['rating_class'] = cln_phone_reviews['Rating'].apply(lambda x: 'bad' if x < 3 else'good')


# Shifting asin to the first position

first_column = cln_phone_reviews.pop('asin')
cln_phone_reviews.insert(0, 'asin', first_column)


# Rename the columns
cln_phone_reviews.columns = ['product_id','rating','category','description','title','brand','feature','rank','details','related','price','img_url','review_text','helpfulness','rating_class']