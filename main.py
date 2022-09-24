import sys
from condensor import *
from pdf_converter import *
from create_transcript import *

CHARACTER_LIMIT = 100

def main():

    wav_file = str(sys.argv[1])
    create_transcript(wav_file)
    
    file = open("transcript.txt", "r")
    text = file.read()
    document = nlp(text)
    file.close()

    summary = str(generate_summary(3, document)).split(" ")
    pdf_converter(summary)
    

if __name__ == "__main__":
    main()