import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
eng=pyttsx3.init()
eng.setProperty('rate', 150)
eng.setProperty('volume', 0.9) 
def speak(text):
    eng.say(text)
    eng.runAndWait()
def greet():
    current_hour = datetime.datetime.now().hour
    if current_hour < 12:
        speak("Good morning!")
    elif 12 <= current_hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am your voice assistant. How can I assist you today?")
def list_sp():
    recogn=sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        try:
            audio = recogn.listen(source, timeout=5, phrase_time_limit=5)
            command = recogn.recognize_google(audio).lower()
            return command
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Could you please repeat?")
            return ""
        except sr.RequestError:
            speak("There seems to be an issue with the speech recognition service.")
            return ""
        except Exception as e:
            speak(f"An error occurred: {str(e)}")
            return ""
def respond(command):
    """Perform tasks based on the command."""
    if "hello" in command:
        speak("Hello! How can I help you?")
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}.")
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        speak(f"Today's date is {current_date}.")
    elif "search" in command:
        speak("What would you like to search for?")
        query = list_sp()
        if query:
            speak(f"Searching for {query} on the web.")
            webbrowser.open(f"https://www.google.com/search?q={query}")
    elif "exit" in command or "quit" in command:
        speak("Goodbye! Have a great day.")
        return False
    else:
        speak("Sorry, I didn't understand that. Can you try again?")
    return True
def main():
    greet()
    running = True
    while running:
        command = list_sp()
        if command:
            running = respond(command)

if __name__ == "__main__":
    main()