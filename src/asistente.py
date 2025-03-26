from traduccion import traduction
from reconocimiento import recognition
import speech_recognition as sr
import pyttsx3

def hablar(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

def escuchar():
    reconocedor = sr.Recognizer()
    with sr.Microphone() as fuente:
        print("Escuchando...")
        audio = reconocedor.listen(fuente)
    try:
        print("Reconociendo...")
        texto = reconocedor.recognize_google(audio, language="es-ES")
        print(f"Usuario: {texto}")
        return texto.lower()
    except sr.UnknownValueError:
        hablar("No entendí lo que dijiste.")
        return ""
    except sr.RequestError as e:
        hablar("No puedo conectarme al servicio de reconocimiento de voz; revisa tu conexión a internet.")
        return ""

def asistente():
    hablar("¡Hola! Soy tu asistente virtual. ¿En qué puedo ayudarte?")
    while True:
        comando = escuchar()
        if "hola" in comando:
            hablar("¡Hola! ¿Cómo estás?")
        elif "adiós" in comando:
            hablar("¡Adiós! Que tengas un buen día.")
            break
        elif "hora" in comando:
            import datetime
            hora = datetime.datetime.now().strftime("%H:%M")
            hablar(f"Son las {hora}")
        elif "quién eres" in comando:
            hablar("¡Soy tu asistente personal de inteligencia artificial!")
        elif "qué puedes hacer" in comando:
            hablar("Estoy en la etapa de desarrollo, pronto podré hacer cosas útiles.")
        elif "traducción" in comando:
            hablar("Etapa de traducción")
            traduction()
        elif "reconocimiento" in comando:
            hablar("Etapa de Reconocimiento Facial")
            recognition()
        elif comando:
            hablar("Lo siento, no pude entenderte. ¿Puedes repetirlo?.")

if __name__ == "__main__":
    asistente()
