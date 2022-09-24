import os
import sys
import speech_recognition as sr
import ffmpeg

file = sys.argv

r = sr.Recognizer()
transcriptData = ''

with sr.AudioFile(file) as source:
    r.adjust_for_ambient_noise(source)
    
    #listen to the audio in small increments, concatenating to transcriptData
    while True:
        try:
            audio_data = r.record(source, duration=30)
            transcriptPart = r.recognize_google(audio_data)
            transcriptData += transcriptPart + " "
        except:
            break

print(transcriptData)

f = open("transcript.txt", "w")
f.write(transcriptData)
f.close()


