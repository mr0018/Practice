'''
Challenge #7:
Given a string of lowercase and uppercase alpha characters, write a function
that returns a string where each character repeats in an increasing pattern,
starting at 1. Each character repetition starts with a capital letter and the
rest of the repeated characters are lowercase. Each repetition segment is
separated by a `-` character.
Examples:
- repeat_it("abcd") -> "A-Bb-Ccc-Dddd"
- repeat_it("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
- repeat_it("cwAt") -> "C-Ww-Aaa-Tttt"
def repeat_it(input_str):
'''
def repeat_it(Str):
    p=[]
    c=1
    for i in Str:
        p.append(i*c)
        c=c+1
##    return (' '.join(p))
    p1=('-'.join(p))
    return p1.title()
print(repeat_it("abcd"))
print(repeat_it("RqaEzty"))
print(repeat_it("cwAt"))
