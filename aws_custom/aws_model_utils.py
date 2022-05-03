''' aws_model_utils.py
* ====================================================================================
* Name: Zachary Benson, Jan 2022
* Project: OSINT Pipeline
* Purpose: This file contains the neccessary utilities to run model innferences.
* Contact Information: 
*     Email: zachary.n.benson@gmail.com
* ===================================================================================== 
'''
#Dependecies
import json
import numpy as np
import boto3
import glob
from IPython.display import display, Image
import os
from aws_custom.aws_config import *

'''
** classify_obstruction_type(image_path)
* @brief
* classifies fingerprint against ml model, to determine
* the likelyhood that it is a given obstruction type.
* @param image_path - path to image to analyse.
* @return list -prediction and certinity of labels

*'''
def model_inference(image_path,endpoint):

    imgage_path = load_img(image_path) 
    #Define endpoint
    endpoint_name = endpoint
    
    #Define runtime session 
    runtime = boto3.Session().client(service_name="runtime.sagemaker")

    #Open File to test
    with open(image_path, "rb") as f:
        payload = f.read()
        payload = bytearray(payload)
    response = runtime.invoke_endpoint(
        EndpointName=endpoint_name, ContentType="application/x-image", Body=payload
    )
    
    result = response["Body"].read()
    # result will be in json format and convert it to ndarray
    
    result = json.loads(result)
   
    return result

'''
** list_pictures():
* @brief - collects list of all pictures in test file.
* @return list - of picture paths
*'''
def list_pictures(path):
    #gathers list of all finger prints in test file
    list_of_pictures = glob.glob(path + "*.jpg")
    
    #determines number of files
    num_pictures = len(list_of_pictures)
    return list_of_pictures,num_pictures
            
'''
**  file_name_info()
* @brief - segments file name to obtain actual fingerprint labels
* @param - path to fingerprint file
* @return list - full list of labels 
*'''
def file_name_info(path):
    #strip path
    labels = os.path.basename(path)
    
    #strip filee extension
    labels = labels.split(".")[0]
    
    #segment information
    labels = labels.split("_")
    
    #returns full list of labels
    return labels

def check_images(files, endpoint):
    delete = []
    for file in files:
        results = model_inference(file, endpoint)
        #FIXME:check results, if not boat
        if(results[5] > .80 ): 
            #add filename to delete
            delete.append(file)

    return delete

def delete_non_boats(files):
    for filePath in files:
        try:
            os.remove(filePath)
        except:
            print("Error while deleting file : ", filePath)

def remove_from_df(df,delete):
    #Deleting specific information from dataframe. 
    return df[df.column_name.isin(delete) == False]


def load_image(filepath):
    # load the image
    img = load_img(filepath)
    
    # resize the images for model enpoint.
    img = smart_resize(img, (180,180))

    return img