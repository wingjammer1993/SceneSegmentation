import re
import numpy as np
import matplotlib.pyplot as plt


def get_stats(file_text):
	dict_hue = {}
	elem = 0
	for line in file_text:
		if re.search('hue value', line):
			k = line.split()
			elem = float(k[-1])
			dict_hue[elem] = 0
		if re.search('meanIOU', line):
			m = line.split()
			dict_hue[elem] = float(m[-1])
	return dict_hue


if __name__ == '__main__':
	filename = "deeplab-hue-job.1297084.out"
	file = open(filename)
	output = get_stats(file)
	plt.bar(list(output.keys()), list(output.values()))
	plt.axhline(y=0.6, color='r', linestyle='dotted')
	plt.xlabel("+/- hue variation")
	plt.ylabel("Mean IoU")
	plt.title("DeepLab + Pascal VOC 2012")
	plt.show()







