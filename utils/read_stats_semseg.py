import re
import numpy as np
import matplotlib.pyplot as plt


default = {'hue': 0, 'contrast': 1, 'saturation': 1, 'brightness': 1, 'gamma': 1}


def get_stats(ip_string, file_text):
	dict_hue = {}
	elem = 0
	for line in file_text:
		if re.search(ip_string, line):
			kp = line.split()
			elem = float(kp[-1])
			if elem != default[ip_string]:
				dict_hue[elem] = 0
		if re.search('Mean IoU', line):
			m = line.split()
			if elem in dict_hue:
				if dict_hue[elem] == 0:
					dict_hue[elem] = float(m[-1])
	dict_hue[0] = 0.44
	return dict_hue


if __name__ == '__main__':
	filename = "semseg-val-job.1335750.out"
	for k in default:
		file = open(filename)
		output = get_stats(k, file)
		plt.bar(list(output.keys()), list(output.values()))
		plt.axhline(y=0.6, color='r', linestyle='dotted')
		plt.xlabel(k)
		plt.ylabel("Mean IoU")
		plt.title("Segnet")
		plt.show()







