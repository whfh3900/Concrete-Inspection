import os
import cv2
import numpy as np

accepted_130BY130_path_dir = 'spallSubImageForTraining/imageClustersV130B130/accepted/'
nonaccepted_130BY130_path_dir = 'spallSubImageForTraining/imageClustersV130B130/nonAccepted/'
accepted_2100BY2100_path_dir = 'spallSubImageForTraining/imageClustersV2100B100/accepted/'
nonaccepted_2100BY2100_path_dir = 'spallSubImageForTraining/imageClustersV2100B100/nonAccepted/'

file_list = []
error_file_list = []
error_f = open('cv_error_list.txt','w')
for i in [accepted_130BY130_path_dir,nonaccepted_130BY130_path_dir,accepted_2100BY2100_path_dir,nonaccepted_2100BY2100_path_dir]:
    each_file_list = os.listdir(i)
    for j in each_file_list:
        image_data = i+j
        file_list.append(image_data)
        try:
            img = cv2.imread(image_data)
            img = cv2.resize(img,(224, 224), interpolation = cv2.INTER_CUBIC)
        except cv2.error:
            error_file_list.append(image_data)
            error_f.write(image_data)
            error_f.write('\n')


f = open('train_list.txt','r')
no_f = open('nothing_list.txt','w')
#new_file_list = []
new_f = open('new_train_list.txt','w')
for _,file_name in enumerate(f):
	image_name = file_name.split(',')
	if image_name[0] in file_list:
		if image_name[0] not in error_file_list:
			data = '{},{}'.format(image_name[0],image_name[1])
			new_f.write(data)
	else:
		no_f.write(data)			
f.close()
new_f.close()

f = open('test_list.txt','r')
#new_file_list = []
new_f = open('new_test_list.txt','w')
for _,file_name in enumerate(f):
	image_name = file_name.split(',')
	if image_name[0] in file_list:
		if image_name[0] not in error_file_list:
			data = '{},{}'.format(image_name[0],image_name[1])
			new_f.write(data)				
	else:
		no_f.write(data)
f.close()
new_f.close()
print('-------------------------------------------spallSubImage done.-------------------------------------------')

accept_100BY100_path_dir = 'crackSubImageForTraining/100BY100/accept/'
nonaccpet_100BY100_path_dir = 'crackSubImageForTraining/100BY100/nonaccpet/'
accept_130BY130_path_dir = 'crackSubImageForTraining/130BY130/accept/'
nonaccpet_130BY130_path_dir = 'crackSubImageForTraining/130BY130/nonaccpet/'
file_list = []

for i in [accept_100BY100_path_dir,nonaccpet_100BY100_path_dir,accept_130BY130_path_dir,nonaccpet_130BY130_path_dir]:
    each_file_list = os.listdir(i)
    for j in each_file_list:
        image_data = i+j
        file_list.append(image_data)
        try:
            img = cv2.imread(image_data)
            img = cv2.resize(img,(224, 224), interpolation = cv2.INTER_CUBIC)
        except cv2.error:
            error_file_list.append(image_data)
            error_f.write(image_data)
            error_f.write('\n')
error_f.close()  


f = open('train_list_crack_2.txt','r')
#new_file_list = []
new_f = open('new_train_list_crack.txt','w')
for _,file_name in enumerate(f):
	image_name = file_name.split(',')
	if image_name[0] in file_list:
		if image_name[0] not in error_file_list:
			data = '{},{}'.format(image_name[0],image_name[1])
			new_f.write(data)				
	else:
		no_f.write(data)
f.close()
new_f.close()

f = open('test_list_crack_2.txt','r')
#new_file_list = []
new_f = open('new_test_list_crack.txt','w')
for _,file_name in enumerate(f):
	image_name = file_name.split(',')
	if image_name[0] in file_list:
		if image_name[0] not in error_file_list:
			data = '{},{}'.format(image_name[0],image_name[1])
			new_f.write(data)				
	else:
		no_f.write(data)
f.close()
new_f.close()
no_f.close()
print('-------------------------------------------crackSubImage done.-------------------------------------------')
