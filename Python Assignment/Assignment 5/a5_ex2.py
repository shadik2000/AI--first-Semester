import os

def print_directory_recursively(dir_path: str, level: int):
    # If dir_path is a file
    if os.path.isfile(dir_path):
        print(f"{'  ' * level}{os.path.basename(dir_path)}")
        print(f"{'  ' * (level + 1)}dir_path is a file not a directory")
    # If dir_path is a directory
    elif os.path.isdir(dir_path):
        print(f"{'  ' * level}{os.path.abspath(dir_path)}")
        for item in os.listdir(dir_path):
            item_path = os.path.join(dir_path, item)
            print_directory_recursively(item_path, level + 1)
    # Print an error for an invalid path
    else:
        print(f"{'  ' * level}dir_path is invalid")

def print_directory(dir_path: str):
    print_directory_recursively(dir_path, 0)



# Example:
# print_directory(r"C:\Users\Hp\Desktop\Assignment 5\d0")
