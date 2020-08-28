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

train_X = train_X.apply(lambda x: x.split()) # break into words (tokenise)
test_X = test_X.apply(lambda x: x.split())

train_X = train_X.apply(lambda x: [word.lower() for word in x]) # make lower case
test_X = test_X.apply(lambda x: [word.lower() for word in x])

def remove_punctuation(row):
    new_row = []
    for r in row:
        for j in string.punctuation:
            r = r.replace(j, '')
        new_row.append(r)
    return new_row

train_X = train_X.apply(remove_punctuation)
test_X = test_X.apply(remove_punctuation)

train_X = train_X.apply(lambda x: [''.join([i for i in word if not i.isdigit()]) for word in x]) # hahahahhahahahahahha
test_x = test_X.apply(lambda x: [''.join([i for i in word if not i.isdigit()]) for word in x])   # removes digits from text somehow

train_X = train_X.apply(lambda x: [word for word in x if word not in stopwords.words('english')]) # Remove stopwords
test_X = test_X.apply(lambda x: [word for word in x if word not in stopwords.words('english')])

train_X = train_X.apply(lambda x: [word.strip() for word in x if word != '']) # strip whitespace
test_X = test_X.apply(lambda x: [word.strip() for word in x if word != ''])

# train_X = train_X.apply(lambda x: [word for word in x if word != ''])
# test_X = test_X.apply(lambda x: [word for word in x if word != ''])
lem = nltk.stem.WordNetLemmatizer()
train_X = train_X.apply(lambda x: [lem.lemmatize(word) for word in x]) # lemmatise the words
test_X = test_X.apply(lambda x: [lem.lemmatize(word) for word in x])

print(train_X.head)
# def make_lower(row):
#     return [word.lower() for word in row]





count_vect = CountVectorizer()

X_train_counts = count_vect.fit_transform(X)

tfidf_transformer = TfidfTransformer()

X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)
#clf = MultinomialNB().fit(X_train_tfidf, y)

text_clf = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', MultinomialNB())
])

text_clf.fit(X, y)
test_eg = ['Coronavirus: NSW records 13 new cases of COVID-19', 'Try this out and see what happens!', 'The personality cult Donald Trump launched in 2016 has subsumed the Republican Party', 'The University of Paris-Saclay has a teaching and research staff of 9,000, catering to 48,000 students—more than Harvard or Stanford', 'Bulgarians have been Europe’s gardeners longer than you think']

# X_new_counts = count_vect.transform(test_eg)
# X_new_tfidf = tfidf_transformer.transform(X_new_counts)

prediction = text_clf.predict(test_eg)
print(prediction)
#scores = cross_val_score(text_clf, X, y, cv=10)
#print(scores)
#print(text_clf.score(X_test, y_test))

# for p in prediction:
#     if p:
#         print("Clickbait")
#     else:
#         print("Not clickbait")

#print(prediction)