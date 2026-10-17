
const form = document.getElementById("chat-form");
const input = document.getElementById("message-input");
const messages = document.getElementById("chat-messages");
const sendButton = document.getElementById("send-button");

function addMessage(text, className) {
    const message = document.createElement("div");
    message.classList.add("message", className);

    // textContent prevents user messages from being treated as HTML.
    message.textContent = text;

    messages.appendChild(message);
    messages.scrollTop = messages.scrollHeight;
}

form.addEventListener("submit", async function (event) {
    event.preventDefault();

    const message = input.value.trim();

    if (!message) return;

    addMessage(message, "user-message");
    input.value = "";
    sendButton.disabled = true;

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: message })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Something went wrong.");
        }

        addMessage(data.reply, "bot-message");

    } catch (error) {
        addMessage(
            "Could not get a response. Please try again.",
            "bot-message"
        );
        console.error(error);
    } finally {
        sendButton.disabled = false;
        input.focus();
    }
});
