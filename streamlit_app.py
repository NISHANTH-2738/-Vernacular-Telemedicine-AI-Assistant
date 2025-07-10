import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import os
from utils import translate_text, speak_text
from ai_logic import analyze_symptom

st.set_page_config(page_title="Tamil Telemedicine AI Assistant", layout="centered")
st.title("🩺 தமிழ் டெலிமெடிசின் எய்ஐ உதவியாளர்")
st.markdown("சிம்ப்டம்களை தமிழில் பேசவும், உதவியாளர் பதில் அளிக்கும்.")

if st.button("🎙️ பேச தொடங்கு"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        with st.spinner("கேட்கின்றேன்..."):
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
    try:
        tamil_text = recognizer.recognize_google(audio, language="ta-IN")
        st.success(f"📥 நீங்கள் சொன்னது: {tamil_text}")

        english = translate_text(tamil_text, src="ta", dest="en")
        st.write(f"🌐 English translation: {english}")

        response_en = analyze_symptom(english)
        response_ta = translate_text(response_en, src="en", dest="ta")
        st.write(f"🤖 பதில்: {response_ta}")

        speak_text(response_ta, lang="ta")
    except Exception as e:
        st.error("⚠️ ஆடியோ புரியவில்லை.")
