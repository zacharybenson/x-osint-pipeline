''' aws_config.py
* ====================================================================================
* Name: Zachary Benson, Jan 2022
* Project: OSINT Pipeline
* Purpose: This file configures settings for aws.
* Contact Information: 
*     Email: zachary.n.benson@gmail.com
* ===================================================================================== 
'''
#Buckets
ENDPOINT_BUCKET = 'twitter-osint'

#Model Endpoint
END_POINT = 'tensorflow-inference-2022-05-02-22-44-49-873'

def s3_config():
    cmd = 'aws configure import --csv file://credentials.csv' #Config Command
    #Run Command
    os.system(cmd)
    
def main():
    return ENDPOINT_BUCKET, END_POINT

if __name__ == "__main__":
    main()
