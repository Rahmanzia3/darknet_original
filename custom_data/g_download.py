'''
WAT TO CHANGE OBJ.DATA OBJ.NAMES NAD MAKE FILE

'''



import requests
from tqdm import tqdm
from zipfile import ZipFile 
import sys

import os
from argparse import ArgumentParser
import argparse
# In OBJ.DATA you need to change no. of classes, training.txt, testing.txt and backup location
'''
classes= 2
train  = /home/tericsoft/mustafa/darknet/mask_own/train.txt
#valid  = coco_testdev
valid = /home/tericsoft/mustafa/darknet/mask_own/train.txt
names = /home/tericsoft/mustafa/darknet/mask_own/obj.names
backup = /home/tericsoft/mustafa/darknet/mask_own/backup

'''


def download_file_from_google_drive(id, destination):
    def get_confirm_token(response):
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                return value

        return None

    def save_response_content(response, destination):
        CHUNK_SIZE = 32768

        with open(destination, "wb") as f:
            with tqdm(unit='B', unit_scale=True, unit_divisor=1024) as bar:
                for chunk in response.iter_content(CHUNK_SIZE):
                    if chunk:  # filter out keep-alive new chunks
                        f.write(chunk)
                        bar.update(CHUNK_SIZE)

    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)    


def un_zip(source,destination):
    
    file_name = source
  
    # opening the zip file in READ mode 
    with ZipFile(file_name, 'r') as zip: 
    # printing all the contents of the zip file 
        zip.printdir() 
      
        # extracting all the files 
        print('Extracting all the files now...') 

        # ######## ADD DESTINATION LOCATION HERE
        zip.extractall(destination) 
        print('Done!') 

def delete_zip(download_directory):
    path = download_directory
    os.remove(path)
    print('ZIP file has beed deleted')










def obj_data_is(number):
    print('OBJ DATA DATA',number)
    append_lines = []

    classes = "classes = "+str(int(number[0]))+'\n'
    train = "train =" +str(os. getcwd())+"/training.txt\n"
    valid = "valid =" +str(os. getcwd())+"/testing.txt\n"
    names_o = "names =" +str(os. getcwd())+"/obj.names\n"
    backup = "backup =" +str(os. getcwd())+"/backup\n"

    append_lines.append(classes)
    append_lines.append(train)
    append_lines.append(valid)
    append_lines.append(names_o)
    append_lines.append(backup)

    obj_data = open(str(os. getcwd())+"/obj.data","w")
    obj_data.writelines(append_lines)



    # print(lines)
def obj_names_is(names):

    #### # In OBJ.NAMES you need to add class names
    ###### Number of classes must be equals to number of classes here
    append_lines_names = []
    obj_names = open(str(os. getcwd())+"/obj.names","w")
    for x in range(len(names)):
        # print(x)
        # print('!!!!!!!!!!!!!!!!!!!!!!!')
        if x != len(names)-1:
            text = names[x]+'\n'
        # text = str(x)+'\n'
            append_lines_names.append(text)
        elif x == len(names)-1:
            text = names[x]
            append_lines_names.append(text)

    names_lines = obj_names.writelines(append_lines_names)
    obj_names.close()



def cfg(number):

    '''
    in yolov4  yolo.cfg file you need to change ln:960,1047,1134 as filters=(classes+5)*3
                                                ln:967,1054,1141 as classes=opt.no_classes

    THIS IS YOLOV4 IN YOLO V3 NUMBER OF LINE MIGHT BE DIFFER SO IF YOU ARE USING OTHER VERSION 
    YOU NEED TO CHANGE LINE NUMBER SO THAT CODE CAN WRITE THERIR

    '''

    file = open(str(os. getcwd())+'/yolo.cfg','r')
    lines = file.readlines()
    # print('!!!!!!!!!!!!!!!!!!!!!',lines)

    lines[960] = 'filters='+str((int(number[0])+5)*3)+'\n'
    lines[1134] = 'filters='+str((int(number[0])+5)*3)+'\n'
    lines[1047] = 'filters='+str((int(number[0])+5)*3)+'\n'

    lines[967] = 'classes='+ str(int(number[0]))+'\n'
    lines[1054] = 'classes='+ str(int(number[0]))+'\n'
    lines[1141] = 'classes='+ str(int(number[0]))+'\n'




    file = open(str(os. getcwd())+'/yolo.cfg','w')
    file.writelines(lines)
    file.close()

