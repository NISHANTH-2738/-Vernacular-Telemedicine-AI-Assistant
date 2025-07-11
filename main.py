import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import os
from utils import translate_text, speak_text
from ai_logic import analyze_symptom

st.set_page_config(page_title="Tamil Telemedicine AI Assistant", layout="centered")

st.title("🩺 தமிழ் தொலை மருத்துவ எய்ஐ உதவியாளர்")
st.markdown("குரலின் மூலம் உங்கள் அறிகுறிகளை அளிக்கவும். உதவியை தமிழில் வழங்கப்படும்.")

if st.button("🎤 Start Voice Input"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        with st.spinner("குரலை பதிவு செய்கின்றோம்..."):
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
    try:
        tamil_text = recognizer.recognize_google(audio, language="ta-IN")
        st.success(f"🔊 நீங்கள் கூறியது: {tamil_text}")

        english = translate_text(tamil_text, src="ta", dest="en")
        st.write(f"🌐 English Translation: {english}")

        response_en = analyze_symptom(english)
        response_ta = translate_text(response_en, src="en", dest="ta")
        st.write(f"🤖 பதில் (தமிழில்): {response_ta}")

        speak_text(response_ta, lang="ta")
    except Exception as e:
        st.error("மன்னிக்கவும், உங்கள் குரலை புரியவில்லை.")
