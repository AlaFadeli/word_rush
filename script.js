document.getElementById('start-test-btn').addEventListener('click', startTest);

let startTime;
let selectedText;

function startTest() {
    // Hide the "Start Test" button
    document.getElementById('start-test-btn').style.display = 'none';
    
    // Show the typing container
    document.getElementById('typing-container').classList.remove('hidden');
    
    // Fetch the random text for the user to type
    fetchRandomText();
    
    // Record the start time of the test
    startTime = new Date().getTime();
}

function fetchRandomText() {
    const randomTexts = [
        "The wind whispered through the towering trees, as the sun began to set behind the mountains. The sky was painted in hues of pink and orange, casting a serene glow across the valley. Birds flew in the distance, and the scent of pine and earth filled the air. In the quiet, there was a sense of timelessness—a moment that stretched into eternity, where nothing mattered but the beauty of nature.",
        "As the waves crashed against the shore, the sound echoed in the vast emptiness of the beach. The sand beneath my feet was warm, yet the ocean breeze cooled my face. I could see the horizon stretching out into infinity, as though the ocean and the sky were one continuous expanse of blue. It was a moment of peace, a break from the constant noise of the world. And for a fleeting second, I felt at home.",
        "Technology is an ever-evolving landscape, constantly changing the way we live, work, and communicate. With the advent of artificial intelligence, machine learning, and quantum computing, the boundaries of what’s possible seem to expand with each passing day. Yet, with all of these advancements, we must ask ourselves: What are the ethical implications of such rapid progress? How can we ensure that technology serves humanity, rather than the other way around?",
        "The city was alive with activity, as people rushed through the streets, each lost in their own world. Neon lights flickered above, casting a colorful glow on the pavement. The sound of car engines mixed with the chatter of pedestrians, creating a chaotic symphony of urban life. Yet, in the midst of it all, there was a sense of purpose, a collective energy that propelled the city forward. It was a place where dreams were made, and hopes were realized.",
    ];
    
    // Randomly select a paragraph of text
    selectedText = randomTexts[Math.floor(Math.random() * randomTexts.length)];
    
    // Display the selected text
    document.getElementById('selected-text').textContent = selectedText;
}

// Handling user input and checking if the typing is correct
document.getElementById('user-input').addEventListener('input', function () {
    const userInput = this.value;
    const selectedText = document.getElementById('selected-text').textContent;

    // Check if the user's input matches the text and if they finished typing
    if (userInput === selectedText) {
        const endTime = new Date().getTime();
        const timeTaken = (endTime - startTime) / 1000; // Time in seconds
        const words = selectedText.split(' ').length;
        const wpm = (words / timeTaken) * 60; // Calculate words per minute

        // Show results
        document.getElementById('results').textContent = `Test complete! You typed at ${wpm.toFixed(2)} words per minute.`;
        document.getElementById('results-container').classList.remove('hidden');

        // Optionally hide the typing container after the test is done
        document.getElementById('typing-container').classList.add('hidden');
        
        // Show the start button again
        document.getElementById('start-test-btn').style.display = 'inline-block';
    }
});

function displayResults(wpm, accuracy, timeTaken) {
    document.getElementById('results').innerHTML = `WPM: ${wpm.toFixed(2)}<br>Accuracy: ${accuracy.toFixed(2)}%<br>Time: ${timeTaken.toFixed(2)} seconds`;
    document.getElementById('results-container').classList.remove('hidden');
}function calculateWPM(timeTaken, textLength) {
    constfunction calculateWPM(timeTaken, textLength) {
    const words = textLength / 5; // Assuming an average word length of 5 characters
    return (words / timeTaken) * 60; // Words per minute
}

function calculateAccuracy(userInput, selectedText) {
    let correctInputs = 0;
    for (let i = 0; i < Math.min(userInput.length, selectedText.length); i++) {
        if (userInput[i] === selectedText[i]) {
            correctInputs++;
        }
    }
    return (correctInputs / selectedText.length) * 100;
}

function displayResults(wpm, accuracy, timeTaken) {
    document.getElementById('results').innerHTML = `
        <strong>Results:</strong><br>
        <span>Words Per Minute: ${wpm.toFixed(2)} WPM</span><br>
        <span>Accuracy: ${accuracy.toFixed(2)}%</span><br>
        <span>Time Taken: ${timeTaken.toFixed(2)} seconds</span>
    `;
    document.getElementById('results-container').classList.remove('hidden');
}
