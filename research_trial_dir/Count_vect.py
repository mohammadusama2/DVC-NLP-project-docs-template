from numpy import vectorize
from sklearn.feature_extraction.text import CountVectorizer


corpus = [
    "zebra apple ball cat",
    "ball cat dog elephant",
    "very very unique"
]

# vectorizer = CountVectorizer()
# x = vectorizer.fit_transform(corpus)
# print(x.toarray())
# print(vectorizer.get_feature_names_out())

max_features = 100
ngrams = 3

vectorizer = CountVectorizer(max_features=max_features, ngram_range=(1, ngrams))
x = vectorizer.fit_transform(corpus)
print(x)
print(x.toarray())
print(vectorizer.get_feature_names_out())