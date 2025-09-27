# PlushIntel 🐾

PlushIntel is a whimsical chat application designed for Labubu, the mischievous plush toy. Powered by Google's Gemini API, PlushIntel acts as a playful assistant, offering fun facts, collection tips, and toy-friendly advice.

## Features

-   **Interactive Chat Interface:** A simple and cute web-based chat window.
-   **Playful AI Assistant:** The backend is configured with a system prompt to be a helpful and playful companion for a plush toy.
-   **Session-based Memory:** Remembers the conversation history for the current session.
-   **Flask-powered:** A lightweight and simple web framework for the backend.
-   **Gemini API Integration:** Uses the `google.generativeai` library to connect to the Gemini API.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/soccera1/plushintel.git
    cd plushintel
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: A `requirements.txt` file may need to be created if it doesn't exist. Based on `app.py`, the dependencies are `Flask` and `google-generativeai`)*

4.  **Set up your API key:**
    You need to have a Gemini API key. Set it as an environment variable:
    ```bash
    export GEMINI_API_KEY="your-api-key-here"
    ```

## Usage

1.  **Run the Flask application:**
    ```bash
    python app.py
    ```

2.  **Open your browser:**
    Navigate to `http://127.0.0.1:5000` to start chatting with PlushIntel!
