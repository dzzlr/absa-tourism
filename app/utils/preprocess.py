import re
import string

import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
from itertools import chain

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

def cleaning(text, remove_stop_words=True, lemmatize_words=True):
    text = text.lower() # Case folding
    text = text.strip() # Trim text
    # Remove punctuations, special characters, and double whitespace
    text = re.compile('<.*?>').sub('', text) 
    text = re.compile('[%s]' % re.escape(string.punctuation)).sub(' ', text)
    text = re.sub('\s+', ' ', text)
    # Number removal
    text = re.sub(r'\[[0-9]*\]', ' ', text) 
    text = re.sub(r'[^\w\s]', '', str(text).lower().strip())
    # Remove number and whitespaces
    text = re.sub(r'\d', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    
    if remove_stop_words:
        # load stopwords
        stop_words = set(chain(stopwords.words('indonesian'), stopwords.words('english')))
        text = text.split()
        text = [w for w in text if not w in stop_words]
        text = " ".join(text)
    
    if lemmatize_words:
        factory = StemmerFactory()
        stemmer = factory.create_stemmer()
        
        text = text.split()
        lemmatized_words = stemmer.stem(' '.join(text)).split(' ')
        text = " ".join(lemmatized_words)

    return text