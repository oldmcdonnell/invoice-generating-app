import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("animals/*txt")

pdf =FPDF(orientation="P", unit="mm", format="A4")


for filepath in filepaths:
    #add a page
    pdf.add_page()

    #filenames without exntion
    #title create

    filename = Path(filepath).stem
    name = filename.title()

    #add the name to the pdf
    pdf.set_font(family="Arial", size=16, style="B")
    pdf.cell(w=50, h=8, txt=name, ln=1)
#    pdf.cell(w=50, h=50, txt=animal_text, ln=5)

    #get the content
    with open(filepath, "r") as file:
        content = file.read()

    #write the content
    pdf.set_font(family="Arial", size=12)
    pdf.multi_cell(w=0, h=6, txt=content)


#prduce the PDf
pdf.output("output.pdf")
