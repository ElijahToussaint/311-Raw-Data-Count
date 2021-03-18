# imports
import pandas
import openpyxl
import os


# function gets the number of rows and columns of the raw data csv files
def shapeCount():
    shapeList = []
    path = './raw_data/311_raw/'
    for directories in os.listdir(path):
        print(directories)
        relativeDirectoriesPath = os.path.join(path, directories)
        #print(relativeDirectories)
        for files in os.listdir(relativeDirectoriesPath):
            #print(files)
            relativeFilesPath = os.path.join(relativeDirectoriesPath, files)
            #print(relativeFilesPath)
            file = files.split('.')
            year = file[0]
            extension = file[1]
            if extension == 'csv':
                print(year)
                df = pandas.read_csv(relativeFilesPath, low_memory=False)
                rows, columns = df.shape
                print('Rows: ' + str(rows))
                print('Column: ' + str(columns))
                rowList = [directories, year, rows, columns]
                shapeList.append(rowList)
    #print(shapeList)
    return shapeList


# function that will connect the entire program together
# prints the various results of other functions
# this function acts as the main() of the program
def runProgram():
    if shapeCount():
        for row in shapeCount():
            ws.append(row)
        wb.save(filename='311_num_rows.xlsx')
        print('File successfully updated...')
    else:
        print('There is no file...')


# the program is ran here
print('+--------------------------------------+')
print('|RAW DATA ROW AND COLUMN COUNT PROGRAM |')
print('+--------------------------------------+')
print('Version 1.0.0')
print('Sukumar Ganpati')
print('Elijah Toussaint')
print('Farzana Yusuf' + '\n')

# run the program
try:
    wb = openpyxl.Workbook()
    ws = wb.active
    columnNames = ['City','Year','Rows','Columns']
    for value in range(len(columnNames)):
        cell = ws.cell(row=1, column=value+1) 
        cell.value = columnNames[value]
    wb.save(filename='311_num_rows.xlsx')
    runProgram()
except FileNotFoundError:
    print('File already exist...')
