#import libraries
import numpy as np
import pandas as pd
import re, pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.externals import joblib

# score_text ( text ) - function to score text
#   parameters:
#     text - the entire text of the email
#   returns:
#     aggressive_score  - the probability score that the text is aggressive
#
#   example: score = score_text ( text )
#
def score_text ( text ):
    
    # unpickle our dictionary and model
    with open ( "dictionary.pkl", "rb" ) as fp:
        dict = pickle.load ( fp )

    model = joblib.load ( 'ThreatClassificationModel.pkl' )
    
    # cleanse our text (may be unnecessary)
    clean_text = re.sub('[^a-zA-Z]+',' ', text).lower()

    # set up the vectorizer with our dictionary
    vectorizer = CountVectorizer(stop_words='english', vocabulary=dict)
    verbatimsVec = vectorizer.fit_transform([clean_text])
    
    # clean up our features set into a tidy dataframe and score
    wordCounts = pd.DataFrame(verbatimsVec.toarray(), columns=dict) # convert vectors to a dataframe
    aggressive_score = 1.0 - model.predict_proba ( wordCounts ) [:,0] [0]
    
    return aggressive_score

def main(params):
    print(params)
    score = score_text(params["text"])
    resp = {"score": score}
    print(resp)
    return resp
