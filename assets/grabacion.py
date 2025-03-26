import sounddevice as sd
import numpy as np

fs = 44100  # Frecuencia de muestreo
duracion = 5  # Duración de la grabación en segundos

print("Grabando...")
grabacion = sd.rec(int(duracion * fs), samplerate=fs, channels=1)
sd.wait()
print("Grabación finalizada.")

import scipy.io.wavfile as wavfile
wavfile.write("grabacion.wav", fs, grabacion)
print("Grabación guardada en grabacion.wav")
