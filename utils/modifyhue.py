import numpy
import os
import cv2


def get_immediate_subdirectories(a_dir):
	filenames = []
	for root, dirs, files in os.walk(a_dir):
		for file in files:
			filenames.append(file)
	return filenames


def modify_hue(img, deg):
	pass


def change_hue(folder_path, sub_dir_list, deg=10):
	for i in sub_dir_list:
		img_path = os.path.join(folder_path, i)
		img = cv2.imread(img_path)
		hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
		hsv_img[:, :, 1] = hsv_img[:, :, 1] + deg
		new_img = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)
		cv2.imwrite(img_path, new_img)


if __name__ == '__main__':
	path = input("Give the location of image collection: ")
	degree = int(input("Give the degree of change: "))
	sub_dirs = get_immediate_subdirectories(path)
	change_hue(path, sub_dirs, degree)

