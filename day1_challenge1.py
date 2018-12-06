
import numpy as np

def resulting_frequency(frequency_change_filepath, starting_frequency_int=0):
	with open(frequency_change_filepath) as f:
		content = f.readlines()
	content = [starting_frequency_int] + [int(x.strip()) for x in content]
	return(sum(content))

resulting_frequency('data/day1_challenge1.txt',0)

def first_duplicate(frequency_change_filepath, starting_frequency_int=0):
	with open(frequency_change_filepath) as f:
		content = f.readlines()
	content = [int(x.strip()) for x in content]
	cumsum = np.cumsum([starting_frequency_int] + content)
	cumsum_size=len(cumsum)
	while(len(cumsum)==len(set(cumsum))): #while there are no duplicates
		old_cumsum=cumsum
		new_cumsum=np.cumsum([cumsum[-1]] + content)[1:cumsum_size] #calculate more cumulative sums
		cumsum=np.concatenate([cumsum,new_cumsum])
	return [x for x in new_cumsum if x in old_cumsum][0]


first_duplicate('data/day1_challenge1.txt',0)

