import pyttsx3
import datetime
import speech_recognition as sr
from bard import getAnswer
import webbrowser
import os
import pywhatkit


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# print(voices) # prints all the available voices
print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio: str):
    print(audio)
    engine.say(audio)
    engine.runAndWait()


def onlySpeak(audio: str):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    query = "NO Response"
    try:
        print('Recognizing...')
        query = r.recognize_google(audio)
        print(f'You Said : {query}\n')

    except Exception as e:
        print('Please say again')

    return query


def wish(name='Deepak'):
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 12:
        speak('Good Morning ' + name)
    elif 12 < hour <= 16:
        speak('Good Afternoon ' + name)
    else:
        speak('Good Evening ' + name)

    speak('I am Mary, how may I help you ?')

def useBard(query: str):
    """
    :type query: str
    """
    print("Analyzing... this might take some time")
    ans = getAnswer(query)
    if len(ans) <= 200:
        speak(ans)
        return
    print(ans)
    speak("Here is your response. Do you want me to read it ?")
    inp = input('y/n : ').lower()[0]
    if inp == 'y':
        onlySpeak(ans)


def checkUnderstanding(query: str) -> bool:
    ls = ['no one understands', 'no one understand',
          'nobody understands', 'nobody understand',
          'no one seems to understands', 'no one seems to understand',
          'nobody seems to understands', 'nobody seems to understand'
          ]
    for i in ls:
        if i in query:
            return True
    return False
def checkConfession(query: str) -> bool:
    ls = ['i love you', 'go out with you', 'be my girlfriend',
          'go out with me', 'the moon is beautiful'
          ]
    for i in ls:
        if i in query:
            return True
    return False


if __name__ == '__main__':
    wish()
    while True:
        query = takeCommand().lower()
        # ans = getAnswer(query)
        # speak(ans)
        if 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'the time' in query or 'the present time' in query or 'the current time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("Time is : " + strTime)
        elif 'open code' in query or 'vs code' in query or 'launch code' in query or 'visual studio code' in query:
            path = r'C:\Users\dipud\AppData\Local\Programs\Microsoft VS Code\Code.exe'
            os.startfile(path)
        elif checkConfession(query):
            f = open('girlfriend.txt')
            speak(f.read())
            f.close()
        elif checkUnderstanding(query):
            f = open('understanding.txt')
            speak(f.read())
            f.close()
        elif ('play' in query and 'youtube' in query) or ('open' in query and 'youtube' in query):
            query.replace('play', '')
            query.replace('youtube', '')
            pywhatkit.playonyt(query)
        elif 'play' in query:
            query.replace('play', '')
            pywhatkit.playonyt(query)
        elif 'snapshot' in query or 'screenshot' in query:
            pywhatkit.take_screenshot('snap.png')
        elif 'code' in query:
            useBard(query)
        elif 'search' in query:
            query.replace('search', '')
            pywhatkit.search(query)
        elif len(query) >= 5:
            useBard(query)

        else:
            speak('Sorry, I did not understand it.')

