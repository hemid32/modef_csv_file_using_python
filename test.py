# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tempfile import NamedTemporaryFile
import shutil
import csv
import os

arr = os.listdir('D:/pythonProject1/files/')

print(arr)

filename = 'D:/pythonProject1/files/21-1 C400.csv'
tempfile = NamedTemporaryFile(mode='w', delete=False)

fields = ['Time', 'Open', 'High', 'Low', 'Last', 'Change',
          'Volume', 'Open' 'Int', 'IV', 'Delta', 'Gamma', 'Theta', 'Vega', 'Rho', 'Theo', 'Price', 'Strike']

#fieldsWrite = ['ttttt', 'Time', 'Open', 'High', 'Low',]


def modifeFileCsv() :
    derecory = input('derectory : ')
    derectoryUse = derecory.replace('\\' , '/')
    file_edit = input('file or all ?  : ')
    field_delet = input(' field delet ==  or no tabi false  : ')


    with open(filename, encoding='utf8') as csvfile, tempfile:
        nameField = filename.split('/')[-1]
        reader = csv.DictReader(csvfile)
        fieldsWrite = []
        for i in reader.fieldnames :
            fieldsWrite.append(i)
        # = reader.fieldnames
        fieldsWrite.insert(0, nameField)
        print(fieldsWrite)
        if ('false' != 'false'):
            delet = deletField(reader.fieldnames , 'false')
            if(delet == False ) :
                print('this field note exist')
            else :
                fieldsWrite = delet

        writer = csv.DictWriter(tempfile, fieldnames=fieldsWrite)
        print('*** creat heaser')
        writer.writeheader()
        for row in reader:
            rowN = {}
            for filed in fieldsWrite :
                if filed == nameField :
                    rowN[filed] = filed
                else :
                    rowN[filed] = row[filed]
            print('write ===', rowN )
            writer.writerow(rowN)
    shutil.move(tempfile.name, filename)

modifeFileCsv()


def deletField(listfedl , feildDelet):
    field_delete = input('Type the name of the column you want to delete if no column delete insert false : ')
    if(field_delete != 'false'):
        if(field_delete in listfedl ) :
            listfedl.remove(feildDelet)
            return  listfedl
        else :
            print('Error column not exist .. !')
            return
    else :
        return  listfedl


