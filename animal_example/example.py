import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("animals/*txt")

pdf =FPDF(orientation="P", unit="mm", format="A4")

def get_info(filepath=filepaths):
    with open(filepath, 'r') as file_local:
        info_local = file_local.readlines()
    return info_local

def write_info(info_arg, filepath=filepaths):
    with open(filepath, 'w') as file_local:
        file_local.writelines(info_arg)
        print(type(info_arg))

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

#prduce the PDf
pdf.output("output.pdf")
