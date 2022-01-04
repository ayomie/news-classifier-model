from django.apps import AppConfig

def load_final_model():
    import pickle
    from .utils import tokenize
    with open('pipe.pickle', 'rb') as picklefile:
        saved_pipe = pickle.load(picklefile)
        
    return saved_pipe


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def predict(text):
        saved_pipe = load_final_model()
        pred = saved_pipe.predict([text])
        
        return pred
