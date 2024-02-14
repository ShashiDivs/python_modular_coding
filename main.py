from utils.file_organizer import FileOrganizer

if __name__ == "__main__":
    source_directory = input("Enter the source directorty path")
    organize_files = FileOrganizer(source_directory)
    organize_files.organize_files()