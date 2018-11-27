""" open each mapillary label, iterate through every pixel
and group it in cityscapes classes to create a cityscapes
compliant validation set, save the new label set.
This label set will be opened with mapillary data loader"""

import os
import json


cityscapes_mapillary_map = {}


def map_new_labels(filenames, newpath):
	pass


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
	path_val = r"C:\Users\Amruta\Desktop\Project\Datasets\Mapillary"
	path_new_val = r"C:\Users\Amruta\Desktop\Project\Datasets\Mapillary\validation\labels"
	fnames = get_immediate_subdirectories(path_val + "\labels")
	map_new_labels(fnames, path_new_val)
	names, ids, colors = parse_config(path_val)
