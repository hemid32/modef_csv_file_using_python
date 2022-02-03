# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tempfile import NamedTemporaryFile
import shutil
import csv
import os



fields = ['Time', 'Open', 'High', 'Low', 'Last', 'Change',
          'Volume', 'Open' 'Int', 'IV', 'Delta', 'Gamma', 'Theta', 'Vega', 'Rho', 'Theo', 'Price', 'Strike']

#fieldsWrite = ['ttttt', 'Time', 'Open', 'High', 'Low',]
def deletField(listfedl, columnDelet):
    """

    """
    #field_delete = input('Type the name of the column you want to delete if no column delete insert false : ')
    if(columnDelet != 'false'):
        if(columnDelet in listfedl ) :
            listfedl.remove(columnDelet)
            return  listfedl
        else :
            print('Error column  not exist ... !!!!!')
            #return
    else :
        return  listfedl








def mainModifeFile(filename , columnDelet) :
    #print('start creat === ' , filename)
    tempfile = NamedTemporaryFile(mode='w', delete=False)
    with open(filename, encoding='utf8') as csvfile, tempfile:
        nameField = (filename.split('/')[-1])[0:-4]
        reader = csv.DictReader(csvfile)
        fieldsWrite = []
        for i in reader.fieldnames:
            fieldsWrite.append(i)
        # = reader.fieldnames
        fieldsWrite.insert(0, nameField)
        # print(fieldsWrite)
        fieldsWrite = deletField(fieldsWrite , columnDelet)
        writer = csv.DictWriter(tempfile, fieldnames=fieldsWrite )
        writer.writeheader()
        for row in reader:
            rowN = {}
            for filed in fieldsWrite:
                if filed == nameField:
                    rowN[filed] = filed
                else:
                    rowN[filed] = row[filed]
            #print('write ===', rowN)
            writer.writerow(rowN)
    shutil.move(tempfile.name, filename)
    print('***Edited  ', filename , ' successfully***')


def modifeFileCsv() :
    derecory = input('put directory path : ')
    derectoryUse = derecory.replace('\\' , '/')
    file_edit = input('Do you want to update all the files in the file ? if yes click all if no put nome file  : ')
    field_delet = input('put the name of the column you want to delete or false if you no delete any column  : ')

    arr = os.listdir(derectoryUse)
    if(file_edit == 'all'):
        for file in arr :
            mainModifeFile(derectoryUse + '/'+ file , field_delet )
    else :
        if file_edit + '.csv' in arr :
            mainModifeFile(derectoryUse + '/' + file_edit  + '.csv' , field_delet )
        else :
            print('file not exist ')


modifeFileCsv()
