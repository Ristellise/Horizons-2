import openpyxl
import os


def loadmod(abslocation):
    for root, dirs, files in os.walk(abslocation):
        for name in files:
            if name == "Resources.xlsx":
                wb = openpyxl.load_workbook(filename=name)
                # Set active to first page... (Resources)
                wb.active = 0
                worksheet = wb.active
                row1 = list(worksheet.rows[0])
                print(row1)