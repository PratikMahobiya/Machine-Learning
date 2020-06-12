import speech_recognition as sr
from gtts import gTTS

r = sr.Recognizer()
with sr.Microphone() as source:
    print('Speak Anything:- ---------------')
    # r.adjust_for_ambient_noise(source,duration=2)
    audio = r.listen(source)
    try:
        txt = r.recognize_google(audio)
        print('You Said: {}'.format(txt))
        if txt is not None:
            self.text.set("Now Listen Your Words:----")
            output = gTTS(text=txt, lang= "hi-IN", slow=False)
            output.save("output.mp3")
            os.system("start output.mp3")
            print('Now Listen Your Words:----')
    except:
        print("Sorry, could not recognize your voice")
    