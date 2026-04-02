import requests
from PIL import Image
import io
import os
from dotenv import load_dotenv

load_dotenv()

# Your Hugging Face API token
API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")
API_URL = "https://router.huggingface.co/hf-inference/models/black-forest-labs/FLUX.1-schnell"

def generate_image(prompt):
    print(f"Generating image for: '{prompt}'...")
    
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    payload = {"inputs": prompt}
    
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        
        if response.status_code == 200:
            # Read the image content and display/save it
            imageBytes = io.BytesIO(response.content)
            image = Image.open(imageBytes)
            
            # Display and save the image
            image.show()
            image.save("generated_image.png")
            print("\nSuccess! Your dragon image has been saved as 'generated_image.png'.")
        else:
            print(f"Error ({response.status_code}): {response.text}")
            
    except Exception as e:
        print(f"Error generating image: {e}")

if __name__ == "__main__":
    # Ask the user for the text prompt
    text_prompt = input("Enter a text prompt to generate an image: ")
    generate_image(text_prompt)
