// Get elements from the HTML page
const inputText = document.getElementById("inputText");
const outputText = document.getElementById("outputText");

const sourceLanguage = document.getElementById("sourceLanguage");
const targetLanguage = document.getElementById("targetLanguage");

const translateButton = document.getElementById("translateButton");
const copyButton = document.getElementById("copyButton");
const speakButton = document.getElementById("speakButton");
const swapButton = document.getElementById("swapButton");
const characterCount = document.getElementById("characterCount");


// Translate button
translateButton.addEventListener("click", async function () {

    const text = inputText.value.trim();

    const source = sourceLanguage.value;
    const target = targetLanguage.value;

    // Check if text is empty
    if (text === "") {
        alert("Please enter some text.");
        return;
    }

    // Check if same language is selected
    if (source === target) {
        outputText.value = text;
        return;
    }

    // Show loading message
    outputText.value = "Translating...";
    translateButton.disabled = true;
translateButton.textContent = "Translating...";

    try {

        // Create API URL
        const url =
            `https://api.mymemory.translated.net/get?q=${encodeURIComponent(text)}&langpair=${source}|${target}`;

        // Send request to translation API
        const response = await fetch(url);

        // Convert API response into JavaScript data
        const data = await response.json();

        // Display translated text
        outputText.value = data.responseData.translatedText;
        translateButton.disabled = false;
translateButton.textContent = "Translate";

    } catch (error) {

        console.error(error);
    
        outputText.value = "❌ Translation failed. Please check your internet connection and try again.";
        translateButton.disabled = false;
        translateButton.textContent = "Translate";
    }
});


// Copy button
copyButton.addEventListener("click", function () {

    const text = outputText.value;

    if (text.trim() === "") {
        alert("There is no translation to copy.");
        return;
    }

    navigator.clipboard.writeText(text);

    alert("Translation copied!");
});
// Text-to-speech button
speakButton.addEventListener("click", function () {

    const text = outputText.value;

    if (text.trim() === "") {
        alert("There is no translation to listen to.");
        return;
    }

    const speech = new SpeechSynthesisUtterance(text);

    speech.lang = targetLanguage.value;

    window.speechSynthesis.speak(speech);
});
// Swap source and target languages
swapButton.addEventListener("click", function () {

    const currentSource = sourceLanguage.value;
    sourceLanguage.value = targetLanguage.value;
    targetLanguage.value = currentSource;

    const currentInput = inputText.value;
    inputText.value = outputText.value;
    outputText.value = currentInput;
});


// Character counter
inputText.addEventListener("input", function () {

    const count = inputText.value.length;

    characterCount.textContent = `${count} / 500 characters`;
});