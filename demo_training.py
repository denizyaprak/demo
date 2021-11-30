import os

def get_file(dir):
    total = 0
    for sub_folders in os.listdir(str(dir)):
        counter = 0
        for files in os.listdir(dir + f"//{sub_folders}"):
            counter += 1
        total += counter
    return total