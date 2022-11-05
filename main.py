# Our main file.

import speech_recognition as sr

# Cria um reconhedor de voz
r = sr.Recognizer()

# Abre o microfone para captura de som.
with sr.Microphone() as source:
     audio = r.listen(source) # Definme o microfone como ponte de aúdio.

     print(r.recognize_google(audio))