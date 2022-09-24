from fpdf import FPDF
  
# save FPDF() class into
# a variable pdf
def pdf_converter(text_file):
    pdf = FPDF()  
    
    # Add a page
    pdf.add_page()
    
    # set style and size of font
    # that you want in the pdf
    pdf.set_font("Times", size = 12)
    
    # open the text file in read mode
    f = open(text_file, "r")
    
    # insert the texts in pdf
    for x in f:
        pdf.cell(200, 10, txt = x, ln = 2, align = 'L')
    
    # save the pdf with name .pdf
    pdf.output("converted.pdf")  