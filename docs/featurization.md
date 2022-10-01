# featurization stage

```python
from sklearn.featur_extraction import CountVectorizer

max_features = 4
ngrams = 2

vectorizer = CountVectorizer(max_features-max_features, ngrams_range=(1,ngrams))
x = vectorizer.fit_transform(corpus)
print(x.toarray())
print(vectorizer.get_feature_names_out())
```