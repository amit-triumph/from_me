import os
import shutil
## ##

source_dir = r'C:\Users\Public\Amit\my_persnol\data'
desination_dir = r'C:\Users\Public\Amit\my_persnol\duplicate'

def get_file_list(source_dir):
    file_list = []
    for root,dir,files in os.walk(source_dir):
        for file in files:
            file_list.append(os.path.join(root,file))

    return file_list

def get_duplicate_files(file_list,):
    duplicate_list = []
    for i in range(len(file_list)):
        file_names = [file_path.split('\\')[-1][0:8] for file_path in file_list[i+1:len(file_list)]]
        # d_file_names = [d_files.split('\\')[-1][0:8] for d_files in d_files[i+1:len(d_files)]]
        # print(file_list[i].split('\\')[-1][0:8])
        # print([file_path.split('\\')[-1][0:8] for file_path in file_list[i+1:len(file_list)]])
        print([os.path.basename(f)[0:8] for f in os.listdir(desination_dir)])
        if (file_list[i].split('\\')[-1][0:8] in file_names and 
            file_list[i].split('\\')[-1][0:8] not in [os.path.basename(f)[0:8] for f in os.listdir(desination_dir)]):
            shutil.copy(file_list[i],desination_dir)
    return duplicate_list

if __name__ == '__main__':
    file_list = get_file_list(source_dir)
    d_list = get_duplicate_files(file_list,)
    print(os.listdir(desination_dir))

