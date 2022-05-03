# #Dispatcher
import schedule
from twitter.twitter_scrape import *
from subprocess import call
from postgree.df_sql_utils import main as sql_main
from twitter.twitter_scrape import main as tws_main
from aws.aws_file_upload import main as aws_up_main 
from aws.aws_config import *
from aws.aws_model_utils import *
 
def main():
    # Scrape For Tweets
    df = tws_main()

    #Download Images
    download_image(df)

    # Filter For Tweets with Boats
    image_files = list_images()
    delete_list = check_images(image_files, END_POINT)
    #Remove tweets that dont have boats
    df = remove_from_df(df, delete_list)
    delete_non_boats(delete_list)

    # Translate tweets if needed

    # Spacy Pipeline

    # Save Pictures to S3
    move_for_upload(path_down,path_up)
    aws_up_main(path_to) 
    delete_temp_folders(path_down, path_up)
    # Scoring

    # Save To Database
    sql_main(df)


#Complete this task everyday.
schedule.every(1).day.do(main)
 
while True:
    schedule.run_pending()