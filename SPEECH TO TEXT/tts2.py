import speech_recognition as sr
from gtts import gTTS
import tkinter as tk
from threading import Thread
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
        self.btn_1 = tk.Button(self, text = "ENGLISH",command=self.thr)
        self.btn_2 = tk.Button(self, text = "Hindi",command=self.thr)
        self.text_b = tk.Text(self)

        self.select_o.pack()
        self.btn_1.pack()
        self.btn_2.pack()
        self.text_b.pack()


    def show(self):
        while True:
            self.text_b.insert("insert", "test ")
            time.sleep(2)

        # mystr = " "
        # print('Say Something:- ---------------')
        # r = sr.Recognizer()
        # while True:
        #     with sr.Microphone() as source:
        #         # r.adjust_for_ambient_noise(source,duration=2)-------------------------------
        #         audio = r.listen(source)
        #         time.sleep(3)
        #         try:
        #             mystr = mystr + str(r.recognize_google(audio, language= s_lang))
        #             self.text_b.insert("insert",mystr)
        #             print(mystr)
        #         except:
        #             pass
    
    def inp(self):
       while True:
           pass 

    #----------------------------Exit Button Funtion-------------------------------------
    def win_quit(self):
        exit()


    def thr(self):
        t1 = Thread(target = self.inp)
        t2 = Thread(target = self.show)
        t1.start()
        t2.start()
        self.after(5000,self.inp)



#--------------------------Main Function---------------------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    root.title("speech to text:---")
    root.geometry("500x500+200+200")
    app = Application(master=root)
    root.mainloop()