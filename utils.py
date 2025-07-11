from gtts import gTTS
from deep_translator import GoogleTranslator
import os

# Translation using Deep Translator
def translate_text(text, src="ta", dest="en"):
    return GoogleTranslator(source=src, target=dest).translate(text)

# Convert text to speech and play it
def speak_text(text, lang="ta"):
    tts = gTTS(text=text, lang=lang)
    tts.save("reply.mp3")
    os.system("start reply.mp3")  # On Windows
