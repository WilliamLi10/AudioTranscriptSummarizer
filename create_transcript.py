from distutils.command.upload import upload
from sre_constants import JUMP
from google.cloud import speech_v1 as speech
from google.cloud import storage



def add_file(upload_path, destination_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket("lec-rec")
    blob = bucket.blob(destination_name)
    blob.upload_from_filename(upload_path)
def speech_to_text(config, audio):
    client = speech.SpeechClient()
    return client.long_running_recognize(config=config, audio=audio)
    
def create_transcript(wav_file):
    add_file(wav_file,wav_file)
    client = speech.SpeechClient()
    config = dict(language_code="en-US",audio_channel_count = 2,enable_automatic_punctuation=True)
    uri_name = "gs://lec-rec/" + wav_file
    audio = dict(uri= uri_name)
    operation = client.long_running_recognize(config=config, audio=audio)
    while(not operation.done()):
        print("Transcribing")
    response = operation.result()
    rets = ""
    for result in response.results:
        best_alternative = result.alternatives[0]
        transcript = best_alternative.transcript
        rets += transcript
    return rets

