# CodeAlpha Task 2: FAQ Chatbot

## Project Description
This project is an FAQ Chatbot developed as part of the CodeAlpha internship. It answers frequently asked questions about college courses, admissions, scholarships, fees, examinations, results, and facilities.

The chatbot uses text processing and similarity matching to identify user questions and return relevant answers. It also provides responses to greetings and thank-you messages.

## Features
- Answers frequently asked questions.
- Uses NLP-based text processing.
- Matches user questions with stored FAQs.
- Handles greetings and thank-you messages.
- Provides fallback responses for unsupported questions.
- Includes a web interface built using HTML, CSS, and JavaScript.

## Technologies Used
- Python
- NLTK
- Flask
- HTML
- CSS
- JavaScript
- JSON

## Project Structure
- `main.py` — Chatbot logic and question matching.
- `app.py` — Flask web application.
- `faqs.json` — Frequently asked questions and answers.
- `templates/index.html` — Chatbot webpage.
- `static/style.css` — Webpage styling.
- `static/script.js` — Chat interface functionality.
- `requirements.txt` — Python dependencies.

## How to Run

1. Install Python.
2. Install the required packages:

   `pip install -r requirements.txt`

3. Start the application:

   `python app.py`

4. Open your browser and visit:

   `http://127.0.0.1:5000`

## Project Purpose
The purpose of this project is to demonstrate a simple FAQ chatbot that processes user questions and provides relevant answers through a web interface.