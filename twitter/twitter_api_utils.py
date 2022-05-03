''' twitter_api_utils.py
* ====================================================================================
* Name: Zachary Benson, Jan 2022
* Project: OSINT Pipeline
* Purpose: This file contains the neccessary utilities to run twitter api.
* Contact Information: 
*     Email: zachary.n.benson@gmail.com
* ===================================================================================== 
'''
#Dependecies
import pandas as pd
import json
import numpy as np
import os
import glob

def tweets_to_df(tweets):
    # Save data as dictionary
    tweets_dict = tweets.json() 
    print(json.dumps(tweets_dict, indent=1))
    
    # Extract "data" value from dictionary
    tweets_data = tweets_dict['data'] 

    # Transform to pandas Dataframe
    return pd.json_normalize(tweets_data) 

def initilize_download():
    path = os.getcwd()

    #Try to make download and upload foldeer
    try:
        os.mkdir(path + '/download')
        os.mkdir(path + '/upload')
        print("Folder is ready for download")
        os.chdir(path + '/download') 
    #If they are already made, move into download folder.
    except:
        print("Folder is ready for download")
        os.chdir(path + '/download') 


def download_image(URL):
    #Download image using terminal command.
    cmd_dl = 'gallery-dl ' + '"' + URL + '"' + ' -d' + '"' + URL + '"'
    #Run Command
    os.system(cmd_dl)

def clean_up():
    path = os.getcwd()
    #Move file to basedirectory
    cmd_mv = 'find ' + '"' + path + '"' + ' -name "*.jpg" -exec mv {} "'+ path + '" \;'
    os.system(cmd_mv)

    #Clean up folders created during download
    cmd_clean = 'find . -type d -empty -delete'
    os.system(cmd_clean)

def move_for_upload(path_from, path_to):
    cmd_mv = 'find ' + '"' + path_from + '"' + ' -name "*.jpg" -exec mv {} "'+ path_to + '" \;'
    os.system(cmd_mv)

    #Clean up folders created during download
    cmd_clean = 'find . -type d -empty -delete'
    os.system(cmd_clean)

def delete_temp_folders(download, upload):
    #Clean up folders created during download
    cmd_clean = 'rm -R ' + download + ';'
    cmd_clean = cmd_clean + 'rm -R ' + upload
    os.system(cmd_clean)
    
def download(x):
    #Try to get the tweet download url, if its not there move on.
    try:
        photo_url = x['entities.urls'][0].get('expanded_url')
        download_image(photo_url)
        
    except:
        print("There is not an image at this link to download.")
    else:
        print('Working...')

def list_images():
   path = os.getcwd() + '/download/'
   print(path)
   return glob.glob(path + "*.jpg")