print("CodePath TIP 103 Summer 2024 Session 4")
print("\n")

'''

Week 3, Session 1 Problems

Problem 1: Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

U - Understand: 

- Given a list of integers, we are to determine how much water can be trapped after raining.
- The width of each bar is 1.
- What happens when the list is empty?
- What happens when the list contains only one element?

M - Match:M

- We can match this problem to the two-pointer approach.
- We can use two pointers to keep track of the left and right walls.


P - Plan:

1. Initialize two pointers, left and right, to 0 and n - 1 respectively.
2. Initialize two variables, left_max and right_max, to 0.
3. Initialize a variable, result, to 0.
4. While left is less than right:
    a. If height[left] is less than height[right]:
        i. If height[left] is greater than left_max, update left_max to height[left].
        ii. Else, increment result by left_max - height[left].
        iii. Increment left by 1.
    b. Else:
        i. If height[right] is greater than right_max, update right_max to height[right].
        ii. Else, increment result by right_max - height[right].
        iii. Decrement right by 1.

R - Review:

- All test cases passed when ran on LeetCode

E - Evaluate:

- The time complexity of this solution is O(n) where n is the length of the input list.
- The space complexity of this solution is O(1).


'''

def trap(height):
    result = 0

    left = 0
    right = len(height) - 1

    # Initialize left_max and right_max to 0
    # these variables will keep track of the maximum height of the left and right walls

    # the idea is to keep 
    left_max = 0
    right_max = 0

    while left < right:
        # If the height of the left wall is less than the height of the right wall
        if height[left] < height[right]:
            # If the height of the left wall is greater than left_max
            if height[left] >= left_max:
                # Update left_max to the height of the left wall
                left_max = height[left]
            else:
                # otherwise, increment result by left_max - height[left]
                result += left_max - height[left]
            left += 1
        else:
            # If the height of the right wall is greater than right_max
            if height[right] >= right_max:
                # Update right_max to the height of the right wall
                right_max = height[right]
            else:
                # otherwise, increment result by right_max - height[right]
                result += right_max - height[right]
            right -= 1

    return result


# Test cases

trap_test_cases = [
    ([0,1,0,2,1,0,1,3,2,1,2,1], 6),
    ([4,2,0,3,2,5], 9),
    ([], 0),
    ([1], 0),
    ([0,1,0,2,1,0,1,3,2,1,2,1], 6),
    ([4,2,0,3,2,5], 9),
    ([0,1,0,2,1,0,1,3,2,1,2,1], 6),
    ([4,2,0,3,2,5], 9),]

for height, expected in trap_test_cases:
    assert trap(height) == expected

print("## All test cases passed for Trapping Rain Water ##")

'''

Problem 2: Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a str1ing s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.


Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3: 
Input: s = " "
Output: true
Explanation: s is an empty str1ing "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

U - Understand:

- Given a string, we are to determine if it is a palindrome.
- We are to ignore non-alphanumeric characters and consider only alphanumeric characters.
- What happens when the string is empty?
- What happens when the string contains only one character?

M - Match:

- We can match this problem to the two-pointer approach.
- Or, we can use the built-in isalnum() method to check if a character is alphanumeric.

P - Plan:

1. Initialize two pointers, left and right, to 0 and n - 1 respectively.
2. While left is less than right:
    a. If the character at index left is not alphanumeric, increment left by 1.
    b. If the character at index right is not alphanumeric, decrement right by 1.
    c. If the character at index left is alphanumeric and the character at index right is alphanumeric:
        i. If the lowercase of the character at index left is not equal to the lowercase of the character at index right, return False.
        ii. Increment left by 1 and decrement right by 1.

3. Return True.

R - Review:

- All test cases passed when ran on LeetCode

E - Evaluate:

- The time complexity of this solution is O(n) where n is the length of the input string.
- The space complexity of this solution is O(1).


'''

def is_palindrome(str1):

    # Initialize left and right pointers
    left = 0
    right = len(str1) - 1

    # While left is less than right
    while left < right:
        # If the character at, index left is not alphanumeric, increment left by 1
        if not str1[left].isalnum():
            left += 1
        # If the character at index right is not alphanumeric, decrement right by 1
        elif not str1[right].isalnum():
            right -= 1
        # If the character at index left is alphanumeric and the character at index right is alphanumeric
        elif str1[left].lower() != str1[right].lower():
            return False
        else:
            left += 1
            right -= 1

    return True

# Test cases
is_palindrome_test_cases = [
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    (" ", True),
    ("", True),
    ("a", True),
    ("ab", False),
    ("A Santa at NASA", True),
    ("No 'x' in Nixon", True),
    ("Was it a car or a cat I saw?", True),
    ("Eva, can I see bees in a cave?", True),
    ("abccba", True),
    ("abc cba", True),
    ("abcddcba", True),
    ("abcd dcba", True),
    ("12321", True),
    ("123321", True),
    ("12345", False)
]

for s, expected in is_palindrome_test_cases:
    assert is_palindrome(s) == expected

print("## All test cases passed for Valid Palindrome ##")

print("\n")

print("All test cases passed for Week 3, Session 1 Problems.")


