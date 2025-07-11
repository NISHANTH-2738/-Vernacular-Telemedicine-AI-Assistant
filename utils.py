from gtts import gTTS
from deep_translator import GoogleTranslator
import os

def translate_text(text, src="ta", dest="en"):
    return GoogleTranslator(source=src, target=dest).translate(text)

def speak_text(text, lang="ta"):
    tts = gTTS(text=text, lang=lang)
    tts.save("reply.mp3")
    os.system("start reply.mp3")
