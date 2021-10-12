'''
Challenge #10:
Given a string of space separated integers, write a function that returns the
maximum and minimum integers.
Example:
- max_and_min("1 2 3 4 5") -> "5 1"
- max_and_min("1 2 -3 4 5") -> "5 -3"
- max_and_min("1 9 3 4 -5") -> "9 -5"
Notes:
- All inputs are valid integers.
- There will always be at least one number in the input string.
- The return string must be two numbers separated by a single space, and 
the maximum number is first.
def max_and_min(input_str):
'''
def max_and_min(s):
    s1=s.split()
    s2=sorted(s1)
    l=s2[-1],s2[0]
    return (' '.join(l))
print(max_and_min("6 7 1 2 3 4 5"))
