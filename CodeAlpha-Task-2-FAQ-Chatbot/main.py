import json
import nltk
import re
from difflib import SequenceMatcher


def clean_text(text):
    text = text.lower()
    words = nltk.wordpunct_tokenize(text)
    words = [
        re.sub(r"[^a-z0-9]", "", word)
        for word in words
    ]
    words = [word for word in words if word]
    return " ".join(words)


def load_faqs():
    with open("faqs.json", "r", encoding="utf-8") as file:
        return json.load(file)


def similarity(user_question, faq_question):
    user_text = clean_text(user_question)
    faq_text = clean_text(faq_question)

    user_words = set(user_text.split())
    faq_words = set(faq_text.split())

    if not user_words or not faq_words:
        return 0

    # Exact match
    if user_text == faq_text:
        return 1.0

    # Ignore common words that don't describe the topic
    common_words = {
        "what", "is", "are", "the", "a", "an", "how",
        "can", "i", "do", "when", "where", "me", "my",
        "please", "tell", "about", "does", "to", "for"
    }

    user_keywords = user_words - common_words
    faq_keywords = faq_words - common_words

    if not user_keywords or not faq_keywords:
        return 0

    # Require at least one meaningful word in common
    if not (user_keywords & faq_keywords):
        return 0

    overlap = len(user_keywords & faq_keywords) / len(
        user_keywords | faq_keywords
    )

    sequence_score = SequenceMatcher(
        None, user_text, faq_text
    ).ratio()

    return max(overlap, sequence_score * 0.7)


class FAQChatbot:
    def __init__(self, faqs):
        self.faqs = faqs

    def get_answer(self, message):
        text = clean_text(message)

        if not text:
            return "Please type a message so I can help you."

        # Friendly conversation
        if text in ["hi", "hello", "hey", "good morning",
                    "good afternoon", "good evening"]:
            return "Hello! 😊 Welcome! It's great to meet you. How can I help you today?"

        if text in ["thanks", "thank you", "thank you so much"]:
            return "You're very welcome! 😊 I'm happy to help."

        if text in ["bye", "goodbye", "see you", "exit", "quit"]:
            return "Goodbye! 👋 Have a wonderful day!"

        if text in ["how are you", "how are you doing"]:
            return "I'm doing great, thank you for asking! 😊 What can I help you with?"

        # Match the message with the FAQ dataset
       
        # Match the message with the FAQ dataset
        best_faq = None
        best_score = 0

        user_text = clean_text(message)

        for faq in self.faqs:
            possible_questions = [faq["question"]]
            possible_questions.extend(faq.get("variations", []))

            for question in possible_questions:
                faq_text = clean_text(question)

                # Give priority to exact matches
                if user_text == faq_text:
                    return faq["answer"]

                score = similarity(message, question)

                if score > best_score:
                    best_score = score
                    best_faq = faq

        if best_faq and best_score >= 0.50:
            return best_faq["answer"]


        return (
            "I'm sorry, I don't have a reliable answer to that yet. 😊 "
            "Try asking me about courses, admissions, scholarships, "
            "fees, examinations, results, or college facilities."
        )

def main():
    faqs = load_faqs()
    chatbot = FAQChatbot(faqs)

    print("=" * 45)
    print("       COLLEGE FAQ CHATBOT")
    print("=" * 45)
    print("Bot: Hello! 😊 Welcome! How can I help you today?")
    print("Type 'exit' to close the chatbot.")

    while True:
        message = input("\nYou: ").strip()
        answer = chatbot.get_answer(message)
        print("Bot:", answer)

        if clean_text(message) in ["exit", "quit", "bye", "goodbye"]:
            break

if __name__ == "__main__":
    main()