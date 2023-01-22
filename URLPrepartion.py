import re

def URL_Prepration(next_page_code='NM',page_number=0,uni_name=''):
    """function to prepare the url for crawler

    Args:
        next_page_code (str, optional): _description_. Defaults to ''.
        page_number (int, optional): _description_. Defaults to 0.
        uni_name (str, optional): _description_. Defaults to ''.

    Returns:
        str: google scholar url
    """
    google_scholar_url=''
    uni_name = re.sub(r'\s','+',uni_name)
    page1_temp = f'https://scholar.google.com/citations?hl=en&view_op=search_authors&mauthors={uni_name}&btnG='
    other_pages_temp=f'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors={uni_name}&after_author={next_page_code}&astart={page_number*10}'
    if page_number == 0:
        google_scholar_url = page1_temp
    else:
        google_scholar_url = other_pages_temp
    return google_scholar_url

def Person_URL(scholar_url_code=''):
    return f'https://scholar.google.com/citations?hl=en&user={scholar_url_code}'


def Last_Activity_URL(scholar_url_code=''):
    return f'https://scholar.google.com/citations?hl=en&user={scholar_url_code}&view_op=list_works&sortby=pubdate'

def Most_Cited_URL(scholar_url_code=''):
    return f'https://scholar.google.com/citations?hl=en&user={scholar_url_code}'