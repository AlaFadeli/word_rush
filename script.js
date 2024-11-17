document.getElementById('start-test-btn').addEventListener('click', startTest);

let startTime;
let selectedText;

function startTest() {
    console.log("Start Test clicked");

    // Hide the "Start Test" button after the test begins
    document.getElementById('start-test-btn').style.display = 'none';
    
    // Show the typing container (user will start typing here)
    document.getElementById('typing-container').classList.remove('hidden');
    
    // Fetch random text for the user to type
    fetchRandomText();
    
    // Record the start time of the test
    startTime = new Date().getTime();
}

function fetchRandomText() {
    const randomTexts = [
        "The wind whispered through the trees as the sun began to set, casting a golden hue across the landscape. Birds chirped, and the air was cool and crisp, a reminder of the changing seasons.",
        "The ocean waves crashed against the shore, while the salty breeze swept across the sand. The sky stretched out into the horizon, where the blue of the sea met the sky in perfect harmony.",
        "Technology is changing rapidly, with new innovations like AI and machine learning reshaping industries. We must consider how these advancements impact society and how we can use them for good.",
        "In the heart of the city, people bustled through the streets, their faces illuminated by neon lights. The sound of footsteps mixed with the hum of traffic, creating a constant rhythm of urban life.",
    ];

    // Randomly select a shorter paragraph
    selectedText = randomTexts[Math.floor(Math.random() * randomTexts.length)];
    console.log("Random text selected:", selectedText);

    // Display the selected shorter text for the user to type
    document.getElementById('selected-text').textContent = selectedText;}

document.getElementById('user-input').addEventListener('input', function () {
    const userInput = this.value.trim();  // Remove any leading/trailing spaces
    const selectedText = document.getElementById('selected-text').textContent.trim(); // Also trim the selected text

    console.log("User input:", userInput);

    // Check if the user input matches the selected text
    if (userInput === selectedText) {
        console.log("Text complete!");

        const endTime = new Date().getTime();
        const timeTaken = (endTime - startTime) / 1000; // Time in seconds
        const words = selectedText.split(' ').length;
        const wpm = (words / timeTaken) * 60; // Calculate words per minute

        // Show results
        const resultsMessage = `Test complete! You typed at ${wpm.toFixed(2)} words per minute.`;
        document.getElementById('results').textContent = resultsMessage;

        // Show the results container and hide typing input
        document.getElementById('results-container').classList.remove('hidden');
        
        // Hide typing container after the test is done
        document.getElementById('typing-container').classList.add('hidden');
        
        // Show the "Start Test" button again for a new test
        document.getElementById('start-test-btn').style.display = 'inline-block';
    }
});

