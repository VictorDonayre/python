import speech_recognition as sr
import pyttsx3

# Inicializar reconocimiento de voz y síntesis de voz
reconocedor = sr.Recognizer()
sintetizador = pyttsx3.init()

# Configurar la voz (opcional)
voices = sintetizador.getProperty('voices')
sintetizador.setProperty('voice', voices[0].id)  # 0 para voz masculina, 1 para femenina

def hablar(texto):
    sintetizador.say(texto)
    sintetizador.runAndWait()

def escuchar():
    with sr.Microphone() as fuente:
        print("Escuchando...")
        audio = reconocedor.listen(fuente)
        try:
            comando = reconocedor.recognize_google(audio, language='es-ES')  # Configura el idioma a español
            print(f"Tú dijiste: {comando}")
            return comando.lower()
        except sr.UnknownValueError:
            print("No pude entender el audio")
            return ""
        except sr.RequestError:
            print("No se pudo obtener resultados del servicio de Google")
            return ""

def ejecutar_comando(comando):
    if 'hola' in comando:
        hablar("Hola, ¿cómo puedo ayudarte?")
    elif 'cómo estás' in comando:
        hablar("Estoy bien, gracias por preguntar.")
    elif 'adiós' in comando:
        hablar("Adiós, que tengas un buen día.")
        return False  # Detiene el asistente
    else:
        hablar("No entendí ese comando.")
    return True

# Bucle principal del asistente
activo = True
while activo:
    comando = escuchar()
    if comando:
        activo = ejecutar_comando(comando)