"""
lmhm a si l batouri khask d5el hadchi
pip ola conda install spacy
       //             nltk
       //             textblob
python -m spacy download en_core_web_sm
"""

# We get started by importing spacy
import spacy
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
from nltk.tokenize import sent_tokenize



# keywords_extraction function hiya li ghat7tatj ghat3tiha string f7al hada w ghat3refj 3lik array dyal features 

review="I want a pink phone. that takes beautiful pictures. A nice big screen. And I want the battery to be really good"


def review_to_sentences(review):
    tokenized_review=sent_tokenize(review)
    return tokenized_review


def Extract_features(review):
    sentences=review_to_sentences(review)
    aspects= []
    description = []
    nlp = spacy.load("en_core_web_sm")  
    for sentence in sentences:
        doc = nlp(sentence)
        descriptive_term = ''
        target = ''
        for token in doc:
            if token.dep_ == 'nsubj' or token.pos_ == 'NOUN':
                target = token.text
            if token.pos_ == 'ADJ':
                prepend = ''
                for child in token.children:
                    if child.pos_ != 'ADV':
                        continue
                    prepend += child.text + ' '
                descriptive_term = prepend + token.text
        aspects.append(target)
        description.append(descriptive_term)
    return aspects, description

def Classify_and_stats(review):
    aspects=Extract_features(review)[0]
    description=Extract_features(review)[1]
    # We train the NaivesBayesClassifier
    train = [
    ('it flies best performace really fast uptodate smooth animation gaming boottime', 'positive'),
    ('Slowdowns bad performace really slow unusable outdated bugs glitches', 'negative'),
    ('good battery-live stands all the day never need to charge reliable long screen-on time', 'positive'),
    ('bad battery-live dies shortly you need to charge always not reliable short screen-on time', 'negative'),
    ('Big amoled screen deep colors 2k 1440p 1080p full hd super amoled beautiful watch content', 'positive'),
    ('small TN screen shallow colors low resolution bad content consumption experice watch content ', 'negative'),
    ('very good value for the money affoardable fair price it is worth it', 'positive'),
    ('bad good value for the money very exprensive it is overpriced and not worth it', 'positive'),
    ]
    output=[]
    cl = NaiveBayesClassifier(train)
    # And then we try to classify some sample sentences.
    blob = TextBlob(review, classifier=cl)
    i=0
    for s in blob.sentences:
        sentence=blob.sentences[i]
        output.append({i: sentence,
        'aspects' : aspects[i],
        'description' : description[i],
        'stats': s.sentiment,
        'classify' : s.classify()})
        i+=1
    return output

def Features_mapping(review):
    output=[]
    Classify_and_stats(review)
    return output


def keywords_extraction(review):
    sentences=review_to_sentences(review)
    keywords= []
    nlp = spacy.load("en_core_web_sm")  
    for sentence in sentences:
        doc = nlp(sentence)
        descriptive_term = ''
        target = ''
        for token in doc:
            if token.dep_ == 'nsubj' or token.pos_ == 'NOUN':
                target = token.text
            if token.pos_ == 'ADJ' or token.pos_ == 'NUM' or token.pos_ == 'VERB':
                prepend = ''
                for child in token.children:
                    if child.pos_ != 'fds':
                        continue
                    prepend += child.text + ' '
                descriptive_term = prepend + token.text
        keywords.append(descriptive_term)
        keywords.append(target)
    return keywords



print("the review text is: ",review)
print(Classify_and_stats(review))

