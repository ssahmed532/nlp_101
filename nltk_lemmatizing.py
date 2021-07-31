import text_samples
from nltk.stem     import WordNetLemmatizer
from nltk.tokenize import word_tokenize


lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("scarves"))
print(lemmatizer.lemmatize("worst"))
print(lemmatizer.lemmatize("worst", pos="a"))
print(2 * '\n')

words = word_tokenize(text_samples.string_for_lemmatizing)
print("Word tokens:")
print(words)
print(2 * '\n')

lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
print("Lemmatized word tokens:")
print(lemmatized_words)
print(2 * '\n')
