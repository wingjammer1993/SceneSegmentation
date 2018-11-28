import re
import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict


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
	return dict_hue


if __name__ == '__main__':
	filenames = OrderedDict({"semseg-val-job.1335750.out": 'A', "semseg-val-job.1371191.out": 'B',
	             "semseg-val-job.1396458.out": 'C', "semseg-val-job.1454840.out": 'D'})
	def_vals = {'A': 0.44, 'B': 0.41, 'C': 0.38, 'D': 0.37}
	for k in default:
		for filename in filenames:
			file = open(filename)
			output = get_stats(k, file)
			if k == 'hue':
				output[0] = def_vals[filenames[filename]]
			else:
				output[1] = def_vals[filenames[filename]]
			new_x, new_y = zip(*sorted(zip(list(output.keys()), list(output.values()))))
			plt.plot(new_x, new_y, label=filenames[filename])
			plt.plot(new_x, new_y, 'g.')
			plt.ylim(0, 0.6)
			plt.xticks(new_x)
			# plt.axhline(y=0.36, color='r', linestyle='dotted', label='default mIOU on val set')
		plt.xlabel(k)
		plt.ylabel("Mean IoU")
		plt.title("SegNet - mIOU vs. {} value".format(k))
		plt.legend()
		plt.show()







