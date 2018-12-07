import numpy as np
import collections
import re
import itertools

def max_finite(step_filepath):
	with open(step_filepath) as f:
		content = f.readlines()
	content=[x.strip() for x in content]
	content_array = list([x.split(', ') for x in content])
	#content_array=[(1,1),(1,6),(8,3),(3,4),(5,5),(8,9)]
	content_array=[(int(a[0]),int(a[1])) for a in content_array]
	x = [a[0] for a in content_array]
	y = [a[1] for a in content_array]
	tuples=list(itertools.product(range(min(x)-2, max(x)+2), range(min(y)-2, max(y)+2)))
	infinite_list=[]
	agg_list=[]
	for tup in tuples:
		values=[abs(tup[0]-coord[0])+abs(tup[1]-coord[1]) for coord in content_array]
		if values.count(min(values))==1:
			agg_list.append(values.index(min(values)))
		else:
			agg_list.append(None)
		if (tup[0] in [min(x)-1,max(x)+1] or tup[1] in [min(y)-1,max(y)+1]):
			infinite_list.append(values.index(min(values)))
	agg_list_non_infinite = [x for x in agg_list if x not in infinite_list]
	return max(collections.Counter(agg_list_non_infinite).values())


max_finite('data/day6.txt')

def safe_region(step_filepath):
	with open(step_filepath) as f:
		content = f.readlines()
	content=[x.strip() for x in content]
	content_array = list([x.split(', ') for x in content])
	#content_array=[(1,1),(1,6),(8,3),(3,4),(5,5),(8,9)]
	content_array=[(int(a[0]),int(a[1])) for a in content_array]
	x = [a[0] for a in content_array]
	y = [a[1] for a in content_array]
	tuples=list(itertools.product(range(min(x)-2, max(x)+2), range(min(y)-2, max(y)+2)))
	safe_list=[]
	for tup in tuples:
		values=[abs(tup[0]-coord[0])+abs(tup[1]-coord[1]) for coord in content_array]
		value_sum=sum(values)
		if value_sum<10000:
			safe_list.append(tup)
	return len(safe_list)


safe_region('data/day6.txt')




#not 3920