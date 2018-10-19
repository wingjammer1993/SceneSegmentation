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
	if ip_string == 'hue':
		dict_hue[0] = 0.36
	else:
		dict_hue[1] = 0.36
	return dict_hue


if __name__ == '__main__':
	filename = "semseg-val-job.1335752.out"
	for k in default:
		file = open(filename)
		output = get_stats(k, file)
		new_x, new_y = zip(*sorted(zip(list(output.keys()), list(output.values()))))
		plt.plot(new_x, new_y, label='mIOU on modified val set')
		plt.plot(new_x, new_y, 'g.')
		plt.ylim(0, 0.6)
		plt.xticks(new_x)
		plt.axhline(y=0.36, color='r', linestyle='dotted', label='default mIOU on val set')
		plt.xlabel(k)
		plt.ylabel("Mean IoU")
		plt.title("DeepLab - mIOU vs. {} value".format(k))
		plt.legend()
		plt.show()







