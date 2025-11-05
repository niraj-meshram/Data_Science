import joblib
from deepface import DeepFace
import numpy as np
import os


classifier = None
label_encoder = None

base_dir = os.path.dirname(os.path.abspath(__file__))
artifact_path = os.path.join(base_dir, "artifacts")

def get_celebrity_name(image_path):
    load_artifacts()
    try:
        # Extract embedding using DeepFace
        embedding = DeepFace.represent(img_path=image_path, model_name="ArcFace", enforce_detection=False)[0]["embedding"]
        embedding = np.array(embedding).reshape(1, -1)

        # Predict the celebrity
        pred = classifier.predict(embedding)[0]
        proba = classifier.predict_proba(embedding).max()
        celebrity_name = label_encoder.inverse_transform([pred])[0]

        return celebrity_name, proba * 100
    except Exception as e:
        return str(e), None




def load_artifacts():
    print("Loading saved artifacts.....")

    global classifier
    global  label_encoder
    # Load the pre-trained model and label encoder
    classifier = joblib.load(os.path.join(artifact_path, "celebrity_classifier.pkl"))
    label_encoder = joblib.load(os.path.join(artifact_path, "label_encoder.pkl"))
    print("Loading the artifacts is done.")


if __name__ == "__main__":
    load_artifacts()