print("Ethan Pineda")
print("\n")
'''
Session 1, June 5th 2024 Problems 1 & 2 Solutions
'''

# PROBLEM 1
'''
Write a function that takes in two strings and returns True if the second string is a substring of the first, and False otherwise.

NOTE: You may not use the in operator (Python) or call a library function that tests for substrings, such as substring() or indexOf() (Java).


Examples:

Input: laboratory, rat
Output: true

Example 2:
Input: cat, meow
Output: false

UMPIRE Method:

U - Understand

- What happens when both inputs are empty strings?
- What should happen if the second string is longer than the first one? 

Example 1:
Input: laboratory, rat
Output: true

Example 2:
Input: cat, meow
Output: false

M - Match

- Since this is a string problem, this is most likely going to involve solving using two pointers
- The most trival solution is to use a nested for-loop to iterate through the first string and check if the second string is a substring of the first string

- Another solution is to use a hashmap to store the characters of the first string and then use a nested for-loop

P - Plan

- Start off by creating by iterating through the first string
- Every iteration, check if the current character matches the first character of the second string
- If it does, then check if the rest of the second string matches the rest of the first string

R - Review

- Test cases:
- Input: laboratory, rat
Output: true

- Input: cat, meow
Output: false

- Input: cat, cat
Output: true

E - Evaluate
- Time complexity: O(n * m) - where n is the length of the first string and m is the length of the second stringe
- Space complexity: O(1) 
'''


def is_substring(str_1, str_2):
  # base case 1: if the second string is empty, return True
  if len(str_2) > len(str_1):
    return False
  # base case 2: if the second string is longer than the first string, return False
  if len(str_2) == 0:
    return True
  # base case 3: if the first string is empty, return False
  if len(str_1) == 0:
    return False

  # flag to keep track of whether the second string is a substring of the first string
  is_substring = False

  # iterate through the first string
  for i in range(len(str_1)):
    # check if the current character matches the first character of the second string
    if str_1[i] == str_2[0]:
      # if we found a matching character, check if the rest of the second string matches the rest of the first string
      j = 0
      while i < len(str_1):
        # if j is equal to the length of the second string, then we have found a substring
        if j == len(str_2) - 1:
          is_substring = True
          break
        if str_1[i] == str_2[j]:
          i += 1
          j += 1
        else:
          break

  return is_substring

print("*** Is Substring ***")
test_cases_is_substring = [
    ("laboratory", "rat"),  # True
    ("cat", "meow"),  # False
    ("hi", "Hello"),  # False
    ("brianna", "anna"),  # True
    ("cat", "cat")  # True
]   

for str_1, str_2 in test_cases_is_substring:
  print(f"Input: {str_1}, {str_2}")
  print(f"Output: {is_substring(str_1, str_2)}")

# PROBLEM 2
'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string: "". 

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

U - Understand

- What should happen if the input array is empty?
- What should happen if the input array contains only one string?
- What should happen if the input array contains only empty strings?


M - Match

- since we need to find the longest common prefix, we are probably going to need to use two pointers

P - Plan

- create a variable to store the longest common prefix
- access the first string in the array
- loop through the rest of the strings in the array
- compare the characters of the current string with the characters of the first string
- if there's a mismatch, then we can return the longest common prefix
- otherwise, we can update the longest common prefix

R - Review

- Test cases:
- Input: strs = ["flower","flow","flight"]
Output: "fl"

- Input: strs = ["dog","racecar","car"]
Output: ""

- Input: strs = ["hi", "Hello"]
Output: ""

- Input: strs = ["brianna", "anna"]
Output: "a"

- Input: strs = ["cat", "cat"]
Output: "cat"

E - Evaluate    

- Time complexity: O(n * m) - where n is the length of the array and m is the length of the longest string
- Space complexity: O(1)

'''

def longest_common_prefix(strs):
  
  if len(strs) == 0:
    return strs[0]

  longest_prefix = ""

  first_string = strs[0]
  current_prefix = ""
  
  for string in strs[1:]:
    for i in range(len(first_string)):
      # check if the current character matches the character in the first string
      if i < len(string) and first_string[i] == string[i]:
        current_prefix += first_string[i]
      else:
        # if not, then we need to break out of the loop
        break
    # if the current prefix is empty, then there is no common prefix
    if len(current_prefix) == 0:
      return ""
    # if the current prefix is shorter than the longest prefix, then update the longest prefix
    if len(current_prefix) < len(longest_prefix) or longest_prefix == "":
      longest_prefix = current_prefix
    current_prefix = ""

  return longest_prefix

print("*** Longest Common Prefix ***")
test_cases_longest_common_prefix = [
    (["flower", "flow", "flight"], "fl"),
    (["dog", "racecar", "car"], ""), 
    (["hi", "Hello"], ""),
    (["brianna", "anna"], "a"),
    (["cat", "cat"], "cat") 
]

for strs, expected in test_cases_longest_common_prefix:
  print(f"Input: {strs}")
  print(f"Output: {longest_common_prefix(strs)}")

print("*** END OF SESSION 1 ***")

print("*** START OF SESSION 2 ***")

# PROBLEM 1

'''
Given a positive integer n, you can apply one of the following operations:

