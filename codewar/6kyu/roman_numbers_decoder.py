'''
Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer. 
You don't need to validate the form of the Roman numeral.

Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately, 
starting with the leftmost digit and skipping any 0s. So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) 
and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII). 
The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.

Example:
"MM"      -> 2000
"MDCLXVI" -> 1666
"M"       -> 1000
"CD"      ->  400
"XC"      ->   90
"XL"      ->   40
"I"       ->    1
Help:
Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000
'''

def solution(roman : str) -> int:
    """complete the solution by transforming the roman numeral into an integer"""
    
    roman_dict = {"I":1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    
    # Reverse Order 
    letters = list(roman)[::-1]

    prev_value = 0
    current_value = 0
    
    final = 0
    
    for letter in letters:
        if letter in roman_dict:
            current_value = roman_dict[letter]    
            if current_value >= prev_value:
               final += current_value
            else:
                final -= current_value
        else:
            print("invalid")
            break

        prev_value = current_value       
    return final

print(solution('MM'))
print(solution('MDCLXVI'))
print(solution("MMMDCCCLXXXVIII"))




