import cv2
import os
import math
import glob
#import sys
import numpy as np
#import shutil
from tqdm import tqdm
from opts2 import parse_opts
opt = parse_opts()

def PanoramaImageCrop(file, savePath, preprocesstype):
	count = 1
	if preprocesstype == 'folder':
		for i in tqdm(file) :
			image = cv2.imread(i)
			name = os.path.basename(i)
			size = opt.crop_size
			v, h = image.shape[:2]
			i_max = h / size
			i_max = math.ceil(i_max) - 1
			j_max = v / size
			j_max = math.ceil(j_max) - 1
			for i in range(int(i_max)):
				for j in range(int(j_max)):
					image_crop = image[j*size:(j+1)*size, i*size:(i+1)*size]
					cv2.imwrite(savePath + name[:-4] + '_' + str(count) + '.png', image_crop)
					count += 1
	elif preprocesstype == 'image':
		savePath = file[0][:-4]
		if os.path.isdir(savePath):
			pass
		else:
			os.mkdir(savePath)
		count = 1
		image = cv2.imread(file[0])
		name = os.path.basename(file[0])
		size = opt.crop_size			
		v, h = image.shape[:2]
		i_max = h / size
		i_max = math.ceil(i_max) - 1
		j_max = v / size
		j_max = math.ceil(j_max) - 1
		
		for i in tqdm(range(i_max)):
			for j in range(j_max):
				image_crop = image[j*size:(j+1)*size, i*size:(i+1)*size]
				cv2.imwrite(savePath + name[:-4] + '_' + str(count) + '.png', image_crop)
				count += 1		


if __name__ == "__main__":

	folderpath = opt.crop_inputpath
	savefolder = folderpath.split('/')[-2]+'crop'+str(opt.crop_size)
	savepath = folderpath+savefolder+'/'
	preprocesstype = opt.preprocesstype
	if os.path.isdir(savepath):
		pass
	else:
		os.mkdir(savepath)
	imageList = glob.glob(folderpath + '*.png') or glob.glob(folderpath+'*.jpg')
	PanoramaImageCrop(imageList, savepath, preprocesstype)


			


