#
# taken from:
#       https://lvngd.com/blog/text-normalization-natural-language-processing-python/
#

import re
import string
import unidecode
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import gensim.downloader as api
from pycontractions import Contractions
from word2number import w2n



sample_text = text = "“Everything we’re doing is about going forward,” Phoebe Philo told Vogue in 2009, shortly before showing her debut Resort collection for Céline. Although the label had garnered headlines when it was revived by Michael Kors in the late ’90s, it was Philo who truly brought the till then somewhat somnambulant luxury house to the forefront. Critics credited her with pushing fashion in a new direction, toward a more spare, stripped-down kind of sophistication. What Céline now offered women was, as the magazine put it, “a grown-up and hip way to put themselves together.”"


sentences = sent_tokenize(sample_text)
print(f"Using sentence tokenization, found {len(sentences)} sentences:")
print(sentences)
