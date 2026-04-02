from flask import Flask, render_template, request, jsonify
import requests
import io
import os
import time
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Ensure the static/images directory exists for serving saved images
os.makedirs(os.path.join("static", "images"), exist_ok=True)

# Your Hugging Face API token
API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")
API_URL = "https://router.huggingface.co/hf-inference/models/black-forest-labs/FLUX.1-schnell"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    prompt = data.get("prompt")
    
    if not prompt:
        return jsonify({"success": False, "error": "No prompt provided"}), 400

    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    payload = {"inputs": prompt}
    
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        
        if response.status_code == 200:
            # Read the image content
            imageBytes = io.BytesIO(response.content)
            image = Image.open(imageBytes)
            
            # Generate a unique filename using timestamp
            filename = f"generated_{int(time.time())}.png"
            filepath = os.path.join("static", "images", filename)
            
            # Save the image into the static directory
            image.save(filepath)
            
            # Return the URL string to the frontend
            return jsonify({
                "success": True, 
                "image_url": f"/{filepath.replace(os.sep, '/')}" 
            })
        else:
            return jsonify({"success": False, "error": f"API Error ({response.status_code}): {response.text}"}), 500
            
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == "__main__":
    print("Starting Flask Web Server...")
    print("Open your browser and visit: http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
