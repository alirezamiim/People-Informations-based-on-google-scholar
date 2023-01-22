#This Script is for txt file handling
import os


def OpenText(path='',text_file_name=''):
    """this is the function for openin the txt and retuen the data

    Args:
        text_file_name (str, optional): the name of txt file want to open. Defaults to ''.

    Returns:
        str: the text which is stored in the 
    """
    try:
        text_file = open(path+text_file_name+'.txt',mode='r')
        txt = text_file.read()
        text_file.close()
    except:
        txt = 'Choose the right File ٔName to read!!'
    return txt #return the text as string
    

def SaveText(path='',text_file_name='',save_text=''):
    """This function is for Saving the str into a txt

    Args:
        text_file_name (str, optional): this is the name of the file which want to write. Defaults to ''.
        input_txt (str, optional): input String. Defaults to ''.
    """
    try:
        text_file = open(path+text_file_name+'.txt',mode='a')
        text_file.write(save_text+'\n')
        text_file.close()
    except:
        print('Choose the correct Path File Name To Save!!!',save_text)
        
        
def DeletTextFile(path='',text_file_name=''):
    os.remove(path+'/'+text_file_name+'.txt')
    pass


