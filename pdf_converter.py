from fpdf import FPDF

CHARACTER_LIMIT = 100
  
# save FPDF() class into
# a variable pdf
def pdf_converter(summary):
    pdf = FPDF()  
    
    # Add a page
    pdf.add_page()
    
    # set style and size of font
    # that you want in the pdf
    pdf.set_font("Times", size = 12)
    
    # open the text file in read mode

    # insert the texts in pdf

    char_count = 0
    line = ""
    for word in summary:
        char_count += len(word) + 1
        if char_count < CHARACTER_LIMIT:
            line += word + " "
        else:
            char_count = len(word) + 1
            pdf.cell(200, 20, txt = line, ln = 2, align = 'L')
            line = word + " "


    
    # save the pdf with name .pdf
    pdf.output("converted.pdf")  