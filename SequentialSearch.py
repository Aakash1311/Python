sequential search 
def ss(number_list,n):
	found = False
	for i in number_list:
		if i==n:
			found = True
			break
	return found

numbers  =range(1,300)	
result =ss(numbers,205)
print(result)		