import openpyxl
import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*xlsx")
print(filepaths)

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    filename = Path(filepath).stem
    pdf.set_font(family="Arial", size=16, style="B")
    pdf.cell(w=50, h=8, txt="Invoice#")
