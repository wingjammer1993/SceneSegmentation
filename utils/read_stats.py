import re
import numpy as np
import matplotlib.pyplot as plt


def get_stats(file_text):
	dict_hue = {}
	elem = 0
	for line in file_text:
		if re.search('hue_value', line):
			k = line.split()
			elem = float(k[7].split("=")[-1].strip(','))
			dict_hue[elem] = 0
		if re.search('Mean', line):
			m = line.split()
			dict_hue[elem] = float(m[-1])
	return dict_hue


if __name__ == '__main__':
	filename = "enet-hue-job.1287986.out"
	file = open(filename)
	output = get_stats(file)
	plt.bar(list(output.keys()), list(output.values()))
	plt.axhline(y=0.3, color='r', linestyle='dotted')
	plt.xlabel("+/- hue variation")
	plt.ylabel("Mean IoU")
	plt.title("ENet + CamVid")
	plt.show()







