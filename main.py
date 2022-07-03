from re import split
from openpyxl import load_workbook
from art import tprint

tprint('Maksim1337')
wb = load_workbook('excel.xlsx')
sheet = wb.active
coll1 = 1
coll2 = 1

with open('accounts.txt', "r") as file:
    for line in file:
        result = split(':',line)
        sheet[f'A{coll1}'] = result[0]
        coll1 += 1
        sheet[f'B{coll2}'] = result[1]
        coll2 += 1

wb.save('excel2.xlsx')