import os

#function to return the two lists, on with all text file paths and other with the names of all files
Output_folder="Output/"
def get_file_path(Output_folder):
    file_path =os.listdir('Output/')
    files=file_path[:]
    # for i,j in enumerate(file_path):
    #     file_list[i]=f'Output/{j}/{j}.wav'
    file_path=[f'Output/{j}/{j}.txt' for j in (file_path)]
    return file_path,files