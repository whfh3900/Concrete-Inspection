# -*- coding: utf-8 -*-

import os
import cv2
import numpy as np
import glob
from opts2 import parse_opts
from tqdm import tqdm
opt = parse_opts()

path = opt.makelist_inputpath+'/'
folder_list = glob.glob(path + '*.png')
f = open(opt.makelist_name,'a')

class_num = 0
for i in tqdm(folder_list):
	#print(i)
	classification = i.split('_')[-2]
	if '배경' in classification:
		data = '{},{}\n'.format(i,class_num)
		f.write(data)
	elif '누수' in classification:
		class_num = 1
		data = '{},{}\n'.format(i,class_num)
		f.write(data)
	else:
		class_num = 2
		data = '{},{}\n'.format(i,class_num)
		f.write(data)		
f.close()

