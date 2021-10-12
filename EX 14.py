'''
Challenge #14:
Given a non-empty array of integers `nums`, every element appears twice 
except except for one. Write a function that finds the element that only 
appears once.
Examples:
- single_number([3,3,2]) -> 2
- single_number([5,2,3,2,3]) -> 5
- single_number([10]) -> 10
def single_number(nums):
'''
def single_number(nums):
    for i in nums:
        if nums.count(i)==1:
            return i
print(single_number([3,3,2]))
print(single_number([5,2,3,2,3]))
print(single_number([10]))
