from tkinter import*
import speech_recognition as sr
root=Tk()
root.geometry("500x500")
root.config(bg="lightblue")

def radio():
    speech_recognition = sr.Recognizer()
    with sr.Microphone() as source:
        var1=speech_recognition.listen(source) 
        voice_data=''
        try:
            voice_data=speech_recognition.recognize_google(var1,language='es-mx')
        except sr.UnknownValueError:
            print("No entendi")
    print(voice_data)
        
button_1=Button(root,text="dame click",command=radio)
button_1.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()