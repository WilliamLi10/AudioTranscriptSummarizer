from fpdf import FPDF

CHARACTER_LIMIT = 100
  
# save FPDF() class into
# a variable pdf




def pdf_converter(title,summary):
    pdf = FPDF()  
    
    # Add a page
    pdf.add_page()
    
    # set style and size of font
    # that you want in the pdf
    pdf.set_font("Times", size = 12)
    pdf.cell(0, 10, txt = title + " Summary", ln = 1, align = 'c')
    pdf.ln(10)

    # open the text file in read mode

    # insert the texts in pdf

    char_count = 0
    line = ""

    for i, sentence in enumerate(summary):
        line = str(i) + ") " + sentence
        pdf.multi_cell(0,5,txt = line, align= 'L')


    
    # save the pdf with name .pdf
    pdf.output("converted.pdf")  