# Text to Image Generator

A simple Python application that allows users to generate images from text prompts using Hugging Face's `FLUX.1-schnell` model. Includes both a CLI script and a Flask web interface.

## Prerequisites

- Python 3.8+
- Hugging Face API Token (Get one for free at [huggingface.co](https://huggingface.co))

## Installation

1. Clone this repository:
   ```bash
   git clone <your-repo-url>
   cd "Text to image"
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure your API token:
   - Rename `.env.example` to `.env`
   - Open `.env` and replace `your_huggingface_api_token_here` with your actual Hugging Face API token.

## Usage

### Web Interface
Run the Flask server:
```bash
python app.py
```
Then open `http://127.0.0.1:5000` in your web browser.

### Command Line Interface
Run the CLI script:
```bash
python text_to_image.py
```
