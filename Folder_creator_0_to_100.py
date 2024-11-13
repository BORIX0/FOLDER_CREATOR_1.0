# Welcome Folder creator 0 to 100 ver 1.0. this tool creates 100 folders in a order. Like this = 001,002,003,010,050,089,0100.
# TOOL NAME: FOLDER_CREATOR_0_to_100 AND VERSION IS =  1.0 version... :) ...


import os 

# here you need to put your own path where you want the folders to be :)

path= ''
os.chdir(path)
for i in range (1,10):
        NewFolder='000' + str(i)
        os.makedirs(NewFolder)

# same with here put the same path here too!

path= ''
os.chdir(path)
for i in range (10,100):
        NewFolder='00' + str(i)
        os.makedirs(NewFolder)

