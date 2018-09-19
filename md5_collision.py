import hashlib
import numpy as np
import os


def slayer_six():
	hash_str = {}
	flag = 1
	while flag:
		num = np.random.randint(50, 10000)
		istr = os.urandom(num)
		md5hash = hashlib.md5(istr).hexdigest()
		slayer = md5hash[0:6] + md5hash[-6:]
		if slayer in hash_str:
			print(md5hash)
			print(slayer)
			print(hash_str[slayer])
			print(istr)
			if hash_str[slayer] != istr:
				flag = 0
				print("slayer-6 found")
		else:
			hash_str[slayer] = istr


if __name__ == '__main__':
	slayer_six()

