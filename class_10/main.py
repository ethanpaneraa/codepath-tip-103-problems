print("CodePath TIP 103 Summer 2024 Session 10")
print("\n")


'''

Week 10, Session 1 Problems

Problem 1: Longest Consqutive Sequence

U - Understand:

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence. The algorithm must run in O(n) time.

Examples:
Example 1:

Input: nums = [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore, its length is 4.
Example 2:

Input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
Output: 9
Explanation: The longest consecutive elements sequence is [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]. Therefore, its length is 9.

M - Match:

This problem can be matched to the use of a hash set to keep track of the elements in the array and find the longest consecutive sequence efficiently.

P - Plan:

Convert the list nums to a set num_set to allow O(1) lookups.
Initialize a variable longest_streak to keep track of the longest consecutive sequence.
Iterate through each number in nums:
If the number is the start of a sequence (i.e., num - 1 is not in num_set), initialize current_num to this number and current_streak to 1.
Increment current_num and current_streak as long as current_num + 1 is in num_set.
Update longest_streak with the maximum value between longest_streak and current_streak.
Return longest_streak.

R - Review:

Ensure the approach correctly identifies the start of sequences and counts the consecutive numbers.
Verify edge cases such as an empty array or an array with no consecutive numbers.

E - Evaluate:

Time complexity: O(n) because each element is processed once.
Space complexity: O(n) for the hash set.

'''

def longest_consecutive(nums):
    if not nums:
        return 0

    num_set = set(nums)
    longest_streak = 0

    for num in nums:
        if num - 1 not in num_set:  # Check if it's the start of a sequence
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak


# Test cases
longest_consecutive_test_cases = [
    [[100, 4, 200, 1, 3, 2], 4],
    [[0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9],
]

for nums, expected in longest_consecutive_test_cases:
    result = longest_consecutive(nums)
    assert result == expected, f"For {nums}, expected {expected} but got {result}"

'''

Problem 2: Best Time to Buy and Sell Stock II

U - Understand:

Given an integer array prices where prices[i] is the price of a given stock on the i-th day, find the maximum profit you can achieve. You can buy and sell on the same day and hold at most one share at any time.

Examples:
Example 1:

Input: prices = [7, 1, 5, 3, 6, 4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5 - 1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6 - 3 = 3.
Total profit is 4 + 3 = 7.
Example 2:

Input: prices = [1, 2, 3, 4, 5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5 - 1 = 4.
Total profit is 4.
Example 3:

Input: prices = [7, 6, 4, 3, 1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.

M - Match:

This problem can be matched to a greedy approach where we sum up all the positive differences between consecutive days.

P - Plan:

Initialize max_profit to 0.
Iterate through the prices array from the second day to the last day.
For each day, if the price of the current day is greater than the price of the previous day, add the difference to max_profit.
Return max_profit.

R - Review:

Ensure the approach correctly sums all the positive differences between consecutive days.
Verify edge cases such as an array with one or no prices, or where prices only decrease.

E - Evaluate:

Time complexity: O(n) where n is the number of days.
Space complexity: O(1) since we are using a constant amount of extra space.

'''

def max_profit(prices):
    max_profit = 0
    
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            max_profit += prices[i] - prices[i - 1]
    
    return max_profit


# Test cases
max_profit_test_cases = [
    [[7, 1, 5, 3, 6, 4], 7],
    [[1, 2, 3, 4, 5], 4],
    [[7, 6, 4, 3, 1], 0],
]

for prices, expected in max_profit_test_cases:
    result = max_profit(prices)
    assert result == expected, f"For {prices}, expected {expected} but got {result}"


print("### END OF WEEK 10, SESSION 1 ###")
print("### END OF CODEPATH TIP 103 SUMMER 2024 ###")