
from condensor import *
from pdf_converter import *

def main():
    file = open("book-1984.txt", "r")
    text = file.read()
    document = nlp(text)
    file.close()

    summary = generate_summary(3, document)
    
    new_file = open("text.txt", "w")
    for line in summary:
        new_file.write(str(line))
    new_file.close()
    

    pdf_converter("text.txt")
    

if __name__ == "__main__":
    main()