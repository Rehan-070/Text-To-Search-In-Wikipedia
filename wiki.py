import pyttsx3
import wikipedia
from wikipedia.exceptions import PageError

voice = pyttsx3.init()

Inp = input("Enter text to search in Wikipedia: ")

try:
    result = wikipedia.summary(Inp, sentences=3)
    print(result)
    voice.say(result)
except PageError:
    print(f"Page '{Inp}' not found. Please try another search term.")
    voice.say(f"Page '{Inp}' not found.")
except wikipedia.DisambiguationError as e:
    print(f"Multiple possible matches for '{Inp}': {e.options}")
    voice.say(f"Multiple possible matches for '{Inp}'.")
except Exception as e:
    print(f"An error occurred: {e}")
    voice.say("An error occurred.")
    
voice.runAndWait()
