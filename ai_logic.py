def analyze_symptom(text):
    text = text.lower()
    if "fever" in text:
        return "You may have a viral fever. Please rest and stay hydrated."
    elif "cough" in text:
        return "You might have a cold. Avoid cold drinks and get rest."
    elif "headache" in text:
        return "Try to rest. If it persists, consult a doctor."
    elif "vomit" in text or "nausea" in text:
        return "It could be food-related. Stay hydrated and eat light."
    else:
        return "Please describe your symptoms more clearly."
