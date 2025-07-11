import streamlit as st
import os
from utils import translate_text, speak_text
from ai_logic import analyze_symptom

st.set_page_config(page_title="Tamil Telemedicine AI Assistant", layout="centered")
st.title("🩺 தமிழ் தொலைமருத்துவ AI உதவியாளர்")

# Check if running on Streamlit Cloud
is_cloud = os.getenv("STREAMLIT_SERVER_HEADLESS") == "1"

if not is_cloud:
    import speech_recognition as sr

    st.info("மைக்ரோஃபோனில் உங்கள் அறிகுறிகளைச் சொல்லவும்...")

    if st.button("🎙️ கேட்டெடுக்க தொடங்கு"):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            st.write("📢 சத்தத்தை பொருத்தமாகத் தேர்ந்தெடுத்து கொண்டிருக்கிறது...")
            recognizer.adjust_for_ambient_noise(source)
            st.write("🛑 கேட்கப்படுகிறது... பேசுங்கள்.")
            audio = recognizer.listen(source)

        try:
            tamil_text = recognizer.recognize_google(audio, language="ta-IN")
            st.success(f"நீங்கள் கூறியது: {tamil_text}")

            english = translate_text(tamil_text, src="ta", dest="en")
            st.write(f"Translation: {english}")

            response_en = analyze_symptom(english)
            response_ta = translate_text(response_en, src="en", dest="ta")

            st.success(f"AI பதில்: {response_ta}")
            speak_text(response_ta, lang="ta")

        except Exception as e:
            st.error("தகவலை புரிந்துகொள்ள முடியவில்லை. மீண்டும் முயற்சிக்கவும்.")
else:
    st.warning("🎧 மைக்ரோஃபோன் ஆதரவு இந்த இணையதளத்தில் இல்லை. தயவுசெய்து லோகலாக இயக்கவும்.")
