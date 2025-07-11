def analyze_symptom(symptom):
    # Very basic symptom-response logic (you can expand this later)
    if "fever" in symptom.lower():
        return "You might have an infection. Please take rest and stay hydrated."
    elif "cough" in symptom.lower():
        return "It may be a mild cold. If it persists, consider consulting a doctor."
    else:
        return "Please consult a healthcare professional for accurate diagnosis."
