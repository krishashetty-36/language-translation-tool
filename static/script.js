
const chatForm = document.getElementById("chat-form");
const messageInput = document.getElementById("message-input");
const chatMessages = document.getElementById("chat-messages");
const sendButton = document.getElementById("send-button");

function addMessage(text, sender) {
    const message = document.createElement("div");
    message.classList.add("message", `${sender}-message`);
    message.textContent = text;

    chatMessages.appendChild(message);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

chatForm.addEventListener("submit", async function (event) {
    event.preventDefault();

    const message = messageInput.value.trim();

    if (!message) {
        return;
    }

    addMessage(message, "user");
    messageInput.value = "";
    messageInput.focus();
    sendButton.disabled = true;
    sendButton.textContent = "Sending...";

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: message })
        });

        if (!response.ok) {
            throw new Error("Server error");
        }

        const data = await response.json();
        addMessage(data.answer, "bot");
    } catch (error) {
        addMessage(
            "Sorry, I couldn't connect to the chatbot. Please try again.",
            "bot"
        );
    } finally {
        sendButton.disabled = false;
        sendButton.textContent = "Send ➤";
        messageInput.focus();
    }
});
