'''
Challenge #11:
You are given a non-empty list of words., 
Write a function that returns the *k* most frequent elements.
The list that you return should be sorted by frequency from highest to 
lowest. If two words have the same frequency, then the word with the lower 
alphabetical order should come first.
Example 1:
Input:
words = ["lambda", "school", "rules", "lambda", "school", "rocks"]
k = 2
Output:
["lambda", "school"]
Explanation:
"lambda" and "school" are the two most frequent words.
Example 2:
Input:
words = ["the", "sky", "is", "cloudy", "the", "the", "the", "cloudy", "is", "is"]
k = 4
Output:
["the", "is", "cloudy", "sky"]
Explanation: 
"the", "is", "cloudy", and "sky" are the four most frequent words. The words
are sorted from highest frequency to lowest.
Notes:
- `k` is always valid: `1 <= k <= number of unique elements.
- words in the input list only contain lowercase letters.
'''
