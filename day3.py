import numpy as np
import collections
import re
import itertools


def get_data(x):
	edge_distance = [int(a) for a in re.search(r"@ (.*):", x).group(1).split(',')]
	dimension = [int(a) for a in re.search(r": (.*)", x).group(1).split('x')]
	row = [i for i in range(edge_distance[0],edge_distance[0]+dimension[0])]
	col = [i for i in range(edge_distance[1],edge_distance[1]+dimension[1])]
	product = list(itertools.product(row, col))
	return product

def overlaps(claim_filepath):
	with open(claim_filepath) as f:
		content = f.readlines()
	content=[x.strip() for x in content]
	content_array = list([get_data(x) for x in content])
	content_array_unnested=list(itertools.chain(*content_array))
	num_duplicated=[x for x in list(collections.Counter(content_array_unnested).values()) if x>1]
	return len(num_duplicated)

a = overlaps('data/day3.txt')