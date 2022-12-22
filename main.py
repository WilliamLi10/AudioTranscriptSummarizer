import sys
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from pdf_converter import *
from create_transcript import *

CHARACTER_LIMIT = 100

def main():

    wav_file = str(sys.argv[1])
    text = create_transcript(wav_file)
    outFile = open("transcript.txt","w")
    outFile.write(text)
    outFile.close()
    parser = PlaintextParser.from_file("transcript.txt",Tokenizer("english"))


    summarizer = LexRankSummarizer()
    summary = summarizer(parser.document,sys.argv[2])
    summary = ([str(i) for i in summary])
    #print(summary)
    pdf_converter(" ".join(sys.argv[1].split(".")[0].split("_")),summary)
    

if __name__ == "__main__":
    main()