import os
import shutil
import datetime
import schedule
import time


# Source  directory
source_dir = r"C:\Users\avata\OneDrive\Pictures\Screenshots"
# Destination Directory
destination_dir = r"C:\Users\avata\OneDrive\Desktop\Backoup"

def copy_folder_to_directory(source , dest):
    today = datetime.date.today()
    # To save the folder  with date and time of backup
    des_dir = os.path.join(dest , str(today))

    try:
        shutil.copytree(source, des_dir)
        print(f"Folder copied to : {des_dir}")

    except FileExistsError:
        print(f"Folder already exists in : {dest}")    

# To run a particular time  everyday
schedule.every().day.at("16:42").do(lambda: copy_folder_to_directory(source_dir, destination_dir)) 


while True:
    # It will call all the schedule  functions at their respective times
    schedule.run_pending()
    time.sleep(60) # A minute interval


