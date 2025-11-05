import os
from flask import render_template

from flask import  Flask, request, jsonify
import util

# Find the parent folder of server.py (which contains templates/)
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
app = Flask(__name__, template_folder=template_dir)


@app.route("/flask")
def hello():
    return "This is flask server!"


# Serve Frontend
@app.route("/")
def home():
    return render_template('index.html')

# Upload + Predict endpoint
@app.route("/upload_and_predict", methods=["POST"])
def upload_and_predict():
    try:
        if 'image' not in request.files:
            return jsonify({"error": "No image uploaded."}), 400

        img = request.files['image']

        # Save to uploads/ folder
        uploads_dir = os.path.join(os.getcwd(), 'uploads')
        os.makedirs(uploads_dir, exist_ok=True)
        img_path = os.path.join(uploads_dir, img.filename)
        img.save(img_path)

        # Predict
        celebrity_name, confidence = util.get_celebrity_name(img_path)

        return jsonify({
            "celebrity": celebrity_name,
            "confidence": round(confidence, 2) if confidence else 0.0
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/get_celebrity_name", methods=['POST'])
def get_celebrity_name():
    try:
        # Parse request
        data = request.get_json()
        image_path = data.get('image_path')

        if not image_path or not os.path.exists(image_path):
            return jsonify({"error": "Invalid or missing image path."}), 400

        # Run prediction
        celebrity_name, confidence = util.get_celebrity_name(image_path)

        if celebrity_name:
            return jsonify({
                "celebrity": celebrity_name,
                "confidence": round(confidence, 2) if confidence else 0.0
            }), 200
        else:
            return jsonify({"error": "Prediction failed", "message": confidence}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
    print("Starting python flask server for celebrity prediction....")
    app.run(debug=True)