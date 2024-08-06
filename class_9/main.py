print("CodePath TIP 103 Summer 2024 Session 9")
print("\n")

'''

Week 9, Session 1 Problems

U - Understand:

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words. The same word in the dictionary may be reused multiple times in the segmentation.

Examples:
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple". Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

M - Match:

This problem can be matched to dynamic programming (DP) where we can use a DP array to keep track of whether substrings of s can be segmented into dictionary words.

P - Plan:

Initialize a DP array dp where dp[i] is true if the substring s[0:i] can be segmented into dictionary words.
Set dp[0] to true because an empty string can always be segmented.
Iterate over the string s from 1 to len(s).
For each position i, check all possible substrings s[j:i] where 0 <= j < i.
If dp[j] is true and s[j:i] is in wordDict, set dp[i] to true.
Return dp[len(s)].
R - Review:

Ensure the DP array is correctly updated based on the presence of substrings in wordDict.
Verify the edge cases, such as an empty string or a string with no possible segmentations.
E - Evaluate:

Time complexity: O(n^2 * k) where n is the length of s and k is the maximum length of a word in wordDict.
Space complexity: O(n) for the DP array.

'''

def wordBreak(s, wordDict):
    n = len(s)
    dp = []
    dp.append(True)
    for i in range(1, n + 1):
        dp.append(False)
        for j in range(i):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break

    return dp[n]

# Test cases
wordBreak_test_cases = [
    ["leetcode", ["leet", "code"], True],
    ["applepenapple", ["apple", "pen"], True],
    ["catsandog", ["cats", "dog", "sand", "and", "cat"], False],
]

for s, wordDict, expected in wordBreak_test_cases:
    result = wordBreak(s, wordDict)
    assert result == expected, f"For {s} and {wordDict}, expected {expected} but got {result}"


'''

Problem 2: Longest Palindromic Substring

U - Understand:
Given a string s, return the longest palindromic substring in s.

Examples:
Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
M - Match:
This problem can be matched to dynamic programming (DP) or the expand-around-center approach to find the longest palindromic substring.

P - Plan:

We'll use the expand-around-center approach for its simplicity and efficiency.

Initialize variables to keep track of the start and end of the longest palindromic substring found.
Iterate over each character in the string, treating each character and the gap between each pair of characters as potential centers of a palindrome.
For each center, expand outward while the characters at the expanding edges are equal.
Update the start and end indices if a longer palindrome is found.
Return the substring from start to end indices.

R - Review:

Ensure the expand-around-center logic correctly identifies palindromes of both odd and even lengths.

Verify edge cases such as a single character string or no palindrome longer than one character.

E - Evaluate:

Time complexity: O(n^2) because we expand around each center and there are 2n-1 centers.
Space complexity: O(1) as we only use a few extra variables.

'''

def longest_palindromic_substring(s):
    if not s:
        return ""

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    start, end = 0, 0

    for i in range(len(s)):
        left1, right1 = expand_around_center(i, i)  # Odd length palindrome
        left2, right2 = expand_around_center(i, i + 1)  # Even length palindrome

        if right1 - left1 > end - start:
            start, end = left1, right1
        if right2 - left2 > end - start:
            start, end = left2, right2

    return s[start:end + 1]

# Test cases
longest_palindromic_substring_test_cases = [
    ["babad", "bab"],
    ["cbbd", "bb"],
]

for s, expected in longest_palindromic_substring_test_cases:
    result = longest_palindromic_substring(s)
    assert result == expected, f"For {s}, expected {expected} but got {result}"


print("### END OF WEEK 9, SESSION 1 ###")
print("\n")

'''

Week 9, Session 2 Problems

Problem 1: Generate Parentheses

U - Understand:

Given n pairs of parentheses, generate all combinations of well-formed parentheses.

Examples:
Example 1:

Input: n = 3
Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]
Example 2:

Input: n = 1
Output: ["()"]

M - Match:

This problem is well-matched to a backtracking approach where we generate the sequence step-by-step and ensure at each step that the generated sequence is valid.

P - Plan:

Define a helper function that takes the current sequence, the number of open parentheses used, and the number of close parentheses used.
If the current sequence length is 2 * n, add it to the results list.
If the number of open parentheses used is less than n, add an open parenthesis and recursively call the helper function.
If the number of close parentheses used is less than the number of open parentheses, add a close parenthesis and recursively call the helper function.
Return the results list.

R - Review:

Ensure the recursive approach correctly generates all valid combinations by maintaining the count of open and close parentheses.

E - Evaluate:

Time complexity: O(4^n / sqrt(n)), which is the number of valid parentheses combinations (Catalan number).
Space complexity: O(n) for the recursion stack.

'''


def generate_parenthesis(n):
    def backtrack(current, open_count, close_count):
        if len(current) == 2 * n:
            results.append(current)
            return
        
        if open_count < n:
            backtrack(current + "(", open_count + 1, close_count)
        if close_count < open_count:
            backtrack(current + ")", open_count, close_count + 1)

    results = []
    backtrack("", 0, 0)
    return results

# Test cases
generate_parenthesis_test_cases = [
    [3, ["((()))", "(()())", "(())()", "()(())", "()()()"]],
    [1, ["()"]],
]

for n, expected in generate_parenthesis_test_cases:
    result = generate_parenthesis(n)
    assert result == expected, f"For {n}, expected {expected} but got {result}"


'''

Problem 2: Subsets

U - Understand:

Given an array of unique elements, generate all possible subsets (the power set).

Examples:
Example 1:

Input: nums = [1, 2, 3]
Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
Example 2:

Input: nums = [0]
Output: [[], [0]]

M - Match:

This problem can be matched to a backtracking or iterative approach where we systematically explore all possible subsets.

P - Plan:

Initialize an empty list to hold the result.
Use a backtracking function that takes the current subset and the starting index.
At each step, add the current subset to the result.
Iterate over the elements starting from the current index, add the current element to the subset, and recursively call the backtracking function with the next index.
After the recursive call, remove the last element from the subset to backtrack.

R - Review:

Ensure the recursive approach correctly generates all subsets without duplicates.
Verify edge cases such as an empty array or an array with one element.

E - Evaluate:

Time complexity: O(2^n) since there are 2^n possible subsets for an array of length n.
Space complexity: O(n) for the recursion stack and the subsets being generated.

'''

def subsets(nums):
    def backtrack(start, current_subset):
        results.append(current_subset[:])
        
        for i in range(start, len(nums)):
            current_subset.append(nums[i])
            backtrack(i + 1, current_subset)
            current_subset.pop()

    results = []
    backtrack(0, [])
    return results


# Test cases
subsets_test_cases = [
    [[1, 2, 3], [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]],
    [[0], [[], [0]]],
]

for nums, expected in subsets_test_cases:
    result = subsets(nums)
    assert result == expected, f"For {nums}, expected {expected} but got {result}"

print("### END OF WEEK 9, SESSION 2 ###")

print('### END OF WEEK 9 ###')
