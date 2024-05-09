import os

def get_files_in_directory(directory):
    files = []
    for file_name in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file_name)):
            files.append(file_name)
    return files
