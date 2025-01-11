
'''
Task
Your task is to write a function which returns the n-th term of the following series, which is the sum of the first n terms of the sequence (n is the input parameter).

https://www.codewars.com/kata/555eded1ad94b00403000071/train/python

You will need to figure out the rule of the series to complete this.

Rules
You need to round the answer to 2 decimal places and return it as String.

If the given value is 0 then it should return "0.00".

You will only be given Natural Numbers as arguments.

'''

def series_sum(n):
    
    # Happy Coding ^_^
    sum = 0.0
    last = 1
    
    for i in range(1,n+1):
        num = last
        sum += 1/num
        last += 3

    return f"{num:.2f}"

print(series_sum(1))


### Best practices 

'''
def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))
'''

'''
def series_sum(n):
    sum = 0
    for i in range(1, n * 3, 3):
        sum += 1 / i
    return "{:.2f}".format(sum)
'''