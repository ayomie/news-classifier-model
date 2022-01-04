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

def load_final_model():
    with open('pipe.pickle', 'rb') as picklefile:
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
        saved_pipe = pickle.load(picklefile)
        
    return saved_pipe


def predict(text):
    saved_pipe = load_final_model()
    pred = saved_pipe.predict([text])
    
    return pred