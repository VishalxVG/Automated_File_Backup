## Python Backup Script

This repository contains a backup script written in Python, utilizing the os, shutil, datetime, and schedule libraries to perform scheduled backups. The script is designed to run daily at 16:42.

### How to Use:

1. **Import Necessary Libraries:** Import the required libraries: `os`, `shutil`, `datetime`, and `schedule`.

2. **Define Source and Destination Directories:** Define the source directory (`source_dir`) and the destination directory (`destination_dir`). In this case, the source directory is the "Screenshots" folder in the user's OneDrive Pictures folder, and the destination directory is a "Backup" folder on the user's desktop.

3. **Define `copy_folder_to_directory` Function:** This function takes two arguments: the source directory (`source`) and the destination directory (`dest`). It creates a new folder in the destination directory with the current date as its name. Then, it tries to copy the entire source directory to the new folder using `shutil.copytree`. If the folder already exists in the destination directory, it raises a `FileExistsError` and prints a message.

4. **Schedule Backup Operation:** Schedule the `copy_folder_to_directory` function to run every day at 16:42 using `schedule.every().day.at("16:42").do()`.

5. **Run Infinite Loop:** Run an infinite loop that checks for scheduled tasks using `schedule.run_pending()`. The loop sleeps for 60 seconds between each check using `time.sleep(60)`.

### Running the Script:

When the script is executed, it will create a backup of the source directory in the destination directory every day at 16:42. If the backup folder already exists in the destination directory, it will not overwrite it. Instead, it will create a new folder with the current date as its name.

### Note:

This script assumes that the source directory and the destination directory are on the same drive. If they are not, you may need to adjust the code to handle the transfer of files between different drives.

