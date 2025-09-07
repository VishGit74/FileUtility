import os
import shutil
import json
import sys
import logging
from datetime import datetime
from pathlib import Path

logging.basicConfig(filename='filemgmt.log', level=logging.INFO, format='%(asctime)s - %(message)s')

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

# File organizing method

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

        with open(self.log_file,'a') as file:
            file.write(json.dumps(op_data_member) + '\n')

        op_data.append(op_data_member)

      # Move files and write data to log 
        try:
            for files in os.listdir(pathName):
                if files.endswith('docx') or files.endswith('pdf') or files.endswith('doc') or files.endswith('txt'):
                    src_path = os.path.join(pathName,files)
                    dest_path = os.path.join(foldersCreated[0],files)
                    shutil.move(src_path,dest_path)
                    logging.info(f"Transferred {src_path} to {dest_path}")
                    file_transfer_data = {
                        "source":src_path,
                        "destination":dest_path
                    }
                    with open(self.log_file,'a') as file:
                        file.write(json.dumps(file_transfer_data) + '\n')      

                elif files.endswith('xlsx') or files.endswith('xls') or files.endswith('csv') or files.endswith('json'):
                    src_path = os.path.join(pathName,files)
                    dest_path = os.path.join(foldersCreated[1],files)
                    shutil.move(src_path,dest_path)
                    logging.info(f"Transferred {src_path} to {dest_path}")
                    file_transfer_data = {
                        "source":src_path,
                        "destination":dest_path
                    }
                    with open(self.log_file,'a') as file:
                        file.write(json.dumps(file_transfer_data) + '\n')             

                elif files.endswith('pptx') or files.endswith('ppt') or files.endswith('jpeg') or files.endswith('mpg'):
                    src_path = os.path.join(pathName,files)
                    dest_path = os.path.join(foldersCreated[2],files)
                    shutil.move(src_path,dest_path)
                    logging.info(f"Transferred {src_path} to {dest_path}")
                    file_transfer_data = {
                        "source":src_path,
                        "destination":dest_path
                    }
                    with open(self.log_file,'a') as file:
                        file.write(json.dumps(file_transfer_data) + '\n')
                

                elif files.endswith('dmg') or files.endswith('zip') or files.endswith('exe'):
                    src_path = os.path.join(pathName,files)
                    dest_path = os.path.join(foldersCreated[3],files)              
                    shutil.move(src_path,dest_path)
                    logging.info(f"Transferred {src_path} to {dest_path}")
                    file_transfer_data = {
                        "source":src_path,
                        "destination":dest_path
                    }
                    with open(self.log_file,'a') as file:
                        file.write(json.dumps(file_transfer_data) + '\n')
                    
        except shutil.Error as e:
            logging.error(f"Shutil error: {e}")

        except FileNotFoundError as e:
            logging.error(f"File not found error: {e}")
             
# Method that looks at log file and undoes any file transfers         
                
    def undoOrg(self):
        print("Enter the path of the file you want to undo")
        try:
            choice_file = input ("File path: ")
            with open(self.log_file,'r') as file:
                for line in file:
                    record = json.loads(line.strip())
                    values_list = list(record.values())
                    if len(values_list) == 2:
                        if (values_list[1] == choice_file):                     
                                src_path = values_list[1]
                                dest_path = values_list[0]
                                shutil.move(src_path,dest_path)
                                print("Transfer Done")

                                file_transfer_undo_data = {
                                    "source":src_path,
                                    "destination":dest_path
                                }

                                with open(self.log_file,'a') as file:
                                    file.write(json.dumps(file_transfer_undo_data) + '\n')

        except FileNotFoundError as e:
            logging.error(f"File not found error: {e}")

# Method for printing log file        

    def printLog(self):
        print("Printing report....")
        with open(self.log_file,'r') as file:
            for line in file:
                record = json.loads(line.strip())
                print (record)

# Main Function

def main():
    # Get user input

    
    while True:

        print("Welcome to the file management utility \n")
        print("--------------------------------------\n\n")
        print("1. Organize Files\n")
        print("2. Undo organization\n")
        print("3. Print org logs\n")
        print("\n\n")
        print("Enter a choice (1-3) or any other key to exit program")

        choice = input("Your choice: ")

        if choice == "1":
            print("Enter the directory you want organized\n")
            choice_dir1 = input("Directory name: ")
            smartOrg1 = SmartOrganizer(choice_dir1)
            smartOrg1.fileOrganize()
        elif choice == "2":   
            print("Enter the directory you want organized\n")
            choice_dir2 = input("Directory name: ")         
            smartOrg2 = SmartOrganizer(choice_dir2)
            smartOrg2.undoOrg()
        elif choice == "3":
            print("Enter the directory you want organized\n")
            choice_dir3 = input("Directory name: ")  
            smartOrg3 = SmartOrganizer(choice_dir3)       
            smartOrg3.printLog()
        elif choice =="x":
            print("Exiting program....")
            sys.exit(0)
        else:
            print("Invalid choice - please enter [1-3] or x to exit")

# Calling Main

if __name__ == '__main__':
    main()


    
