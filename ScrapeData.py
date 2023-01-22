import re
from bs4 import BeautifulSoup
import URLPrepartion

def ScrapeNextLink(input_string=''):
    """Scrape Next Link

    Args:
        input_string (str, optional): _description_. Defaults to ''.
    """
    soup = BeautifulSoup(input_string,'html.parser')
    
    next_link = soup.find('button',attrs={'aria-label': 'Next'})

    try:
        next_link = next_link['onclick']
        next_link = re.findall(r'after_author\\x3d(.*?)\\x26astart',next_link)[0]
    except :
        next_link = 'Not Found' 
    

    return next_link



def ScrapeActivity(input_string=''):
    soup = BeautifulSoup(input_string,'html.parser')
    result = soup.find('tr',attrs={'class':'gsc_a_tr'})
    soup = BeautifulSoup(str(result),'html.parser')
    title = soup.find('a',attrs={'class':'gsc_a_at'}).text
    cited_by = soup.find('a',attrs={'class':'gsc_a_ac gs_ibl'}).text
    year = soup.find('td',attrs={'class':'gsc_a_y'}).text
    if cited_by == '':
        cited_by = 'Not Mentioned'
    return [title,cited_by,year]
    
    
    
    

def ScrapeData(input_string=''):
    soup = BeautifulSoup(input_string,'html.parser')
    names = soup.find_all('h3',attrs={'class':'gs_ai_name'})
    departments = soup.find_all('div',attrs={'class':'gs_ai_aff'})
    emails = soup.find_all('div',attrs={'class':'gs_ai_eml'})
    citations = soup.find_all('div',attrs={'class':'gs_ai_cby'})
    fields_of_study = soup.find_all('div',attrs= {'class':'gs_ai_int'})
    scholar_url = []
    
    for field in range(len(fields_of_study)):
        soup = BeautifulSoup(str(fields_of_study[field]),'html.parser')
        fields_of_study[field] = soup.find_all('a', attrs={'class':'gs_ai_one_int'})
        for item in range(len(fields_of_study[field])):
            fields_of_study[field][item] = fields_of_study[field][item].text
        
    for item in range(len(citations)):
        citations[item] = re.sub(r'Cited by ','',citations[item].text)
        emails[item] = re.sub(r'Verified email at ','',emails[item].text)
        
    for item in range(len(names)):
        result = BeautifulSoup(str(names[item]),'html.parser')
        result = result.find('a')
        result = re.sub(r'.*user=','',result['href'] )
        result = URLPrepartion.Person_URL(scholar_url_code=result)
        scholar_url.append(result)
        # print(scholar_url[item])
        
    for index in range(len(names)):
        names[index] = names[index].text
        departments[index] = departments[index].text
        fields_of_study[index] = ' | '.join(fields_of_study[index])
    my_list = []   
    for person in range(len(names)):
        my_list.append([names[person],departments[person],emails[person],
                       citations[person],fields_of_study[person],scholar_url[person]])
    
    return my_list
        
    

# file = open('New.txt')
# inputstr=file.read()
# next_link = ScrapeNextLink(input_string=inputstr)
# print(next_link)


# print(next_link)
# with open('New.txt') as file:
#     print(file.readline()[-1])



    





