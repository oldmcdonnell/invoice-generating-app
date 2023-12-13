import openpyxl
import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("animals/*xlsx")

for filepath in filepaths: