'''
Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

Notes:

Only lower case letters will be used (a-z). No punctuation or digits will be included.
Performance needs to be considered.

Examples
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
'''


def scramble(str1, str2):
        
    set1 = set(str1)
    list2 = list(str2)
    
    list3 = []
    
    for char2 in list2: 
        for char1 in set1:
            if char2 == char1:
                print("match")
                list3.append(char1)

    print(list2)
    print(list3)
    if str(list2) == str(list3):
        return True
    else:
        return False    
    

print(scramble('rkqodlw', 'world'))
print(scramble('katas', 'steak'))
print(scramble('cedewaraaossoqqyt', 'codewars') )
print(scramble("gkyswsqovjubv","gbkwovbjy"))

s1 = ""
s2 = "": True should equal Fals
      

from collections import Counter

def scramble2(str1, str2):
    # Count the frequency of each character in str1 and str2
    count_str1 = Counter(str1)
    count_str2 = Counter(str2)
    
    print(count_str1)
    print(count_str2)
    
    # Check if str1 has enough of each character needed for str2
    for char, count in count_str2.items():
        if count_str1[char] < count:
            return False
    return True

print(scramble2("gkyswsqovjubv","gbkwovbjy"))