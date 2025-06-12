from bot_logic import load_responses, get_response
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        user_input = recognizer.recognize_google(audio)
        print(f"You said: {user_input}")
        return user_input
    except sr.UnknownValueError:
        return "Sorry, I didn't catch that."
    except sr.RequestError:
        return "Sorry, I'm having trouble accessing the speech service."

def chat():
    print("Chatbot is running. Type 'exit' to stop.\n")
    responses = load_responses()

    while True:
        user_input = input("You (type or press Enter to speak): ")
        if user_input.strip() == "":
            user_input = listen()

        if user_input.lower() == "exit":
            print("Bot: Goodbye!")
            speak("Goodbye!")
            break

        bot_reply = get_response(user_input, responses)
        print("Bot:", bot_reply)
        speak(bot_reply)

if __name__ == "__main__":
    chat()
