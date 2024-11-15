
import random
import time 




random_texts = [
    "The sun dipped below the horizon, casting long shadows across the meadow. Birds fluttered by, their wings slicing through the cool evening air. The grass whispered with the soft breeze, while the last of the day's light began to fade. In the distance, the faint sound of a babbling brook echoed through the trees, a peaceful lullaby of nature. As the sky darkened, the stars began to make their appearance, like tiny pinpricks of light scattered across a vast canvas. The quiet of the evening was broken only by the occasional rustle of leaves or the distant hoot of an owl. The world seemed to slow down, as though it, too, were preparing to rest. The air became crisp, carrying with it the earthy scent of damp soil and pine. Every inch of the landscape felt alive yet somehow serene—an invitation to pause and reflect on the beauty of the world. With each passing moment, the fading light transformed into the depth of night, a reminder of the endless cycles of nature",


    "As the first cool breezes of evening began to sweep across the meadow, the colors of the setting sun melted into hues of purple and orange, casting a soft glow on the surrounding landscape. The rustling trees stood as silent sentinels, their branches swaying gently as if to offer a quiet greeting to the oncoming night. Farther in the distance, the mountain peaks appeared to catch the last rays of sunlight, their snow-covered surfaces glowing faintly. It was a moment where time seemed suspended, a brief but profound pause in the rhythm of the world. The peace that settled over the meadow was palpable, as if the very earth itself was breathing a sigh of relief after a long day. It was a simple yet profound reminder of the beauty found in moments of stillness",
    
    
    
    "Technology continues to evolve at an astounding rate, bringing innovations that were once the stuff of science fiction into everyday life. From artificial intelligence to quantum computing, the possibilities seem endless. Yet, as we race forward, it’s important to consider the ethical implications of these advancements and how they shape the future of humanity. While technology has the power to revolutionize industries, enhance productivity, and make life more convenient, it also brings with it a host of challenges. How do we ensure that these innovations are used responsibly? How can we balance progress with the preservation of privacy, security, and human dignity? The more technology advances, the more complex the questions become. Automation, for example, has the potential to create a more efficient world, but it also raises concerns about job displacement and economic inequality.",

    "The mountains rose in the distance, their jagged peaks piercing the sky like ancient guardians. A layer of mist clung to their slopes, creating an air of mystery and wonder. The path ahead was narrow and winding, but the promise of breathtaking views kept the adventurer moving forward, one step at a time. Each twist and turn of the trail revealed something new: the sight of a hidden waterfall, the delicate fragrance of wildflowers, and the sound of birds singing above the canopy. The higher you climbed, the clearer the air became, and the world below seemed to shrink, as if the problems of the everyday were being left behind with each passing step",
]
    



def ts_calculator(start, end, text_length):
    
    typing_time = end - start 
    words = text_length / 5  # Explanation : Accoring to google, average word length is 5 characters 
    wpm = (words / typing_time ) * 60 # WPM PER MINUTE

    return wpm 



def accuracy_calculator(user_input, random_texts):

    correct_inputs = 0 
    for i in range(min(len(user_input), len(random_texts))):
        if input[i] == original_text[i] : 
            correct_inputs += 1 
    accuracy = (correct_inputs / len(random_texts)) * 100 

    return accuracy

def typing_test():

    selected_text = random.choice(random_texts)
    
    
    print("Welcome to WordRush,TEST YOUR TYPING SPEED !!!")
    print ("------------------")    
    print("We chose a random text for you to type, DONT FORGET NEVER TEST YOURSELF ONCE !!! ")
    print(selected_text)
    print("\nStart typing...")



    # Cronometer:
    input("PRESS ANY KEY TO START...")
    start = time.time()

    # Type
    user_input = input("\nStart typing here:")

    # end time : 
    end = time.time()




    # CALCULATE AND DISPLAY WPM AND ACCURACY : 

    wpm = ts_calculator(start, end,len(user_input))

    accuracy = accuracy_calculator(user_input, random_texts)


    print(f"\nYour typing speed is: {wpm:.2f} words per minute.")
    print(f"Time taken: {end - start:.2f} seconds.")
    print(f"Accuracy: {accuracy:.2f}%")


if __name__ == "__main__":
    typing_test()



