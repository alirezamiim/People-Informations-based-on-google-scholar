import TXTFileHandler

def ProcessTrackerForUniversities(country='',university_name=''):
    """which university has started

    Args:
        country (str, optional): _description_. Defaults to ''.
        uni_name (str, optional): _description_. Defaults to ''.
    """
    TXTFileHandler.SaveText(path='Files/'+country,text_file_name=university_name
                            ,save_text=f'university {university_name} has Saved')