
from flask import Flask, render_template, request, jsonify
from main import FAQChatbot, load_faqs

app = Flask(__name__)

faqs = load_faqs()
chatbot = FAQChatbot(faqs)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "").strip()

    if not message:
        return jsonify({"answer": "Please type a question."})

    answer = chatbot.get_answer(message)
    return jsonify({"answer": answer})


if __name__ == "__main__":
    app.run(debug=True)
