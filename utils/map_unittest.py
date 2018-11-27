import cv2
import numpy as np

colors = [  # [  0,   0,   0],
	[128, 64, 128],
	[244, 35, 232],
	[70, 70, 70],
	[102, 102, 156],
	[190, 153, 153],
	[153, 153, 153],
	[250, 170, 30],
	[220, 220, 0],
	[107, 142, 35],
	[152, 251, 152],
	[0, 130, 180],
	[220, 20, 60],
	[255, 0, 0],
	[0, 0, 142],
	[0, 0, 70],
	[0, 60, 100],
	[0, 80, 100],
	[0, 0, 230],
	[119, 11, 32],
]

label_colours = dict(zip(range(19), colors))

void_classes = [0, 1, 2, 3, 4, 5, 6, 9, 10, 14, 15, 16, 18, 29, 30, -1]
valid_classes = [
	7,
	8,
	11,
	12,
	13,
	17,
	19,
	20,
	21,
	22,
	23,
	24,
	25,
	26,
	27,
	28,
	31,
	32,
	33,
]
class_names = [
	"unlabelled",
	"road",
	"sidewalk",
	"building",
	"wall",
	"fence",
	"pole",
	"traffic_light",
	"traffic_sign",
	"vegetation",
	"terrain",
	"sky",
	"person",
	"rider",
	"car",
	"truck",
	"bus",
	"train",
	"motorcycle",
	"bicycle",
]

ignore_index = 250
class_map = dict(zip(valid_classes, range(19)))


def encode_segmap(mask):
	# Put all void classes to zero
	for _voidc in void_classes:
		mask[mask == _voidc] = ignore_index
	for _validc in valid_classes:
		mask[mask == _validc] = class_map[_validc]
	return mask


def decode_segmap(temp):
	r = temp.copy()
	g = temp.copy()
	b = temp.copy()
	for l in range(0, 19):
		r[temp == l] = label_colours[l][0]
		g[temp == l] = label_colours[l][1]
		b[temp == l] = label_colours[l][2]

	rgb = np.zeros((temp.shape[0], temp.shape[1], 3))
	rgb[:, :, 2] = r
	rgb[:, :, 1] = g
	rgb[:, :, 0] = b
	return rgb


def unit_test():
	img = cv2.imread(r"C:\Users\Amruta\Desktop\Project\Datasets\Mapillary\validation\labels\-BYnT4s40fJHAlOumPYbyQ.png")
	mask = encode_segmap(img[:, :, 0])
	rgd = decode_segmap(mask)
	cv2.imwrite("new.png", rgd)
	print("done")

if __name__ == '__main__':
	unit_test()