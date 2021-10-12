'''
Challenge #9:
Given a string, write a function that returns the "middle" character of the
Word. If the word has an odd length, return the single middle character. If 
the word has an even length, return the middle two characters.
Examples:
- get_middle("test") -> "es"
- get_middle("testing") -> "t"
- get_middle("middle") -> "dd"
- get_middle("A") -> "A"
def get_middle(input_str):
'''
def get_middle(s):
    if len(s)%2==0:
        return s[((len(s)//2)-1):((len(s)//2)+1)]
    return s[len(s)//2]
print(get_middle("test"))
print(get_middle("testing"))
print(get_middle("middle"))
print(get_middle("A"))

