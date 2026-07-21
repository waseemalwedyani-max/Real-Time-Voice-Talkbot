import whisper
import cohere
from gtts import gTTS
import os
import sounddevice as sd
from scipy.io.wavfile import write
import time
import keyboard  # المكتبة الجديدة لالتقاط الأزرار

print("Loading AI Models... Please wait.")

# 1. إعداد Cohere و Whisper
co = cohere.Client("YOUR_API_KEY_HERE")  # لا تنسَ وضع مفتاحك
whisper_model = whisper.load_model("base")

freq = 44100
duration = 7

print("\n" + "="*50)
print("The Live Talkbot is ready!")
print("="*50)

while True:
    print("\nPress 'Space' to start recording for 7 seconds, or press 'Esc' to quit...")
    
    # ------------------------------------------
    # حلقة انتظار ذكية لزر المسافة أو الخروج
    # ------------------------------------------
    action = None
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == 'esc':
                action = 'quit'
                break
            elif event.name == 'space':
                action = 'record'
                break
                
    if action == 'quit':
        print("Ending the conversation. Goodbye!")
        break # خروج من البرنامج بالكامل

    # تأخير زمني بسيط (ربع ثانية) حتى لا يسجل صوت ضغطة الكيبورد
    time.sleep(0.25)

    # ==========================================
    # 1. التسجيل
    # ==========================================
    print("🔴 Recording... Speak now!")
    recording = sd.rec(int(duration * freq), samplerate=freq, channels=1)
    sd.wait()
    print("🟢 Recording finished.")

    live_audio_file = "live_record.wav"
    write(live_audio_file, freq, recording)

    # ==========================================
    # 2. الاستماع
    # ==========================================
    print("1. Transcribing...")
    result = whisper_model.transcribe(live_audio_file)
    user_text = result["text"].strip()

    if not user_text:
        print("I didn't hear anything clearly. Let's try again.")
        continue

    print(f"You said: {user_text}")
    print("-" * 50)

    # ==========================================
    # 3. التفكير
    # ==========================================
    print("2. Thinking...")
    response = co.chat(
        model="command-r7b-arabic-02-2025",
        message=user_text
    )
    bot_reply = response.text

    print(f"Talkbot: {bot_reply}")
    print("-" * 50)

    # ==========================================
    # 4. التحدث
    # ==========================================
    print("3. Speaking...")
    tts = gTTS(text=bot_reply, lang='en', slow=False)
    
    audio_file = "bot_response.mp3"
    tts.save(audio_file)
    
    os.system(f"start {audio_file}")
    
    # انتظار 3 ثوانٍ أثناء تشغيل الصوت لتجنب التداخل
    time.sleep(3)