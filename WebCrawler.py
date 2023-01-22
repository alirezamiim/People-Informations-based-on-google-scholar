from selenium import webdriver

def OpenWebPage(url=''):
    """Get URL and return its source

    Args:
        url (str, optional): _description_. Defaults to ''.

    Returns:
        str: return web page source if available
    """
    
    driver = webdriver.Chrome('chromedriver.exe')
    try:
        driver.get(url)
        web_page_source = driver.page_source
        driver.quit()
    except:
        web_page_source = 'web page Error'
    return web_page_source


# print(OpenWebPage(url = 'https://www.youtube.com'))


