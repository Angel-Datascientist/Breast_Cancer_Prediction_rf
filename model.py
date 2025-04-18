import pickle

def load_model():
    with open("model/breast_cancer_rf_model.sav", "rb") as file:
        model = pickle.load(file)
    return model