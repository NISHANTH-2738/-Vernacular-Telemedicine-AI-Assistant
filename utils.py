from gtts import gTTS
from googletrans import Translator
import os

translator = Translator()

def translate_text(text, src="ta", dest="en"):
    result = translator.translate(text, src=src, dest=dest)
    return result.text

def speak_text(text, lang="ta"):
    tts = gTTS(text=text, lang=lang)
    tts.save("reply.mp3")
    os.system("start reply.mp3")
