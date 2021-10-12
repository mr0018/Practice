'''
Challenge #6:
Return the number (count) of vowels in the given string.
We will consider `a, e, i, o, u as vowels for this challenge (but not y).
The input string will only consist of lower case letters and/or spaces.
def get_count(input_str):
'''
def get_count(input_str):
    Count=0
    New_Str = input_str.lower()
    for i in New_Str:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            Count +=1
    return Count
print(get_count(input("Enter String: ")))
