import os
import sys
from glob import glob
import time
import datetime

def sort_with_time(rootdir):
    files_time_list = []
    for root, dir, files in os.walk(rootdir):
        for f in files:
            if f.endswith('.xlsx'):
                path = os.path.join(root, f)
                files_time_list.append((os.path.getmtime(path), path))
            else:
                pass

    if len(files_time_list)==0:
        print("No files were detected. Please run this file in a proper directory.")

    if len(files_time_list) > 1000:
        var = input("There are more than 1000 files. Do you really want to proceed? (y/n))")
        if var == ("y" or "Y"):
            pass
        elif var == ("n" or "N"):
            print("Quitting...")
            exit()
        else:
            print("Invalid answer. Please input y or n. Quitting...")
            exit()


    preview_index = 0
    for mtime, path in sorted(files_time_list, reverse=True):
        if preview_index >= 30:
            break
        name = path #os.path.basename(path)
        t = datetime.datetime.fromtimestamp(mtime)
        print(t, name)
        preview_index +=1
    
    input("Press ENTER to exit.")

def main():
    PATH = os.getcwd()
    print("This program displays the 'xlsx' files in order of the most recent update.")
    sort_with_time(PATH)

if __name__ == '__main__':
    main()

