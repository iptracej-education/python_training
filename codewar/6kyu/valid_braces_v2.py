def valid_braces(string):
    
    stack = []
    pair ={']': '[','}': '{', ')': '(',}
    
    for char in string:
        if char in '[{(':
            print(char)
            stack.append(char)
        if char in ']})':
            if len(stack) == 0 or pair[char] != stack.pop():
                return False
    
    return not stack