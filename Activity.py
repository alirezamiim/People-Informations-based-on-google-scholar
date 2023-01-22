import WebCrawler
import URLPrepartion
import ScrapeData


class Person:
    
    def ScrapeActivity(self):
        
        self.last_activity_url =  URLPrepartion.Last_Activity_URL(scholar_url_code= self.scholar_code) 
        self.most_cited_url =   URLPrepartion.Most_Cited_URL(scholar_url_code=self.scholar_code)
        
        self.last_activity_web_page = WebCrawler.OpenWebPage(url=self.last_activity_url) 
        self.most_cited_web_page = WebCrawler.OpenWebPage(url=self.most_cited_url)
        
        self.last_activity = ScrapeData.ScrapeActivity(input_string=self.scholar_code)
        self.most_cited_activity = ScrapeData.ScrapeActivity(input_string=self.most_cited_activity)
    
    '&view_op=list_works&sortby=pubdate'
    def __init__(self,scholar_code=''):
        self.scholar_code = scholar_code