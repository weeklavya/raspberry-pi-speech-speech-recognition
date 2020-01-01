 
# code for speech recogn
#input as GPIO 6,13,19,26

######################################################################## Refrence Documm #########################################

###https://github.com/Uberi/speech_recognition/blob/master/examples/microphone_recognition.py
######################################################################## Libraries must install in new devices #########################################
# sudo pip3 install SpeechRecognition
#sudo apt-get install portaudio19-dev
#sudo pip3 install pyaudio
###########################################################################################################################



import speech_recognition as sr  
import RPi.GPIO as GPIO
import datetime
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)

 
while True:
    
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
   
        
    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        speechval=r.recognize_google(audio)
        print(speechval)
        if(speechval=='Ok Google'):
            print('LED On')
            GPIO.output(26,GPIO.HIGH)
            time.sleep(10)
            GPIO.output(26,GPIO.LOW)
            print('LED Off')
            
        if(speechval=='turn right'):
            print('turning right')
            GPIO.output(26,GPIO.LOW)

        if(speechval=='current time'):
            print(datetime.datetime.now())
            
        
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
     
