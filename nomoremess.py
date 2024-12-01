import os
from shutil import move
import json


#os.chdir("/Users/javantanna/Downloads")

#print(os.getcwd())

def load_config(file='config.json'):
    try:
        f=open(file,'r')
        return json.load(f)
    except FileNotFoundError:
        print(f"Config file not found: {file} ")
        return {}

def create_folders(directory):

    for dir_ in directory:
        try:
            os.mkdir(dir_)
            #print(f'{dir_} Created')
            
        except OSError:
            print(f'{dir_} already Exist')


def get_folder(ext,directory):
    for folder,extensions in directory.items():
        if ext in extensions:
            return folder
        return 'Other'

def start(directory):

    for filename in os.listdir():
        if filename!=cwd and filename[0]!='.' and '.' in filename:
            ext=os.path.basename(filename).split('.')[-1]
            folder=get_folder(ext,directory)
            if not os.path.isfile(os.path.join(folder,filename)):
                move(filename,folder)


        
        

if __name__=='__main__':
    config=load_config()
    cwd=os.chdir("/Users/javantanna/Downloads")
    create_folders(config)
    start(config)