def create_txt(path):
    # #### Directory where data has been uploaded
    # READ FOLDER FROM
    pre_folder_path  = '/app/darknet/custom_data'


    # TEST ON LOCK DIRECTORY
    # pre_folder_path = '/home/tericsoft/team_alpha/automate_yolo/same_as_git_data'
    folder_name_al = os.listdir(pre_folder_path)

    for x in folder_name_al:
        if x != 'g_download.py':
            folder_name = os.path.join(pre_folder_path,x)


    print(folder_name)

    # folder_name = os.listdir(pre_folder_path)

    # for x in folder_name:
    #     if x != g_download.py:
    #         folder_name = os.path.join(pre_folder_path,x)


    folder_path = os.path.join(pre_folder_path,folder_name)

    sub_folder = os.listdir(folder_path)

    count_1_array = []
    count_2_array = []

    count = 0
    for x in sub_folder:
        dir_sub_folder = os.path.join(folder_path,x)
        images_name = os.listdir(dir_sub_folder)
        surb_array = []
        count = count + 1
        for img in images_name:
            extention = img.rpartition('.')[-1]
            if count == 1:
                # print(111111111111)

                if extention == 'jpg':
                    img_dir = os.path.join(dir_sub_folder,img)
                    # print(img_dir)
                    file1 = open("1.txt", "a")  # append mode 
                    file1.write(str(img_dir)+"\n") 
                    file1.close() 
                    count_1_array.append(1)
            elif count == 2:
                # print(2222222222222222222222)

                if extention == 'jpg':
                    img_dir = os.path.join(dir_sub_folder,img)

                    # print(img_dir)
                    file1 = open("2.txt", "a")  # append mode 
                    file1.write(str(img_dir)+"\n") 
                    file1.close() 

                    count_2_array.append(2)

    first_len  = len(count_1_array)
    second_len = len(count_2_array)

    one_txt_dir = str(os. getcwd())+'/1.txt'

    two_txt_dir = str(os.getcwd())+'/2.txt'


    training_dir = str(os.getcwd())+'/training.txt'
    testing_dir = str(os.getcwd())+'/testing.txt'



    if first_len > second_len:
        os.rename(one_txt_dir,training_dir)
        os.rename(two_txt_dir,testing_dir)
    elif first_len < second_len:
        os.rename(two_txt_dir,training_dir)
        os.rename(one_txt_dir,testing_dir)

def start_training(run):
    run_command = str(run)
    path = '/app/darknet/'
    os.chdir(path)
    os.system(run_command)





if __name__ == "__main__":

    google_drive_id = input("Enter google downloadable ID: ")
# This is valid for DOcker
    download_directory = '/app/darknet/custom_data/alpha.zip'


    # download_directory = '/home/tericsoft/team_alpha/automate_yolo/test_download/alpha.zip'




# This is valid dir in Docker
    unzip_dir = '/app/darknet/task/'

# This is valid in local
    # extract_dir = '/home/tericsoft/team_alpha/automate_yolo/test_download/'


    extract_dir = '/app/darknet/task/'

    number_of_classes = list(map(str, input("Enter interger value of number of classes: ").split()))
    names_of_classes = list(map(str, input("Enter NAMES of classes (str): ").split()))

    download_file_from_google_drive(google_drive_id,download_directory)
    un_zip(download_directory,extract_dir)
    delete_zip(download_directory)
   
    obj_data_is(number_of_classes)
    obj_names_is(names_of_classes)
    cfg(number_of_classes)
    create_txt('')

    alpha_tran = './darknet detector train '+str (os.getcwd())+'/obj.data ' +str (os.getcwd())+'/yolo.cfg '+str (os.getcwd())+'/yolov4.conv.137  -dont_show'

    print('Copy below line and paste it in CMD (darknet dir) \n Tostart training'  )
    print(alpha_tran)
    start_training(alpha_tran)
