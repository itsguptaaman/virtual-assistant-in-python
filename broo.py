import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib



class Bro:

    def __init__(self):
        self.engine = pyttsx3.init('sapi5')

    def create_voice(self):
        '''
        Docstring:
        This function will initilize the voice in program
        :return:None
        '''
        voices = self.engine.getProperty('voices')
        # print(voices[0].id)
        self.engine.setProperty('voice', voices[0].id)

    def speak(self, audio):
        '''
        Docstring:
        This function will take a string as a input and returns the speech of it
        :param audio: String eg " This is a string"
        :return: speech of text
        '''
        self.engine.say(audio)
        self.engine.runAndWait()

    def wish_me(self):
        try:
            hour = int(datetime.datetime.now().hour)
            if 0 <= hour < 12:
                self.speak("Good Morning!")
            elif 12 <= hour < 18:
                self.speak("Good Afternoon!")
            else:
                self.speak("Good Evening")
            self.speak("I am your Bro. Please tell me how may i help you")
        except Exception as e:
            print(e)

    def take_commands(self):
        '''
        Docstring:
        This function will hear your voice from your devices microphone and requrn the query of it.
        :return: query
        '''
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognising...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User Said {query}")

        except Exception as e:
            print(e)
            print("Can you say that again please ...")
            return "None"
        return query

    def send_email(self, to, content):
        '''
        Docstring:
        This function will send an email
        :param to: email og the person
        :param content: the message of the email
        '''
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login("youremail@gmail.com", "your-password")
            server.sendmail("youremail@gmail.com", to, content)
            server.close()

        except Exception as e:
            print(e)


def main():
    '''
    Docstring:
    This is the main function of the program
    '''
    obj1 = Bro()
    obj1.create_voice()
    obj1.speak("Hey Bro, How are you!")
    obj1.wish_me()
    while True:
        query = obj1.take_commands().lower()

        if 'wikipedia' in query:
            obj1.speak("Searching Wikipedia ...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            obj1.speak("According to Wikipedia")
            print(results)
            obj1.speak(results)

        elif "open youtube" in query:
            webbrowser.open("m.youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open linkedin" in query:
            webbrowser.open("https://www.linkedin.com/")

        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "open whatsapp" in query:
            webbrowser.open("https://web.whatsapp.com/")

        elif "the time" in query:
            time_str = datetime.datetime.now().strftime("%H:%M:%S")
            obj1.speak(f"The time is {time_str}")

        elif "open pyCharm" in query:
            code_path = r"C:\Program Files\JetBrains\PyCharm Community Edition 2022.1.4\bin\pycharm64.exe"
            os.startfile(code_path)
        elif "open vs code" in query:
            code_path = r"C:\Users\Aman\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(code_path)

        elif "send email to Aman" in query:
            try:
                obj1.speak("What should I say ")
                content = obj1.take_commands()
                to = "itsamangupta365@gmail.com"
                obj1.send_email(to, content)
                obj1.speak("Email has been send")
            except Exception as e:
                print(e)
                obj1.speak("Sorry, I can't do this task at the moment")


if __name__ == '__main__':
    main()
