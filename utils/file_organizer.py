import os,sys
import shutil
from utils.common import get_file_extension,create_directory

class FileOrganizer:
    def __init__(self, source_directory):
        self.source_directory = source_directory

    
    def organize_files(self):
        if not os.path.exists(self.source_directory):
            print("Source Dierctory not exists..")
            return
        for filename in os.listdir(self.source_directory):
            file_path = os.path.join(self.source_directory, filename)
            if os.path.isfile(file_path):
                extension = get_file_extension(filename)
                if extension:
                    destination_directory = os.path.join(self.source_directory,extension[1:])
                    create_directory(destination_directory)
                try:
                    shutil.move(file_path,os.path.join(destination_directory,filename))
                    print(f"moved'{filename}'to '{destination_directory}'")
                except Exception as e:
                    print(f"Error during Moving '{filename}'to '{destination_directory}' : {e}")
                else:
                    print("skipped '{filename}' as it doesn't have any extension")
            
            else:
                print("skipped '{filename}' as it is not a file")


