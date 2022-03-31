# make sure u r in write directory
# pip virtualenv
# virtualenv venv 
# .\venv\Scripts\activate
# pip install SpeechRecognition pyttsx3 pywhatkit pyjokes pipwin flask
# pipwin install pyaudio
# pip freeze > requirements.txt
# to run this file : py main.py
# end venv : decativate
# exit()


# input : person's audio
# (speech recognition operations - Recognizer, Microphone , listen , recognize_google)
import speech_recognition as sr

# output : machine audio
# (pyttsx3 operations - init, Microphone , listen , recognize_google)
import pyttsx3

# output : action for 
# (pywhatkit operations - playonyt , sendwhats_image)
import pywhatkit

# Wikipedia API for Pythons
# (wikipedia operations - summary , search)
import wikipedia
# default setting language is english 
wikipedia.set_lang("en")

# One line jokes for programmers (jokes as a service)
import pyjokes

listener = sr.Recognizer()

# initialized with default voice
# During construction, the engine initializes and loading a speech engine driver module.
engine = pyttsx3.init()

def take_command():
    """
    take command from user via microphone
    this function doesn't take any argument

    Returns:
        string: user voice text
    """
    command = ''
    
    try:
        # microphone audio input
        # source : <speech_recognition.Microphone object at 0x000001B5247C2230>
        with sr.Microphone() as source:

            print('listening...')
                        
            # voice : <speech_recognition.AudioData object at 0x000001B526888EB0>
            voice = listener.listen(source)
            print(voice)

            # Performs speech recognition on audio_data (an AudioData instance),
            # using the Google Speech Recognition API.
            # returns a list of possible transcriptions (strings).
            command = listener.recognize_google(voice)

            command = command.lower()
            if 'alexa' in command:
                # remove 'alexa' from command
                command = command.replace('alexa', '')
                print(command)
                
    except :
        pass

    return command


def alexa_response(text):
    """
    alexa reponse to user

    Args:
        text (string): any kind of information you want to hear from alexa
    """
    
    # text to speech and send output through speaker
    engine.say(text)
    
    # machine to speak at human audible speed 
    engine.runAndWait()


def alexa_operations():
    """
    multiple operation on command from user to get useful information from alexa
    """
        
    command = take_command()
    
    if 'stop' in command:
        exit()
        
    if 'play' in command:
        song = command.replace('play', '')
        alexa_response('playing '+song)
        
        # this function will play song on your computer
        pywhatkit.playonyt(song)
    
    elif 'whatsapp' in command:
        # Send an Image to a Contact with the no Caption
        pywhatkit.sendwhats_image("+919427004928", "Images/Hello.png")
        
    elif 'what is the time' in command:
        # system time 
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        alexa_response('Current Time is '+time)

    elif 'what are you' in command:
        alexa_response('I am a virtual assistant')
    
    elif 'joke' in command:
        print(pyjokes.get_joke())
        alexa_response(pyjokes.get_joke())      
    
    elif 'wikipedia' in command:
        person = command.replace('wikipedia', '')
        
        # what to search
        info = wikipedia.search(person,results=5)
        print("\n\twikipedia search's\n",info,"\n")
        
        # whos summary , and how many lines to return
        info = wikipedia.summary(person, sentences = 3)            
        print(info,"\n")
        alexa_response("wikipedia summary" + info)
        
    else :
        option = input('Do you have any more query ? [y|n]\n').lower()
        if option == 'n':
            exit()

try : 
    print('Welcome to virtual assistant')
    while True:
        alexa_operations()
except Exception as e:
    print(e)
finally :
    print("\n\tStopping Alexa\n Thank you for using virtual assistant\n\n\n")        