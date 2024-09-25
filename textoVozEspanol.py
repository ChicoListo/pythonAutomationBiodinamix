from pygame import mixer
from gtts import gTTS

def main():
    texto = 'Hola, judith.'
    tts = gTTS(texto, lang='es')
    tts.save('salida.mp3')
    
    mixer.init()
    mixer.music.load('salida.mp3')
    mixer.music.play()

if __name__ == "__main__":
    main()