If n is even, replace n with n / 2.
If n is odd, replace n with either n + 1 or n - 1.
Return the minimum number of operations needed for n to become 1.
Tip: Java programmers should treat Integer.MAX_VALUE() as a special case.

Example 1:
Input: n = 8
Output: 3
Explanation: 8 -> 4 -> 2 -> 1

Example 2:
Input: n = 7
Output: 4
Explanation: 7 -> 8 -> 4 -> 2 -> 1
or 7 -> 6 -> 3 -> 2 -> 1

Example 3:
Input: n = 4
Output: 2

U - Understand

- What should happen if the input is less than 1?
- What should happen if the input is equal to 1?
- What should happen if the input is equal to 2?

M - Match

- This could be a problem that can be solved using recursion
- Or, we can use a while loop to keep track of the number of operations needed to reach 1
- So this is a problem that can be solved using dynamic programming

P - Plan

- I want to use a helper function to keep track of the number of operations
- If n is equal to 1, then return the number of operations
- If n is even, then divide n by 2 and increment the number of operations by 1
- If n is odd, then we can either add 1 or subtract 1 from n
- We can then return the minimum of the two options
- We can then call the helper function with the input n and 0 as the number of operations

R - Review

- Test cases:
- Input: 8
Output: 3

- Input: 7
Output: 4

- Input: 4
Output: 2

- Input: 1
Output: 0

- Input: 2
Output: 1

E - Evaluate

- Time complexity: O(log n)
- Space complexity: O(1)
'''

def integer_replacement(n):
  num_operations = 0

  # helper function to keep track of the number of operations
  def helper(n, num_operations):
    # base case: if n is equal to 1, then return the number of operations
    if n == 1:
      return num_operations
    # if n is even, then divide n by 2 and increment the number of operations by 1
    if n % 2 == 0:
      return helper(n // 2, num_operations + 1)
    # if n is odd, then we can either add 1 or subtract 1 from n and return the minimum of the two options
    else:
      return min(helper(n + 1, num_operations + 1), helper(n - 1, num_operations + 1))

  return helper(n, num_operations)


print("*** Integer Replacement ***")
test_cases_integer_replacement = [
    (8, 3),
    (7, 4),
    (4, 2),
    (1, 0),
    (2, 1)
]

for n, expected in test_cases_integer_replacement:
  print(f"Input: {n}")
  print(f"Output: {integer_replacement(n)}")

# PROBLEM 2

'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol Value I 1 V 5 X 10 L 50 C 100 D 500 M 1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. X can be placed before L (50) and C (100) to make 40 and 90. C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

U - Understand

- What should happen if the input is an empty string?
- What should happen if the input is not a valid Roman numeral?

M - Match

- This is a problem that can be solved using a hashmap
- and since there's a predefined set of roman numerals, we can use a hashmap to store the values of each roman numeral

P - Plan
- create a hashmap to store the values of each roman numeral
- create a variable to store the result
- iterate through the input string
- each iteration, we should check if the current roman numeral is less than the next roman numeral
- if it is, then we should subtract the current roman numeral from the result
- otherwise, we should add the current roman numeral to the result
- we should pay attention to the three special cases where subtraction is used
- return the result

R - Review

- Test cases:
- Input: "III"
Output: 3

- Input: "LVIII"
Output: 58

- Input: "MCMXCIV"
Output: 1994

E - Evaluate

- Time complexity: O(n) - where n is the length of the input string
- Space complexity: O(1)

'''

def roman_to_int(s):
  final_int = 0

  roman_numerals = {
    "I": 1,
    "V": 5, 
    "X": 10, 
    "L": 50, 
    "C": 100,
    "D": 500,
    "M": 1000
  }

  for i in range(len(s)):
    if i + 1 < len(s):
        # compare the ASCII values of the current roman numeral and the next roman numeral
        if roman_numerals[s[i]] < roman_numerals[s[i + 1]]:
            final_int -= roman_numerals[s[i]]
        else:
            # if the current roman numeral is greater than or equal to the next roman numeral, then add the current roman numeral to the result
            final_int += roman_numerals[s[i]]

    else:
        final_int += roman_numerals[s[i]]

  return final_int

print("*** Roman to Integer ***")#
test_cases_roman_to_int = [
    ("III", 3),
    ("LVIII", 58),
    ("MCMXCIV", 1994),
    ("IV", 4),
    ("IX", 9),
    ("XL", 40),
    ("XC", 90),
    ("CD", 400),
    ("CM", 900),
]

for s, expected in test_cases_roman_to_int:
  print(f"Input: {s}")
  print(f"Output: {roman_to_int(s)}")

print("*** END OF SESSION 2 ***")


print("*** END OF WEEK 1 ***")