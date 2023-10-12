import re

def clean_from_tweet(text):
    text = re.sub(r"RT", ' ', text)
    text = re.sub(r"@[A-Za-z0-9]+", ' ', text)
    text = re.sub(r"#[A-Za-z0-9]+", ' ', text)
    text = re.sub(r"(?:\@|http?\://|https?\://|www)\S+", ' ', text)
    text = re.sub(r"[^\w\s]", ' ', text)
    text = re.sub('\s+', ' ', text)
    text = text.strip()
    text = text.lower()
    text = text.split()
    return text

def cleaning(text):
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

    return text