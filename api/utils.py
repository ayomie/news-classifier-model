import pickle

def tokenize(text):
    from nltk.stem import WordNetLemmatizer
    from nltk import word_tokenize

    '''
    PARAMETERS 
        text (str): Text to be processed   
    RETURN
        Returns a processed text variable that was tokenized, lower cased, stripped, and lemmatized
    '''
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()
    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens