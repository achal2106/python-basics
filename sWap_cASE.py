# https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true

def swap_case(s):
    result=''
    for char in s:
        if char.isupper():
            result+=char.lower()
        elif char.islower():
            result+=char.upper()
        else:
            result+=char    
    return result