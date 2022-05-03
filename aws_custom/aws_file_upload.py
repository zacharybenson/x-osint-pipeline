''' aws_file_upload.py
* ====================================================================================
* Name: Zachary Benson, Jan 2022
* Project: OSINT Pipeline
* Purpose: This file uploads images to S3.
* Contact Information: 
*     Email: zachary.n.benson@gmail.com
* ===================================================================================== 
'''
#Dependecies
import boto3
import os

def main(path,bucket):
    #Establish an S3 session
    s3 = boto3.client('s3')

    #Format Upload Command
    cmd = 'aws s3 cp --recursive ' + path + ' s3://' + bucket + '/ --quiet && echo Upload Complete || Upload Failed'

    #Run Command
    os.system(cmd)

if __name__ == "__main__":
        main()