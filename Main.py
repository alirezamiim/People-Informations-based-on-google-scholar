
import ScrapeData
import WebCrawler
import URLPrepartion
import CSVHandler
import threading
import os
import csv
import misc

class People:    
    def LoadScrapeProgress(self):
        with open(self.txt_path,mode='r',encoding='UTF-8') as file:
            
            data = file.readlines()[-1].split(',')
            data[0] = int(data[0])
            self.page_number = data[0]
            self.next_link = data[1]
        
        
    def SavingScrapingProgress(self):
        self.save_text=f'{str(self.page_number+1)},{self.next_link}'
        CSVHandler.SavePeopleDATA(self.csv_path,input_data=self.scraped_data,
                                  country=self.country,university=self.university_name)
        with open(self.txt_path,mode='w',encoding='UTF-8') as file:
            file.write(self.save_text)
        backup = open(self.txt_path + 'backup.txt' , mode='a',encoding='UTF-8') 
        backup.write(self.save_text+'\n')
        backup.close()
        

        
        
        
    def ScrapeProgress(self):
        self.preparedURL = URLPrepartion.URL_Prepration (page_number=self.page_number,uni_name=self.university_name
                                                            ,next_page_code=self.next_link)
        self.web_page_source = WebCrawler.OpenWebPage(self.preparedURL)
        self.scraped_data = ScrapeData.ScrapeData(input_string=self.web_page_source) 
        self.next_link = ScrapeData.ScrapeNextLink(input_string=self.web_page_source)

        if self.next_link == 'Not Found' and len(self.scraped_data) == 0:
            exit()
        
    
        
    def CheckFileExistance(self):
        if os.path.isfile(self.csv_path) == False:
            open(self.csv_path,mode='x')
            print('csv created')
            
        if os.path.isfile(self.txt_path) == False:
            file = open(self.txt_path,mode='x')
            file.write('0,NM')
            file.close()
            print('txt created')
            
    
    def MainProgress(self):
        while  self.next_link != 'Not Found':# and self.page_number < self.how_many_pages_to_find :
            
            self.LoadScrapeProgress()
            self.ScrapeProgress()
            self.SavingScrapingProgress()
    
    def __init__(self,university_name = '',country = '',csv_index=0,next_link='NM'):
        self.how_many_pages_to_find = 1
        self.page_number = 0
        self.next_link=next_link
        self.university_name = university_name
        self.country = country
        self.csv_index=csv_index
        self.data_path = 'Files/'+self.country+'/'+self.university_name+'/'
        self.csv_path = ('UniversitiesCSV/'+str(self.csv_index)+'/'+self.university_name+'-'+self.country+'/'
                  +self.university_name+'-'+self.country+'.csv')
        self.txt_path = ('UniversitiesCSV/'+str(self.csv_index)+'/'+self.university_name+'-'+self.country+'/'
                  +self.university_name+'-'+self.country+'.txt')
        self.CheckFileExistance()
        self.LoadScrapeProgress()

def ScrapePeople():
    CSV_INDEX = 0
    universities = []
    UNIVERSITY_INDEX=0
    COUNTRY_INDEX = 1 
    with open('UniversitiesCSV/'+str(CSV_INDEX)+'.csv',encoding='UTF-8',mode='r') as file:
            reader = csv.reader(file)
            
            for line in reader:
                university_name = line[1]
                country = misc.country_name_code[line[3]]
                universities.append([university_name,country])
        
    uni_0 = People(university_name=universities[0][UNIVERSITY_INDEX]
                    ,country=universities[0][COUNTRY_INDEX],csv_index=CSV_INDEX)
    uni_1 = People(university_name=universities[1][UNIVERSITY_INDEX]
                    ,country=universities[1][COUNTRY_INDEX],csv_index=CSV_INDEX)
    uni_2 = People(university_name=universities[2][UNIVERSITY_INDEX]
                    ,country=universities[2][COUNTRY_INDEX],csv_index=CSV_INDEX)
    uni_3 = People(university_name=universities[3][UNIVERSITY_INDEX]
                    ,country=universities[3][COUNTRY_INDEX],csv_index=CSV_INDEX)
    uni_4 = People(university_name=universities[4][UNIVERSITY_INDEX]
                    ,country=universities[4][COUNTRY_INDEX],csv_index=CSV_INDEX)
    uni_5 = People(university_name=universities[5][UNIVERSITY_INDEX]
                    ,country=universities[5][COUNTRY_INDEX],csv_index=CSV_INDEX)
    uni_6 = People(university_name=universities[6][UNIVERSITY_INDEX]
                    ,country=universities[6][COUNTRY_INDEX],csv_index=CSV_INDEX)
    uni_7 = People(university_name=universities[7][UNIVERSITY_INDEX]
                    ,country=universities[7][COUNTRY_INDEX],csv_index=CSV_INDEX)
    uni_8 = People(university_name=universities[8][UNIVERSITY_INDEX]
                    ,country=universities[8][COUNTRY_INDEX],csv_index=CSV_INDEX)
    uni_9 = People(university_name=universities[9][UNIVERSITY_INDEX]
                    ,country=universities[9][COUNTRY_INDEX],csv_index=CSV_INDEX)



    t0 = threading.Thread(target=uni_0.MainProgress)
    t1 = threading.Thread(target=uni_1.MainProgress)
    t2 = threading.Thread(target=uni_2.MainProgress)
    t3 = threading.Thread(target=uni_3.MainProgress)
    t4 = threading.Thread(target=uni_4.MainProgress)
    t5 = threading.Thread(target=uni_5.MainProgress)
    t6 = threading.Thread(target=uni_6.MainProgress)
    t7 = threading.Thread(target=uni_7.MainProgress)
    t8 = threading.Thread(target=uni_8.MainProgress)
    t9 = threading.Thread(target=uni_9.MainProgress)

    t0.start()
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start() 

ScrapePeople()
