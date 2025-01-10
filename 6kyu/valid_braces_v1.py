def is_match(current,prev):
  if prev == '(' and current == ')':
    return True 
  elif prev == '[' and current == ']':
    return True
  elif prev == '{' and current == '}':
    return True
  else:
    return False
  
def is_odd_length(string):
  return len(string) % 2 == 1
  
def valid_braces(string):
  
  stack = []

  # if a pair-able combination is missing 
  if is_odd_length(string):
    # print("Fail")
    return False

  # Check the sequences of braces 
  for n in string:

    if n in {"(","[","{"}:
      stack.append(n)

    if n in {")","]","}"}:
      if not stack:
        return False
      prev = stack.pop() 
      if not is_match(n,prev):
        return False
  
  # only a one brace is provided in the pair
  if len(stack) > 1:
    return False
      
  return True