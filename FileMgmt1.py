import os
import shutil
import json
import sys
from datetime import datetime
from pathlib import Path

class SmartOrganizer:
    def __init__(self,target_directory):
        self.target_dir = target_directory
        self.log_file = "org_logfile.jsonl"
        self.categories = {
            'Documents':['pdf','docx','doc','txt'],
            'Data':['xlsx','xls','csv','json'],
            'Media':['pptx','ppt','jpeg','mpg'],
            'Applications':['dmg','zip','exe']
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
                "folder3":foldersCreated[2],
                "folder4":foldersCreated[3]
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

            elif files.endswith('pptx') or files.endswith('ppt') or files.endswith('jpeg') or files.endswith('mpg'):
                src_path = os.path.join(pathName,files)
                dest_path = os.path.join(foldersCreated[2],files)
                shutil.move(src_path,dest_path)

            elif files.endswith('dmg') or files.endswith('zip') or files.endswith('exe'):
                src_path = os.path.join(pathName,files)
                dest_path = os.path.join(foldersCreated[3],files)
                shutil.move(src_path,dest_path)


        # Write Data into log     

        with open(self.log_file,'a') as file:
            file.write(json.dumps(op_data_member) + '\n')


        with open(self.log_file,'r') as file:
            for line in file:
                record = json.loads(line.strip())
                for key,folder in record['directories'].items():
                    print (folder)
                


# Define Main Function

def main():
    # Get user input



    pathName = str(sys.argv[1])
    smartOrg1 = SmartOrganizer(pathName)
    smartOrg1.fileOrganize()
     
# Calling Main

if __name__ == '__main__':
    main()


    
