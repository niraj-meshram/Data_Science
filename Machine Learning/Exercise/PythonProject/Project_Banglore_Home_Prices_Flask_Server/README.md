# Bangalore Home Prices Flask Server

Overview
- Minimal Flask API that serves home price predictions using the trained model artifacts.

What It Does
- Exposes HTTP endpoints that load `columns.json` and the model pickle to return predicted prices for input features.

Run
- From `server/`, install requirements and run `python server.py`.
- Frontend under `client/` can be opened in a browser to call the API.

