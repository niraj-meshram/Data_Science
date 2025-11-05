# Celebrity Image Detection

Overview
- Face recognition pipeline using deep face embeddings (e.g., FaceNet/ArcFace) and a classifier.
- Detects a celebrity class for an input face image.

What It Does
- Extracts embeddings from face images and classifies them with a trained model; provides a Flask UI for inference.

Assets
- Large weights and datasets are not committed. Place required `.h5`/`.pkl` files under `model/` and test images under `model/test_images/`.

Run
- Install requirements, start the server (`server/server.py`), and open `ui/index.html` to test.

