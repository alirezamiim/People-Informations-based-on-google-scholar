import csv

def OpenUniversitiesCSV(country=''):
    with open('Files/'+country+'/universities.csv',mode='r',encoding='UTF-8') as csvFile:
        reader = csv.reader(csvFile)
        for line in reader:
            yield line
            
            
def SavePeopleDATA(path='',input_data=[],country='',university=''):
    with open(path,encoding='UTF-8',mode='a',newline='') as peopleCSV:
        for item in input_data:
            item.append(country)
            item.append(university)
            # writer = csv.DictWriter(peopleCSV,item.keys())
            # writer.writerow(item)
            writer = csv.writer(peopleCSV)
            writer.writerow(item)
        
        