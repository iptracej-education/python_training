def valid_braces(string):
    
    stack = []
    pair ={
        ']': '[',
        '}': '{', 
        ')': '(',}
    
    for char in string:
        if char in '[{(':
            print(char)
            stack.append(char)
        if char in ']})':
            print(char)
            if len(stack) == 0:
                return False
            
            top_of_stack = stack.pop()
            if pair[char] != top_of_stack:
                return False

    return not stack