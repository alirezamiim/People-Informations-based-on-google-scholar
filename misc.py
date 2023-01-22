import csv
import re
# import CSVHandler
# import FolderHandler


country_name_code = {'us':'US','uk':'UK','de':'Germany','dk':'Denmark',
                     'se':'Sweden','at':'Austria','in':'India','it':'Italy',
                     'no':'Norway','nl':'Netherland','pt':'Portugal','be':'Belgium',
                     'es':'Spain','ie':'Ireland','fi':'Finland','fr':'France','au':'Australia',
                     'ca':'Canada'}


country_list=['Australia','Austria','Belgium','Canada','Denmark',
              'Finland','France','Germany','India','Ireland',
              'Italy','Netherland','Norway','Portugal','Spain',
              'Sweden','Switzerland','UK','US']



def Cleaner(input_string=''):
    input_string = re.sub(r'/.*','',input_string)
    input_string = re.sub(r'\(.*?\)','',input_string)
    input_string = re.sub(r'&#039;','\'',input_string)
    input_string = re.sub(r'&amp;','&',input_string)
    input_string = input_string.strip()
    return input_string
    
    
    
def UniName():
    with open('CSV Files/Universities DATA.csv',encoding='UTF-8',mode='r') as file:
        reader = csv.reader(file)
        for line in reader:
            line[1] = Cleaner(line[1])
            print(line)
            if line[3]=='us':
                uni_file = open('CSV Files/US/universities.csv',encoding='UTF-8',mode='a')
                uni_file.write(f'{line[0]},{line[1]},{line[2]},{line[3]}\n')
                uni_file.close()
            if line[3]=='uk':
                uni_file = open('CSV Files/UK/universities.csv',encoding='UTF-8',mode='a')
                uni_file.write(f'{line[0]},{line[1]},{line[2]},{line[3]}\n')
                uni_file.close()
            if line[3]=='de':
                uni_file = open('CSV Files/Germany/universities.csv',encoding='UTF-8',mode='a')
                uni_file.write(f'{line[0]},{line[1]},{line[2]},{line[3]}\n')
                uni_file.close()
            if line[3]=='ch':
                uni_file = open('CSV Files/Switzerland/universities.csv',encoding='UTF-8',mode='a')
                uni_file.write(f'{line[0]},{line[1]},{line[2]},{line[3]}\n')
                uni_file.close()
            if line[3]=='it':
                uni_file = open('CSV Files/Italy/universities.csv',encoding='UTF-8',mode='a')
                uni_file.write(f'{line[0]},{line[1]},{line[2]},{line[3]}\n')
                uni_file.close()
            if line[3]=='au':
                uni_file = open('CSV Files/Australia/universities.csv',encoding='UTF-8',mode='a')
                uni_file.write(f'{line[0]},{line[1]},{line[2]},{line[3]}\n')
                uni_file.close()
            if line[3]=='nl':
                uni_file = open('CSV Files/Netherland/universities.csv',encoding='UTF-8',mode='a')
                uni_file.write(f'{line[0]},{line[1]},{line[2]},{line[3]}\n')
                uni_file.close()
            if line[3]=='ca':
                uni_file = open('CSV Files/Canada/universities.csv',encoding='UTF-8',mode='a')
                uni_file.write(f'{line[0]},{line[1]},{line[2]},{line[3]}\n')
                uni_file.close()
            if line[3]=='fr':
                uni_file = open('CSV Files/France/universities.csv',encoding='UTF-8',mode='a')
                uni_file.write(f'{line[0]},{line[1]},{line[2]},{line[3]}\n')
                uni_file.close()
            if line[3]=='fi':
                uni_file = open('CSV Files/Finland/universities.csv',encoding='UTF-8',mode='a')
                uni_file.write(f'{line[0]},{line[1]},{line[2]},{line[3]}\n')
                uni_file.close()
            if line[3]=='es':
                uni_file = open('CSV Files/Spain/universities.csv',encoding='UTF-8',mode='a')
                uni_file.write(f'{line[0]},{line[1]},{line[2]},{line[3]}\n')
                uni_file.close()
            if line[3]=='ie':
                uni_file = open('CSV Files/Ireland/universities.csv',encoding='UTF-8',mode='a')
                uni_file.write(f'{line[0]},{line[1]},{line[2]},{line[3]}\n')
                uni_file.close()
            if line[3]=='se':
                uni_file = open('CSV Files/Sweden/universities.csv',encoding='UTF-8',mode='a')
                uni_file.write(f'{line[0]},{line[1]},{line[2]},{line[3]}\n')
                uni_file.close()
            if line[3]=='pt':
                uni_file = open('CSV Files/Portugal/universities.csv',encoding='UTF-8',mode='a')
                uni_file.write(f'{line[0]},{line[1]},{line[2]},{line[3]}\n')
                uni_file.close()
            if line[3]=='no':
                uni_file = open('CSV Files/Norway/universities.csv',encoding='UTF-8',mode='a')
                uni_file.write(f'{line[0]},{line[1]},{line[2]},{line[3]}\n')
                uni_file.close()
            if line[3]=='be':
                uni_file = open('CSV Files/Belgium/universities.csv',encoding='UTF-8',mode='a')
                uni_file.write(f'{line[0]},{line[1]},{line[2]},{line[3]}\n')
                uni_file.close()
            if line[3]=='dk':
                uni_file = open('CSV Files/Denmark/universities.csv',encoding='UTF-8',mode='a')
                uni_file.write(f'{line[0]},{line[1]},{line[2]},{line[3]}\n')
                uni_file.close()
            if line[3]=='in':
                uni_file = open('CSV Files/India/universities.csv',encoding='UTF-8',mode='a')
                uni_file.write(f'{line[0]},{line[1]},{line[2]},{line[3]}\n')
                uni_file.close()
            if line[3]=='at':
                uni_file = open('CSV Files/Austria/universities.csv',encoding='UTF-8',mode='a')
                uni_file.write(f'{line[0]},{line[1]},{line[2]},{line[3]}\n')
                uni_file.close()
            

# def FolderCreationForEachCSV():
#         for i in range(100):
#             FolderHandler.CreateFolder(path='UniversitiesCSV/'+str(i))
                


def Creating10by10():
    with open('Universities DATA.csv',mode='r',encoding='UTF-8') as refrence:
        universities = csv.reader(refrence)
        i=0
        counter=0
        # for item in country_name_code:
        #     print(item)
        for university in universities:
            if university[3] in country_name_code:
                university[1] = Cleaner(university[1])
                with open('UniversitiesCSV/'+str(counter)+'.csv',encoding='UTF-8',mode='a',newline='') as file:
                    writer = csv.writer(file)
                    
                    writer.writerow(university)
                # print(university)
                
                if (i+1)%10==0:
                    counter+=1
                    print(counter)
                i+=1  
            if(i==1000):
                exit()
                
# import os

# host = "www.google.com"

# i =  os.system("ping " + host )
# print(i)
                
       
        
        
        
        
        






