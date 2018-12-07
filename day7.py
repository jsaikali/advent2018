import numpy as np
import collections
import re
import itertools

## Part 1

def get_data(x):
	first = [a for a in re.search(r"Step (.*) must", x).group(1)]
	second = [a for a in re.search(r"step (.*) can", x).group(1)]
	return first+second

def inefficient_loop(r_dict,all_letters,last_step):
	while(len(all_letters)>0):
		recent_candidates=[]
		for key,value in r_dict.items():
			if last_step in value:
				value.remove(last_step)
				r_dict.update({key:value})
				if len(r_dict[key])==0:
					recent_candidates.append(key)
		for item in recent_candidates:
			deleted=r_dict.pop(item,None)
		candidates=sorted([x for x in all_letters if x not in r_dict.keys()],reverse=True)
		next_step=candidates.pop()
		all_letters.remove(next_step)
		last_step=next_step
		#print(next_step)

def dependencies(step_filepath):
	with open(step_filepath) as f:
		content = f.readlines()
	content=[x.strip() for x in content]
	content_array = list([get_data(x) for x in content])
	result = {}
	for item in content_array: #create list of dependencies per letter
		result.setdefault(item[1], []).append(item[0])
	all_letters=list(set(itertools.chain(*content_array)))
	candidates=sorted([x for x in all_letters if x not in result.keys()],reverse=True)
	print(candidates)
	first_step=candidates.pop()
	all_letters.remove(first_step)
	#print(first_step)
	inefficient_loop(result,all_letters,first_step)
	return result

dependencies('data/day7_test.txt')

## Part 2

def inefficient_loop_5(r_dict,all_letters):
	total_time_elapsed=0
	workers = [0,0,0,0,0]
	working_on = [None,None,None,None,None]
	done_letters=[]
	while(len(done_letters)<26):
		for i in range(5):
			if (workers[i]<=0):
				if working_on[i]!=None:
					last_step=working_on[i]
					done_letters.append(last_step)
					popping=[]
					for key,value in r_dict.items():
						if last_step in value:
							value.remove(last_step)
							r_dict.update({key:value})
							if len(r_dict[key])==0:
								popping.append(key)
					for item in popping:
						deleted=r_dict.pop(item,None)
				candidates=sorted([x for x in all_letters if x not in r_dict.keys()],reverse=True)
				if len(candidates)==0:
					next_step=None
					working_on[i]=next_step
					workers[i]=0
				else:
					next_step=candidates.pop()
					all_letters.remove(next_step)
					working_on[i]=next_step
					workers[i]=60 + ord(next_step.lower()) - 96
		if(len([x for x in all_letters if x not in r_dict.keys()])==0 or len([x for x in working_on if x==None])==0):
			workers=[x-1 for x in workers]
			print(str(total_time_elapsed)+str(working_on))
			total_time_elapsed=total_time_elapsed+1		
	return total_time_elapsed

def dependencies_5(step_filepath):
	with open(step_filepath) as f:
		content = f.readlines()
	content=[x.strip() for x in content]
	content_array = list([get_data(x) for x in content])
	result = {}
	for item in content_array: #create list of dependencies per letter
		result.setdefault(item[1], []).append(item[0])
	all_letters=list(set(itertools.chain(*content_array)))
	print(result)
	#candidates=sorted([x for x in all_letters if x not in result.keys()],reverse=True)
	#print(candidates)
	#print(first_step)
	total_time=inefficient_loop_5(result,all_letters)
	return total_time

dependencies_5('data/day7.txt')

