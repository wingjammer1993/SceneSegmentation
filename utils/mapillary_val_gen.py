""" open each mapillary label, iterate through every pixel
and group it in cityscapes classes to create a cityscapes
compliant validation set, save the new label set.
This label set will be opened with mapillary data loader"""

import os
import json
import cv2
import numpy as np

cityscapes_mapillary_map = {'Bird' : 0, 'Ground Animal' : 0, 'Curb' : 8, 'Fence' : 13,
                            'Guard Rail': 13, 'Barrier': 13, 'Wall': 12, 'Bike Lane': 7,
                            'Crosswalk - Plain' :7, 'Curb Cut' : 8, 'Parking' : 7,
                            'Pedestrian Area': 7, 'Rail Track': 7, 'Road': 7,
                            'Service Lane': 7, 'Sidewalk' :8, 'Bridge': 7,
                            'Building': 11, 'Tunnel': 7, 'Person': 24, 'Bicyclist': 25,
                            'Motorcyclist': 25, 'Other Rider': 25, 'Lane Marking - Crosswalk': 7,
                            'Lane Marking - General': 7, 'Mountain': 22, 'Sand': 22, 'Sky': 23, 'Snow': 21,
                            'Terrain': 22, 'Vegetation': 21, 'Water': 21, 'Banner': 20, 'Bench': 8, 'Bike Rack': 8,
                            'Billboard': 20, 'Catch Basin': 7, 'CCTV Camera': 17, 'Fire Hydrant': 17, 'Junction Box': 17,
                            'Mailbox': 17, 'Manhole': 7, 'Phone Booth': 17, 'Pothole': 7, 'Street Light': 19, 'Pole': 17,
                            'Traffic Sign Frame': 20, 'Utility Pole': 17, 'Traffic Light': 19, 'Traffic Sign (Back)' : 20,
                            'Traffic Sign (Front)' :20, 'Trash Can' : 17, 'Bicycle': 33, 'Boat': 26, 'Bus': 28, 'Car':26, 'Caravan':31,
                            'Motorcycle': 32, 'On Rails': 31, 'Other Vehicle': 27, 'Trailer': 27, 'Truck': 27, 'Wheeled Slow': 27,
                            'Car Mount': 26, 'Ego Vehicle': 26, 'Unlabeled': 0}


def map_new_labels(n, id, colr, filenames, oldpath, newpath):
	for fn in filenames:
		fname = os.path.join(oldpath, fn)
		lbl = cv2.imread(fname)
		r, c, p = lbl.shape
		newlabel = np.zeros((r, c))
		for i in range(0, r):
			for j in range(0, c):
					idx = colr.index([lbl[i][j][2], lbl[i][j][1], lbl[i][j][0]])
					key = n[idx]
					if key in cityscapes_mapillary_map:
						newlabel[i][j] = cityscapes_mapillary_map[key]
		newfpath = os.path.join(newpath, fn)
		cv2.imwrite(newfpath, newlabel)


def get_immediate_subdirectories(a_dir):
    filenames = []
    for root, dirs, files in os.walk(a_dir):
        for file in files:
            filenames.append(file)
    return filenames


def parse_config(root):
	with open(os.path.join(root, 'config.json')) as config_file:
		config = json.load(config_file)

	labels = config['labels']

	class_names = []
	class_ids = []
	class_colors = []
	print("There are {} labels in the config file".format(len(labels)))
	for label_id, label in enumerate(labels):
		class_names.append(label["readable"])
		class_ids.append(label_id)
		class_colors.append(label["color"])

	return class_names, class_ids, class_colors


if __name__ == '__main__':
	# path_val = r"C:\Users\Amruta\Desktop\Project\Datasets\Mapillary"
	# path_new_val = r"C:\Users\Amruta\Desktop\Project\Datasets\Mapillary\validation\labels"
	path_val = r"/projects/amra8468/Mapillary"
	path_new_val = r"/projects/amra8468/Mapillary/validation/labels"
	print("getting subdirectories")
	fnames = get_immediate_subdirectories(path_val + "\labels")
	print("parsing config")
	names, ids, colors = parse_config(path_val)
	print("mapping labels, this may take a while..")
	map_new_labels(names, ids, colors, fnames, path_val + "\labels", path_new_val)

