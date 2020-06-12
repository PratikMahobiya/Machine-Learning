import speech_recognition as sr
from gtts import gTTS
import tkinter as tk
import _thread
import time


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.index()

    def index(self):
        self.QUIT = tk.Button(self, text="QUIT",command=self.win_quit,font=("Arial Bold", 15, "bold"), width="10", relief="groove")
        self.Test = tk.Button(self, text="Test",command=self.createWidgets,font=("Arial Bold", 15, "bold"), width="10", relief="groove")
        
        self.QUIT.pack()
        self.Test.pack()

    def createWidgets(self):
        self.select_o  = tk.Label(self,text ="Select Your Language:- \n '1' for ENGLISH\n '2' for Hindi\n")
        self.btn_1 = tk.Button(self, text = "ENGLISH",command=self.eng)
        self.btn_2 = tk.Button(self, text = "Hindi",command=self.hin)
        self.text_b = tk.Text(self)

        self.select_o.pack()
        self.btn_1.pack()
        self.btn_2.pack()
        self.text_b.pack()

#--------------------------------Language Functions----------------------------------
    def eng(self):
        s_lang = "en"
        label_1 = tk.Label(self,text = "Say Something:---")
        label_1.pack()
        main_fun(self.text_b,s_lang)
        self.onUpdate(s_lang)

    def hin(self):
        s_lang = "hi-IN"
        label_1 = tk.Label(self,text = "Say Something:---")
        label_1.pack()
        main_fun(self.text_b,s_lang)
        self.onUpdate(s_lang)

#-------------------------------frameUpdate Funtion----------------------------------
    def onUpdate(self,s_lang):
        if s_lang == "en":
            self.after(100, self.eng)
        else:
            self.after(100, self.hin)

#----------------------------Exit Button Funtion-------------------------------------
    def win_quit(self):
        exit()

#----------------------------Speech To Text Funtion-----------------------------------
def main_fun(text_b,s_lang):
    mystr = " "
    print('Say Something:- ---------------')
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.adjust_for_ambient_noise(source,duration=2)-------------------------------
        audio = r.listen(source)
        try:
            mystr = mystr + str(r.recognize_google(audio, language= s_lang))
            text_b.insert("insert",mystr)
            print(mystr)
        except:
            pass

#--------------------------Main Function---------------------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    root.title("speech to text:---")
    root.geometry("500x500+200+200")
    app = Application(master=root)
    root.mainloop()