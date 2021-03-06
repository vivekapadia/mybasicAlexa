# Basic Alexa

Alexa is a virtual assistant - essentially a digital voice that can recognise spoken commands and then talk back,
meaning it can answer questions and perform certain tasks such as playing music

does to thing : listen | speak

## Features

- Play on youtube
- whatsapp an image
- ask for time
- get amazing jokes
- wikipedia - search well as summary about that topic

## Tech Stack

**Python:** 3.4 version and above

**PY Module:**

- [speech_recognition](https://pypi.org/project/SpeechRecognition/) Library for performing speech recognition
- [pyttsx3](https://pypi.org/project/pyttsx3/) Text to Speech (TTS) library for Python 2 and 3. Works without internet connection or delay.
- [wikipedia](https://pypi.org/project/wikipedia/) Wikipedia API for Python
- [pyjokes](https://pypi.org/project/pyjokes/) One line jokes for programmers (jokes as a service)
- [PyAudio](https://pypi.org/project/PyAudio/) Bindings for PortAudio v19, the cross-platform audio input/output stream library.
- [pywhatkit](https://pypi.org/project/pywhatkit/) PyWhatKit is a Simple and Powerful WhatsApp Automation Library with many useful Features

## Run Locally

[Clone](https://github.com/vivekapadia/mybasicAlexa.git/) the project

Create a python virtual environment to run the application

```bash
  virtualenv venv 
  .\venv\Scripts\activate
```

Install dependencies

```bash
  pip install -r requirements. txt
```

## Running Tests

To run tests, run the following command in your terminal

To start application

```bash
  py main.py
```

now when in terminal it says "Listen..." then,

```bash
 speak into your microphone : Alexa Play Jason Derulo
```

it will open your machine default browser and open youtube to play random song of Jason Derulo

## FAQ

#### create a vertual environment

virtualenv venv

#### activate the virtual environment

.\venv\Scripts\activate

#### list of modules|packages installed

pip freeze > requirements.txt

#### decativate the virtual environment

decativate

## Lessons Learned

how to integrate multiple python module and use it to have a simple communication between machine and user

## Authors

- [@vivekapadia](https://github.com/vivekapadia)
