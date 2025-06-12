import tkinter as tk
from bot_logic import load_responses, get_response
import pyttsx3

responses = load_responses()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def respond():
    user_input = entry.get()
    chat_log.insert(tk.END, "Habib: " + user_input + "\n")
    bot_reply = get_response(user_input, responses)
    chat_log.insert(tk.END, "Bot: " + bot_reply + "\n\n")
    speak(bot_reply)
    entry.delete(0, tk.END)
