def solution(args):
    
    # Range Extraction

    '''
    
    https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/python
    
    A format for expressing an ordered list of integers is to use a comma separated list of either

    individual integers or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
    Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.
    
    Example:

    solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
    # returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
    
    The idea is
    1. prepare two variables to store the number for the beginning and the end
        beg will stay until we find the end
        end starts with list[0] and will move one by one for each loop 
        n start with list[1] and will move in the loop 
    2. loop though the list until we find the end of the consecutive number
        end will move one by one -> assign n to end
        check if n != end + 1 
    3. Three conditions 
        2.1 - case 1: beg == end, we have 1 consecutive number
        2.2 - case 2: beg == end +1, we have 2 consecutive number
        2.3 - case 3: else, we have 3 or more consecutive number
    
    
    '''
    
    if not args:
        return ""                      # Return empty string for empty input

    result = []
    beg = end = args[0]               # Initialize start and end of the current range

    for n in args[1:] + [None]:       # Loop through rest of args + sentinel for flush
        if n != end + 1:              # If not consecutive, close the current range
            if end == beg:
                result.append(str(beg))                   # Single number
            elif end == beg + 1:
                result.extend([str(beg), str(end)])       # Two separate numbers
            else:
                result.append(f"{beg}-{end}")             # A range (3 or more)
            beg = n                      # Start a new range
        end = n                          # Move end forward (even if range continues)

    return ",".join(result)             # Join all parts into final output string


numbers = [-3,-2,-1,2,10,15,16,18,19,20]
output = solution(numbers)
print(output)