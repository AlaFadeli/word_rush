import random
import time 

# Sample random texts for typing test
random_texts = [
    "The sun dipped below the horizon, casting long shadows across the meadow. Birds fluttered by, their wings slicing through the cool evening air. The grass whispered with the soft breeze, while the last of the day's light began to fade. In the distance, the faint sound of a babbling brook echoed through the trees, a peaceful lullaby of nature. As the sky darkened, the stars began to make their appearance, like tiny pinpricks of light scattered across a vast canvas. The quiet of the evening was broken only by the occasional rustle of leaves or the distant hoot of an owl. The world seemed to slow down, as though it, too, were preparing to rest. The air became crisp, carrying with it the earthy scent of damp soil and pine. Every inch of the landscape felt alive yet somehow serene—an invitation to pause and reflect on the beauty of the world. With each passing moment, the fading light transformed into the depth of night, a reminder of the endless cycles of nature.",
    "As the first cool breezes of evening began to sweep across the meadow, the colors of the setting sun melted into hues of purple and orange, casting a soft glow on the surrounding landscape. The rustling trees stood as silent sentinels, their branches swaying gently as if to offer a quiet greeting to the oncoming night. Farther in the distance, the mountain peaks appeared to catch the last rays of sunlight, their snow-covered surfaces glowing faintly. It was a moment where time seemed suspended, a brief but profound pause in the rhythm of the world. The peace that settled over the meadow was palpable, as if the very earth itself was breathing a sigh of relief after a long day. It was a simple yet profound reminder of the beauty found in moments of stillness.",
    "Technology continues to evolve at an astounding rate, bringing innovations that were once the stuff of science fiction into everyday life. From artificial intelligence to quantum computing, the possibilities seem endless. Yet, as we race forward, it’s important to consider the ethical implications of these advancements and how they shape the future of humanity. While technology has the power to revolutionize industries, enhance productivity, and make life more convenient, it also brings with it a host of challenges. How do we ensure that these innovations are used responsibly? How can we balance progress with the preservation of privacy, security, and human dignity? The more technology advances, the more complex the questions become. Automation, for example, has the potential to create a more efficient world, but it also raises concerns about job displacement and economic inequality.",
    "The mountains rose in the distance, their jagged peaks piercing the sky like ancient guardians. A layer of mist clung to their slopes, creating an air of mystery and wonder. The path ahead was narrow and winding, but the promise of breathtaking views kept the adventurer moving forward, one step at a time. Each twist and turn of the trail revealed something new: the sight of a hidden waterfall, the delicate fragrance of wildflowers, and the sound of birds singing above the canopy. The higher you climbed, the clearer the air became, and the world below seemed to shrink, as if the problems of the everyday were being left behind with each passing step.",
]

# Function to calculate Words Per Minute (WPM)
def ts_calculator(start, end, text_length):
    typing_time = end - start  # Time in seconds
    words = text_length / 5  # Assuming average word length is 5 characters
    wpm = (words / typing_time) * 60  # Words per minute
    return wpm

# Function to calculate accuracy
def accuracy_calculator(user_input, selected_text):
    correct_inputs = 0
    # Compare character by character
    for i in range(min(len(user_input), len(selected_text))):
        if user_input[i] == selected_text[i]:  # Compare the user's input to the selected text
            correct_inputs += 1
    # Accuracy is the number of correct characters divided by the total length of the selected text
    accuracy = (correct_inputs / len(selected_text)) * 100
    return accuracy

# Function for the typing test
def typing_test():
    selected_text = random.choice(random_texts)  # Choose a random sentence
    
    print("Welcome to WordRush, TEST YOUR TYPING SPEED!!!")
    print("------------------")
    print("We chose a random text for you to type, DON'T FORGET NEVER TEST YOURSELF ONCE!!!")
    print(selected_text)
    print("\nStart typing...")
    
    # Wait for the user to press any key to start the test
    input("PRESS ANY KEY TO START...")
    start = time.time()  # Record the start time
    
    # Prompt user to start typing
    user_input = input("\nStart typing here: ")
    
    end = time.time()  # Record the end time
    
    # Calculate WPM and Accuracy
    wpm = ts_calculator(start, end, len(user_input))
    accuracy = accuracy_calculator(user_input, selected_text)
    
    # Display results
    print(f"\nYour typing speed is: {wpm:.2f} words per minute.")
    print(f"Time taken: {end - start:.2f} seconds.")
    print(f"Accuracy: {accuracy:.2f}%")

# Run the typing test if this script is executed
if __name__ == "__main__":
    typing_test()
