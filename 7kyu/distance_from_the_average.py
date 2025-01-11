''''
Input: a list
Output:

Calculate:
    sum of the list
    average of the list 
    difference for each element against the average
    add it to a new list
    return it

'''

def distances_from_average(test_list):
    average = sum(test_list) / len(test_list)
    return [round(average -x,2) for x in test_list]     

### Best Practice
'''

from numpy import mean
def distances_from_average(test_list):
    avg = mean(test_list)
    return [round(avg - x, 2) for x in test_list]
    
    
def distances_from_average(test_list):
    avg = sum(test_list)/len(test_list)
    return list(map(lambda x: round(avg - x, 2), test_list))
    
     
def distances_from_average(lst):
    average = sum(lst) / len(lst)
    return [round(average - n, 2) for n in lst]


'''