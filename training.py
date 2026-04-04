from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib


def load_data():
    data = load_iris()
    return data.data, data.target, data.target_names


def train_model():
    X, y, _ = load_data()
    model = RandomForestClassifier()
    model.fit(X, y)
    return model


def save_model(model, path="model.joblib"):
    joblib.dump(model, path)


if __name__ == "__main__":
    model = train_model()
    save_model(model)
    print("Model trained and saved.")
