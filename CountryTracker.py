
import FolderHandler
import CSVHandler


class MyCountries:
    
    def CreateFolder(self):
        for university_name in CSVHandler.OpenUniversitiesCSV(country=self.country): 
            FolderHandler.CreateFolder(country=self.country,university_name=university_name[1])
    
   
    def __init__(self,country=''):
        self.country = country
    
    
italy = MyCountries(country='Italy')
uk = MyCountries(country='UK')
us = MyCountries(country='US')
india = MyCountries(country='India')
denmark = MyCountries(country='Denmark')
norway = MyCountries(country='Norway')
switzerland = MyCountries(country='Switzerland')
sweden = MyCountries(country='Sweden')
spain = MyCountries(country='Spain')
portugal = MyCountries(country='Portugal')
netherland = MyCountries(country='Netherland')
ireland = MyCountries(country='Ireland')
germany = MyCountries(country='Germany')
canada = MyCountries(country='Canada')
finland = MyCountries(country='Finland')
france = MyCountries(country='France')
austria = MyCountries(country='Austria')
australia = MyCountries(country='Australia')
belgium = MyCountries(country='Belgium')

country_list =[us,uk,india,denmark,italy,norway,canada,belgium,australia,austria,france,finland,germany,
               spain,portugal,netherland,ireland,sweden,switzerland]

for country in country_list:
    country.CreateFolder()

    






