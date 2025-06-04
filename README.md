Jarvis Voice Assistant
Jarvis is a Python-based voice-controlled virtual assistant that responds to voice commands, interacts conversationally using OpenAI's GPT-3.5-turbo model, and performs practical tasks like opening websites, fetching news headlines, and launching applications on your computer.

Description
This voice assistant listens for the wake word "Jarvis" and then processes your spoken commands using speech recognition. It integrates OpenAI’s GPT model to generate intelligent and contextual responses, making interactions natural and dynamic. It can:

Open popular websites like Google, Facebook, YouTube, LinkedIn

Fetch and read aloud the latest top headlines from India

Launch desktop applications configured for your system

Chat conversationally on any other topic using GPT-3.5-turbo

Shut down gracefully on voice command

The assistant uses text-to-speech to speak responses aloud, creating a hands-free experience.

Features
Wake word detection with real-time microphone listening

Speech recognition with Google Speech API

Text-to-speech using gTTS and pyttsx3 engines with audio playback via pygame

AI-powered chat responses using OpenAI GPT-3.5-turbo

News headlines fetching from NewsAPI

Desktop app launching with system compatibility

Easy extensibility for adding more commands

Technologies Used
Python

SpeechRecognition (speech_recognition)

OpenAI API (openai)

Google Text-to-Speech (gTTS)

Pygame (audio playback)

pyttsx3 (text-to-speech engine)

NewsAPI

dotenv (environment variable management)

Webbrowser and subprocess modules

Setup and Installation
Clone the repository.

Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Create a .env file in the root directory with your API keys:

ini
Copy
Edit
YOUR_API_KEY=your_openai_api_key_here
NEWS_API_KEY=your_newsapi_key_here
Modify APP_PATHS dictionary in the script to match application paths on your computer.

Run the script:

bash
Copy
Edit
python jarvis_assistant.py
Usage
Say "Jarvis" to wake the assistant.

Speak your command clearly after the prompt.

The assistant will respond vocally and perform actions like opening websites, reading news, or chatting.

To exit, say "stop" or "exit".

Example Commands
"Open Google"

"Open YouTube"

"What’s the latest news?"

"Open Visual Studio Code"

"Tell me a joke"

"Stop"

Notes
Ensure your microphone is configured and working correctly.

Requires internet connection for speech recognition, news fetching, and AI responses.

Adjust application paths in the script to suit your OS and installed programs.
