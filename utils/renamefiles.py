import shutil
import os
import re


def natural_sort(s, _nsre=re.compile('([0-9]+)')):
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(_nsre, s)]

def get_immediate_subdirectories(a_dir):
    filenames = []
    for root, dirs, files in os.walk(a_dir):
        for file in files:
            filenames.append(file)
    return filenames


def rename(path1, path2, newmap):
	for i,j in newmap:
		a = os.path.join(path2, i)
		b = os.path.join(path1, j)
		shutil.move(a, b)
	print('done')


def create_map(dir1, dir2):
	a = get_immediate_subdirectories(dir1)
	b = get_immediate_subdirectories(dir2)
	a.sort(key=natural_sort)
	newmp = zip(a, b)
	return newmp


if __name__ == '__main__':
	path_modif = r'C:\Users\Amruta\Desktop\new'
	path_map = r'C:\Users\Amruta\Desktop\Project\Datasets\Cityscapes\leftImg8bit_trainvaltest\leftImg8bit\valmodif\munster'
	mp = create_map(path_modif, path_map)
	rename(path_map, path_modif, mp)


