#
# Tested using nltk 3.5
#
# Code is based on the following article:
#
# https://realpython.com/nltk-nlp-python/
#

from nltk.stem import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import word_tokenize


sample_text1 = """
The crew of the USS Discovery discovered many discoveries.
Discovering is what explorers do."""


stemmer = PorterStemmer()

words = word_tokenize(sample_text1)
print(words)

stemmed_words = [stemmer.stem(word) for word in words]
print("Stemmed words using the Porter Stemmer:")
print(stemmed_words)
print(3 * '\n')

snow_stemmer = SnowballStemmer('english')
stemmed_words2 = [snow_stemmer.stem(word) for word in words]
print("Stemmed words using the Snowball Stemmer:")
print(stemmed_words2)
