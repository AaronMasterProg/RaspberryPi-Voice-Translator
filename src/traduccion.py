import speech_recognition as sr
from googletrans import Translator
import pyttsx3

def traduction():
    reconocedor = sr.Recognizer()
    translator = Translator()
    engine = pyttsx3.init()

    with sr.Microphone() as fuente:
        print("Habla en español...")
        audio = reconocedor.listen(fuente)

    try:
        texto_espanol = reconocedor.recognize_google(audio, language="es-ES")
        print(f"Texto en español: {texto_espanol}")

        texto_ingles = translator.translate(texto_espanol, dest="en").text
        print(f"Texto en inglés: {texto_ingles}")

        engine.say(texto_ingles)
        engine.runAndWait()

    except sr.UnknownValueError:
        print("No se pudo entender el audio")
    except sr.RequestError as e:
        print(f"Error en la solicitud: {e}")
