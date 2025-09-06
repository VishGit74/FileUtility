import os
import shutil
import json
import sys
from datetime import datetime
from pathlib import Path

class SmartOrganizer:
    def __init__(self,target_directory):
        self.target_dir = target_directory
        self.log_file = "org_logfile.json"
        self.categories = {
            'Documents':['pdf','docx','doc','txt'],
            'Data':['xlsx','xls','csv','json'],
            'Media':['pptx']
        }

    def fileOrganize(self):
        # Create log file Create Folders and write data to log !!

        foldersCreated = []
        op_data = []

        pathName = self.target_dir
        for category in self.categories.keys():
            newDir = os.path.join(pathName,category)
            os.makedirs(newDir,exist_ok = True)
            foldersCreated.append(newDir)

        op_data_member = {
            "path_name":pathName,
            "directories":{
                "folder1":foldersCreated[0],
                "folder2":foldersCreated[1],
                "folder3":foldersCreated[2]
            }
        }

        op_data.append(op_data_member)

      # Check all files in the directory and move them

        for files in os.listdir(pathName):
            if files.endswith('docx') or files.endswith('pdf') or files.endswith('doc') or files.endswith('txt'):
                src_path = os.path.join(pathName,files)
                dest_path = os.path.join(foldersCreated[0],files)
                shutil.move(src_path,dest_path)

            elif files.endswith('xlsx') or files.endswith('xls') or files.endswith('csv') or files.endswith('json'):
                src_path = os.path.join(pathName,files)
                dest_path = os.path.join(foldersCreated[1],files)
                shutil.move(src_path,dest_path)

            elif files.endswith('pptx') or files.endswith('ppt'):
                src_path = os.path.join(pathName,files)
                dest_path = os.path.join(foldersCreated[2],files)
                shutil.move(src_path,dest_path)


        # Write Data into log     

        with open(self.log_file,'a') as file:
            file.write(json.dumps(op_data) + '\n')
        
    
# Define Main Function

def main():
    # Get user input

    pathName = str(sys.argv[1])
    smartOrg1 = SmartOrganizer(pathName)
    smartOrg1.fileOrganize()
    
    

# Calling Main

if __name__ == '__main__':
    main()
    
