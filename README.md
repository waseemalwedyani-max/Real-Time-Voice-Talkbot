# Real-Time Voice Talkbot 🤖🎙️

## Project Overview
This project is a fully functional, local real-time Talkbot developed as part of the "Smart Methods" training program. It listens to the user's voice via a microphone, processes the text to generate an intelligent response using a Large Language Model (LLM), and replies audibly using Text-to-Speech.

---

## Files Included in this Repository
* **`Task1.py`**: The main Python script containing the Talkbot loop, API integrations, and audio processing logic.
* **`README.md`**: Project documentation and setup instructions.

---

## Libraries & Technologies Used
To build this project, the following Python libraries were installed and utilized:

1. **`openai-whisper`**: For accurate Speech-to-Text (STT) transcription.
2. **`cohere`**: To connect with Cohere's API (`command-r7b-arabic-02-2025` model) for generating contextual and smart responses (LLM).
3. **`gTTS` (Google Text-to-Speech)**: To convert the bot's text responses back into audio (TTS).
4. **`sounddevice` & `scipy`**: To handle live microphone recording and save the audio locally as a `.wav` file.
5. **`keyboard`**: To allow smooth user control (pressing 'Space' to talk and 'Esc' to exit) without interrupting the terminal.

---

## Project Steps & Development Phases
The project was developed in the following systematic steps:

1. **Environment Setup**: Configured the Anaconda environment and VS Code, ensuring all necessary dependencies were installed.
2. **Phase 1: Speech-to-Text**: Implemented Whisper to read a local audio file and transcribe the spoken words into text successfully.
3. **Phase 2: LLM Integration**: Sent the transcribed text to the Cohere API to generate a conversational and interactive response.
4. **Phase 3: Text-to-Speech**: Integrated `gTTS` to vocalize the LLM's text response and played it automatically using Windows OS commands.
5. **Final Phase: Real-Time Live Interaction**: Upgraded the script into a continuous loop, adding live microphone recording functionality and keyboard hotkeys to create a seamless, real-time Chatbot experience.

---

## How to Run the Project
<img width="1154" height="333" alt="Screenshot 2026-07-21 052026" src="https://github.com/user-attachments/assets/232a4208-ec6f-467c-bddf-45b2a9365600" />


1. Clone this repository to your local machine.
2. Ensure you have your Cohere API key. Open `Task1.py` and replace `"YOUR_API_KEY_HERE"` with your actual key.
3. Install the required libraries using the terminal:
   ```bash
   pip install openai-whisper cohere gTTS sounddevice scipy keyboard
   ```
4. Run the script:
   ```bash
   python Task1.py
   ```
5. Follow the on-screen terminal instructions: Press `Space` to record your voice for 7 seconds, wait for the AI's vocal response, or press `Esc` to quit the application.
