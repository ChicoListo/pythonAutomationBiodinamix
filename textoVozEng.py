from pygame import mixer
from gtts import gTTS

def main():
   tts = gTTS('This is a test, and we want to know how meny text can be converted in voice, and we want to know if the spanish can be converted too in the same text, se que podremos.')
   tts.save('output.mp3')
   mixer.init()
   mixer.music.load('output.mp3')
   mixer.music.play()
   
if __name__ == "__main__":
   main()