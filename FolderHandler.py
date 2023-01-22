import os
import csv
import misc


def CreateFolder(path=''):
    try:
        os.mkdir(path=path)
        print('created')
    except OSError as error:
        if error.errno == 17:
            print('Exist')
        if error.errno == 22:
            print('Typo Directory')
        print(error.errno)
        
        
def UniName(country=''):
    with open('Files/'+country+'/'+'universities.csv',encoding='UTF-8') as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            yield line
    
for i in range(100):
    file_path = 'UniversitiesCSV/'+str(i)+'.csv'
    with open(file_path,mode='r',encoding='UTF-8') as refrence:
        universities = csv.reader(refrence)
        for university in universities:
            CreateFolder(path='UniversitiesCSV/'+str(i)+'/'+university[1]+'-'+misc.country_name_code[university[-1]])
            print('UniversitiesCSV/'+str(i)+'/'+university[1]+'-'+misc.country_name_code[university[-1]])
            
        



        








    


