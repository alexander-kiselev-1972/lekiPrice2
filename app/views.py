from django.shortcuts import render

import openpyxl

'''Имена  колонок в базе'''
titul = ['id', 'mnn', 'torgName', 'lekForm', 'factory', 'ATX', 'count', 'predCena',
         'CenaPervUpak', 'ru', 'dateReg', 'EAN13']

###################################################
''' записываем в файл данные'''


def beard_file_csv(data):
    with open('LekiPrice/app/leki.csv', 'a') as leki:
        data = str(data) + ','
        leki.write(data)


######################################################
'''создаем имена будущих колонок в базе'''


def write_titul_in_file(data):
    data = titul

    for name in data:
        beard_file_csv(name)


def read_file(file_name):
    wd = openpyxl.load_workbook(filename=file_name)
    sheet = wd.active

    row_count = sheet.max_row
    column_count = sheet.max_column

    row_count = row_count - (row_count - 10)
    for row in range(4, row_count):
        beard_file_csv('')
        for col in range(1, column_count - 1):

            work_cell = sheet.cell(row, col).value
            if work_cell == None:
                work_cell = ''
            if type(work_cell) == str:
                work_cell = work_cell.replace(',', '')
                work_cell = '"' + work_cell + '"'
            if type(work_cell) == int:
                work_cell = str(work_cell)
                work_cell = work_cell.replace(',', '.')

            beard_file_csv(work_cell)

    # for cellObj in sheet.columns[:5]:
    #   print(cellObj.value)
    # for row in sheet.rows:
    # for cell in row:
    #     print(cell.value)

    # mnn = sheet['B'+str(3)].value
    # torgName = sheet['B' + str(1)].value
    # print(mnn)


write_titul_in_file(titul)
read_file('Django-Import-Export/reports/lek5.xlsx')



# beard_file_csv(data)

