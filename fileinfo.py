import os

def get_file_info(file_path):
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)
    return {'name': file_name, 'size': file_size}

def main():
    # Get the current working directory
    current_directory = os.getcwd()

    # Get the list of files in the current working directory
    files_list = os.listdir(current_directory)

    # Filter out directories and get file information
    file_info_list = [get_file_info(file) for file in files_list if os.path.isfile(file)]

    # Print the list of dictionaries
    for file_info in file_info_list:
        print(file_info)

if __name__ == "__main__":
    main()
