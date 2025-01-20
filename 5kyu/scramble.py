from collections import Counter

def scramble(s1, s2):
    
    '''
    checkers = list(s1.lower())
    checked = list(s2.lower())
    
    result = []
    
    for checked_char in checked: 
        for checker_char in checkers:
            if checked_char == checker_char:
                result.append(checker_char)
                checkers.remove(checker_char)
                break

    print(checked)
    print(result)

    if str(checked) == str(result):
        return True
    else:
        return False    
    
    '''
    
    # Count the frequency of each character in s1 and s2
    count_s1 = Counter(s1)
    count_s2 = Counter(s2)
    
    print(count_s1)
    print(count_s2)
    
    # Check if s1 has enough of each character to match s2
    return all(count_s1[char] >= count_s2[char] for char in count_s2)


    
print(scramble('rkqodlw', 'world')) # ==> True
print(scramble('cedewaraaossoqqyt', 'codewars'))#  ==> True
print(scramble('katas', 'steak')) # ==> False

print(scramble("qeapkriwwijlura","lipkuwuwq")) 
