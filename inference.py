import joblib
from sklearn.datasets import load_iris


def load_model(path="model.joblib"):
    return joblib.load(path)


def predict(model, features: dict) -> str:
    # features to list in correct order
    X = [
        features["sepal_length"],
        features["sepal_width"],
        features["petal_length"],
        features["petal_width"],
    ]

    prediction_idx = model.predict([X])[0]

    # map index to class name
    iris = load_iris()
    return iris.target_names[prediction_idx]