'''

Week 3, Session 2 Problems

Problem 1: Task Scheduler

You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n. Each cycle or interval allows the completion of one task. Tasks can be completed in any order, but there's a constraint: identical tasks must be separated by at least n intervals due to cooling time.

​Return the minimum number of intervals required to complete all tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2

Output: 8

Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

After completing task A, you must wait two cycles before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th cycle, you can do A again as 2 intervals have passed.

Example 2:
Input: tasks = ["A","C","A","B","D","B"], n = 1

Output: 6

Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

With a cooling interval of 1, you can repeat a task after just one other task.


Example 3:
Input: tasks = ["A","A","A", "B","B","B"], n = 3

Output: 10

Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.

U - Understand:

- Given an array of CPU tasks and a cooling time, we are to determine the minimum number of intervals required to complete all tasks.
- We can use the greedy approach to solve this problem.
- What happens when the array is empty?

M - Match:

- We can match this problem to the greedy approach
- We can use a priority queue to keep track of the tasks.

P - Plan:

1. Initialize a variable, result, to 0.
2. Initialize a priority queue, pq, to an empty list.
3. Initialize a dictionary, counter, to store the frequency of each task.
4. Iterate through the tasks list and increment the frequency of each task in the counter dictionary.

R - Review:

- All test cases passed when ran on LeetCode

E - Evaluate:

- The time complexity of this solution is O(n) where n is the length of the input list.
- The space complexity of this solution is O(n).


'''

import heapq

def leastInterval(tasks, n):

    # Initialize a variable, result, to 0
    result = 0

    # Initialize a priority queue, pq, to an empty list
    pq = []

    # Initialize a dictionary, counter, to store the frequency of each task
    counter = {}

    # Iterate through the tasks list and increment the frequency of each task in the counter dictionary
    for task in tasks:
        if task in counter:
            counter[task] += 1
        else:
            counter[task] = 1

    # Add the frequency of each task to the priority queue
    for task, freq in counter.items():
        heapq.heappush(pq, -freq)

    # While the priority queue is not empty
    while pq:
        # Initialize a variable, i, to 0
        i = 0

        # Initialize a list, temp, to an empty list
        temp = []

        # While i is less than or equal to n
        while i <= n:
            # If the priority queue is not empty
            if pq:
                # Pop the task with the highest frequency from the priority queue
                top = heapq.heappop(pq)

                # If the frequency is less than 0, add it to the temp list
                if top < -1:
                    temp.append(top + 1)

            # Increment result by 1
            result += 1

            # If the priority queue is empty and the temp list is empty, break
            if not pq and not temp:
                break

            # Increment i by 1
            i += 1

        # Add the tasks in the temp list back to the priority queue
        for task in temp:
            heapq.heappush(pq, task)

    return result


# Test cases

leastInterval_test_cases = [

    (["A","A","A","B","B","B"], 2, 8),

    (["A","C","A","B","D","B"], 1, 6),

    (["A","A","A", "B","B","B"], 3, 10),]

for tasks, n, expected in leastInterval_test_cases:
    assert leastInterval(tasks, n) == expected

print("## All test cases passed for Task Scheduler ##")

'''

Problem 2: Brick Wall

There is a rectangular brick wall in front of you with n rows of bricks. The ith row has some number of bricks each of the same height (i.e., one unit) but they can be of different widths. The total width of each row is the same.

Draw a vertical line from the top to the bottom and cross the least bricks. If your line goes through the edge of a brick, then the brick is not considered as crossed. You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

Given the 2D array wall that contains the information about the wall, return the minimum number of crossed bricks after drawing such a vertical line.

Example 1:
Input: wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
Output: 2

Example 2:
Input: wall = [[1],[1],[1]]
Output: 3

U - Understand:

- Given a 2D array representing a brick wall, we are to determine the minimum number of crossed bricks after drawing a vertical line.
- We can use the greedy approach to solve this problem.

M - Match:

- We can match this problem to the greedy approach.
- We can use a dictionary to store the positions where the vertical line crosses the bricks.

P - Plan:

1. Initialize a dictionary, counter, to store the positions where the vertical line crosses the bricks.
2. Initialize a variable, max_count, to 0.
3. Iterate through the wall list:


R - Review:

- All test cases passed when ran on LeetCode

E - Evaluate:

- The time complexity of this solution is O(n) where n is the length of the input list.
- The space complexity of this solution is O(n).

'''

def least_bricks(wall):
    # Initialize a dictionary, counter, to store the positions where the vertical line crosses the bricks
    counter = {}
    
    # Initialize a variable, max_count, to 0
    max_count = 0
    
    # Iterate through the wall list
    for row in wall:
        # Initialize a variable, position, to 0
        position = 0
    
        # Iterate through the row
        for brick in row[:-1]:
        # Increment the position by the width of the brick
            position += brick
    
            # Increment the frequency of the position in the counter dictionary
            counter[position] = counter.get(position, 0) + 1
    
            # Update max_count to the maximum of max_count and the frequency of the position
            max_count = max(max_count, counter[position])
    
    # Return the minimum number of crossed bricks
    return len(wall) - max_count


# Test cases

least_bricks_test_cases = [
    ([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]], 2),
    ([[1],[1],[1]], 3),]

for wall, expected in least_bricks_test_cases:
    assert least_bricks(wall) == expected

print("## All test cases passed for Brick Wall ##")

print("\n")

print("All test cases passed for Week 3, Session 2 Problems.")

print("\n")

print("All test cases passed for Week 3 Problems.")