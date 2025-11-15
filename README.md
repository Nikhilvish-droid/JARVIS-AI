# Jarvis AI – Python Virtual Assistant

Jarvis AI is a simple voice-based virtual assistant built using Python. It can perform tasks such as speech recognition, text-to-speech responses, opening apps, searching the web, telling the time/date, sending emails, and more.
This project is beginner-friendly and easily expandable.

## 📌 Features:

🎤 Speech Recognition (using speech_recognition)

🔊 Text-to-Speech using pyttsx3

🌐 Web Search (Google / Wikipedia)

⏰ Tells Time & Date

📁 Opens Apps & Websites

📧 Send Emails (optional)

🖥️ System Commands (shutdown, lock, battery info)

📚 Modular Code Structure for adding new skills

## Required Python Libraries

speechrecognition

pyttsx3

pyaudio

wikipedia

pywhatkit

pyjokes

## ▶️ Run Jarvis AI

### Start the program with: python main.py


### Jarvis will start listening and respond to commands like:

"Hey Jarvis, open YouTube"

"What is the time?"

"Search Wikipedia for Python"

"Tell me a joke"

## 🧠 How It Works
### Speech Recognition

Uses speech_recognition to convert microphone input to text.

### Text-to-Speech

pyttsx3 provides offline voice output.

### Command Processing

A simple command-matching system identifies keywords and triggers actions.

"Play a song on YouTube"

