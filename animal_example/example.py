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

#prduce the PDf
pdf.output("output.pdf")
