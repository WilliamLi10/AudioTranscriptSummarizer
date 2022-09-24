import speech_recognition as sr

def create_transcript(file):

    r = sr.Recognizer()
    transcript_data = ''

    with sr.AudioFile(file) as source:
        r.adjust_for_ambient_noise(source)
        
        #listen to the audio in small increments, concatenating to transcriptData
        while True:
            try:
                audio_data = r.record(source, duration=30)
                transcript_part = r.recognize_google(audio_data)
                transcript_data += transcript_part + " "
            except:
                break

    #print(transcriptData)

    f = open("transcript.txt", "w")
    f.write(transcript_data)
    f.close()


