import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import nltk
import string

df = pd.read_csv("clickbait_data.csv", header=0)

X = df['headline']
y = df['clickbait']

train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.7, random_state=0)

def remove_punctuation(row):
    new_row = []
    for r in row:
        for j in string.punctuation:
            r = r.replace(j, '')
        new_row.append(r)
    return new_row

def transform_data(raw):
    raw = raw.apply(lambda x: x.split()) # Break into words (tokenise)
    raw = raw.apply(lambda x: [word.lower() for word in x]) # Make lower case
    raw = raw.apply(remove_punctuation) # Remove punctuation
    raw = raw.apply(lambda x: [''.join([i for i in word if not i.isdigit()]) for word in x])  # Remove digits
    raw = raw.apply(lambda x: [word for word in x if word not in stopwords.words('english')]) # Remove stopwords
    raw = raw.apply(lambda x: [word.strip() for word in x if word != '']) # Strip whitespace and remove empty strings
    
    lem = nltk.stem.WordNetLemmatizer()
    raw = raw.apply(lambda x: [lem.lemmatize(word) for word in x]) # lemmatise the words

    transformed = raw.apply(lambda x: ''.join(i + ' ' for i in x))
    return transformed

train_X = transform_data(train_X)
test_X = transform_data(test_X)

text_clf = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', MultinomialNB())
])

text_clf.fit(X, y)
#test_eg = ['Coronavirus: NSW records 13 new cases of COVID-19', 'Try this out and see what happens!', 'The personality cult Donald Trump launched in 2016 has subsumed the Republican Party', 'The University of Paris-Saclay has a teaching and research staff of 9,000, catering to 48,000 students—more than Harvard or Stanford', 'Bulgarians have been Europe’s gardeners longer than you think', 'Huge news as universe ending threat approaches planet Earth!!!']
#test_eg = transform_data(pd.Series(['Huge news as universe ending threat approaches planet Earth!!!', 'Coronavirus: NSW records 13 new cases of COVID-19', 'Try this out and see what happens!', 'The personality cult Donald Trump launched in 2016 has subsumed the Republican Party', 'The University of Paris-Saclay has a teaching and research staff of 9,000, catering to 48,000 students—more than Harvard or Stanford', 'Bulgarians have been Europe’s gardeners longer than you think']))
def predictor(content=test_X):

    prediction = text_clf.predict(content)
    
    return prediction

# from sklearn.metrics import confusion_matrix
# print(confusion_matrix(test_y, predictor(test_eg)))

# from sklearn.metrics import classification_report
# print("Classification Report")
# print(classification_report(test_y,predictor(test_eg)))
#scores = cross_val_score(text_clf, X, y, cv=10) 
#print(scores)
#print(text_clf.score(X_test, y_test))

# for p in prediction:
#     if p:
#         print("Clickbait")
#     else:
#         print("Not clickbait")

#print(prediction)
