
import numpy as np
import collections


def count_letters(id_filepath):
	with open(id_filepath) as f:
		content = f.readlines()
	content=[x.strip() for x in content]
	letters = [collections.Counter(x) for x in content]
	twos = [int(len({x : m[x] for x in m if m[x] == 2 })>0) for m in letters]
	threes = [int(len({x : m[x] for x in m if m[x] == 3 })>0) for m in letters]
	return sum(twos)*sum(threes)

count_letters('data/day2.txt')

