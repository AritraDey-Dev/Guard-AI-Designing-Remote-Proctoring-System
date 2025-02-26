import speech_recognition as sr

def keyword_detection(audio_file, keywords):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f"Recognized Text: {text}")
        for keyword in keywords:
            if keyword in text.lower():
                print(f"Keyword Detected: {keyword}")
                return True
    except sr.UnknownValueError:
        print("Speech could not be understood.")
    except sr.RequestError:
        print("API unavailable.")
    return False

def process_audio_chunk(audio_chunk, keywords):
    recognizer = sr.Recognizer()
    audio = sr.AudioData(audio_chunk, sample_rate=44100, sample_width=2)
    try:
        text = recognizer.recognize_google(audio)
        print(f"Recognized Text: {text}")
        for keyword in keywords:
            if keyword in text.lower():
                print(f"Keyword Detected: {keyword}")
                return True
    except sr.UnknownValueError:
        print("Speech could not be understood.")
    except sr.RequestError:
        print("API unavailable.")
    return False
