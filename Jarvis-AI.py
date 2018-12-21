from gtts import gTTs
import speech_recognition as sr
import os
import webbrowser
import smtplib

#speaks audio passed as argument
def talkTome(audio):
    print(audio)
    tts = gTTs(text=audio, lang='en')
    tts.save('audio.mp3')
    os.system('mpg123 audio.mp3')

#ffplay

#listens for commands
def myCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('I am ready for your next command!')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)

        try:
            command = r.recognize_google(audio)
            print('You said:' + command + '\n')

        #loop back to continue to listen for commands if unrecognizable speech is received
        except sr.UnknownValueError:
            assistant(myCommand())

        return comamnd

#if statements for executing commands
def assistant(command):

    if'open Reddit python' in command:
        chrome_path = "/usr/bin/google-chrome"
        url = 'https://www.reddit.com/r/python/'
        webbrowser.get(chrome_path).open(url)

    if 'what are you doing Jarvis' in command:
        talkTome('I am just assisting you sir')

    if 'email' in command:
        talkTome('who is the recipient sir?')
        recipient = myCommand()

        if 'John' in recipient:
            talkTome('what should i say sir?')
            content = myCommand()

            #init gmail SMTP
            mail = smtplib.SMTP('smtp.gmail.com', 587)

            #identify to server
            mail.ehlo()

            #encrypt session
            mail.starttls()

            #login
            mail.login('username', 'password')

            #send message
            mail.sendmail('PERSON NAME', 'emailaddress@anymail.com', content)

            #close connection
            mail.close()

            talkTome('Email sent')

talkTome('I am ready for your command sir')

while True:
    assistant(myCommand())