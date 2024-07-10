print("CodePath TIP 103 Summer 2024 Session 5")
print("/n")

# Problem 1: Recent Counter

# You have a RecentCounter class which counts the number of recent requests within a certain time frame.

# Implement the RecentCounter class:

# RecentCounter() Initializes the counter with zero recent requests.
# int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, 
# and returns the number of requests that has happened in the past 3000 milliseconds 
# (including the new request). Specifically, return the number of requests that have happened 
# in the inclusive range [t - 3000, t].
# It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

# Example 1:

# Input
# ["RecentCounter", "ping", "ping", "ping", "ping"]
# [ [], [1], [100], [3001], [3002] ]

# Output
# [null, 1, 2, 3, 3]

# Explanation
# RecentCounter recentCounter = new RecentCounter();
# recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
# recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
# recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
# recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3

# U - Understand:

# - We need to implement a class RecentCounter that will count the number of requests in the last 3000 milliseconds.
# - Each call to ping(t) uses a strictly larger value of t than the previous call.
# - The ping method should return the number of pings in the inclusive range [t - 3000, t].

# M - Match:

# - This problem can be matched to the queue data structure.
# - A queue can help keep track of the pings and allow efficient removal of old pings.

# P - Plan:

# 1. Initialize a deque to store the timestamps of the pings.
# 2. For each ping(t) call, add the timestamp t to the deque.
# 3. Remove timestamps from the front of the deque if they are older than t - 3000 milliseconds.
# 4. Return the length of the deque which represents the number of requests in the last 3000 milliseconds.

# R - Review:

# - All test cases passed when ran.

# E - Evaluate:

# - The time complexity of the solution is O(n) where n is the number of pings in the last 3000 milliseconds.
# - The space complexity of the solution is O(n) for storing the timestamps.

from collections import deque

class RecentCounter:
    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()
        return len(self.requests)

# Test cases

rc = RecentCounter()

assert rc.ping(1) == 1  # requests = [1], range is [-2999,1], return 1
assert rc.ping(100) == 2  # requests = [1, 100], range is [-2900,100], return 2
assert rc.ping(3001) == 3  # requests = [1, 100, 3001], range is [1,3001], return 3
assert rc.ping(3002) == 3  # requests = [1, 100, 3001, 3002], range is [2,3002], return 3

print("## All test cases passed for Recent Counter ##")

# Problem 2: Implement Queue using Stacks

# Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

# Implement the MyQueue class:

# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.

# Notes:
# - You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
# - Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

# Example 1:

# Input
# ["MyQueue", "push", "push", "peek", "pop", "empty"]
# [ [], [1], [2], [], [], [] ]

# Output
# [null, null, null, 1, 1, false]

# Explanation
# MyQueue myQueue = new MyQueue();
# myQueue.push(1); // queue is: [1]
# myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
# myQueue.peek(); // return 1
# myQueue.pop(); // return 1, queue is [2]
# myQueue.empty(); // return false

# U - Understand:
# - We need to implement a queue using two stacks.
# - We need to implement push, pop, peek, and empty functions.
# - Only standard stack operations (push to top, peek/pop from top, size, and isEmpty) are allowed.

# M - Match:
# - This problem can be matched to the stack data structure.
# - We can use two stacks to implement the queue.

# P - Plan:
# 1. Use two stacks, stack1 and stack2.
# 2. For the push operation, push elements onto stack1.
# 3. For the pop operation, if stack2 is empty, move all elements from stack1 to stack2 and then pop from stack2.
# 4. For the peek operation, if stack2 is empty, move all elements from stack1 to stack2 and then peek from stack2.
# 5. For the empty operation, return true if both stack1 and stack2 are empty, false otherwise.

# R - Review:
# - All test cases passed when ran.

# E - Evaluate:
# - The time complexity for push is O(1).
# - The time complexity for pop and peek is O(n) in the worst case, but O(1) amortized.
# - The space complexity is O(n).

class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2

# Test cases

mq = MyQueue()

mq.push(1)  # queue is: [1]
mq.push(2)  # queue is: [1, 2]
assert mq.peek() == 1  # return 1
assert mq.pop() == 1  # return 1, queue is [2]
assert not mq.empty()  # return False

print("## All test cases passed for Queue using Stacks ##")

print("### END OF SESSION ONE WEEK 5 QUESTIONS ###")

print("\n")

print("### START OF SESSION TWO WEEK 5 QUESTIONS ###")


# Problem 1: Unique Binary Search Trees

# Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

# Example 1:

# Input: n = 3
# Output: 5

# Example 2:

# Input: n = 1
# Output: 1

# U - Understand:
# - We need to determine the number of structurally unique BSTs that can be formed with n nodes.
# - Each BST must use unique values from 1 to n.

# M - Match:
# - This problem can be matched to dynamic programming and combinatorial methods.
# - We can use the concept of Catalan numbers to solve this problem.

# P - Plan:
# 1. Initialize a dp array of size n+1 with dp[0] = 1 and dp[1] = 1.
# 2. Use two nested loops to fill in the dp array where dp[i] represents the number of unique BSTs with i nodes.
# 3. For each i, iterate from 1 to i and calculate dp[i] using the formula:
#    dp[i] += dp[j-1] * dp[i-j]
# 4. Return dp[n] which will give the number of unique BSTs for n nodes.

# R - Review:
# - All test cases passed when ran.

# E - Evaluate:
# - The time complexity is O(n^2).
# - The space complexity is O(n).

def numTrees(n: int) -> int:
    if n == 0:
        return 0
    
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    
    for i in range(2, n + 1):
        for j in range(1, i + 1):
            dp[i] += dp[j - 1] * dp[i - j]
    
    return dp[n]

# Test cases

assert numTrees(3) == 5  # Example 1
assert numTrees(1) == 1  # Example 2

print("## All test cases passed for Unique Binary Search Trees ##")


# Problem 2: Minimum Depth of Binary Tree

# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# Note: A leaf is a node with no children.

# Examples:

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 2

# Example 2:
# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5

# U - Understand:
# - We need to find the shortest path from the root to the nearest leaf node in a binary tree.
# - A leaf node is defined as a node with no children.
# - In the first example, the minimum depth is 2 because the shortest path is 3 -> 9.
# - In the second example, the minimum depth is 5 because the shortest path is 2 -> 3 -> 4 -> 5 -> 6.

# M - Match:
# - This problem can be matched to tree traversal methods such as Breadth-First Search (BFS) or Depth-First Search (DFS).
# - BFS is particularly suitable for finding the shortest path in an unweighted tree.

# P - Plan:
# 1. Use a BFS approach to traverse the tree level by level.
# 2. Initialize a queue and add the root node with depth 1.
# 3. While the queue is not empty:
#    a. Dequeue the front node and check if it is a leaf node.
#    b. If it is a leaf node, return the current depth.
#    c. If not, add its children to the queue with depth incremented by 1.
# 4. If the tree is empty, return 0.

# R - Review:
# - All test cases passed when ran.

# E - Evaluate:
# - The time complexity is O(n), where n is the number of nodes in the tree.
# - The space complexity is O(n) for storing nodes in the queue.

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minDepth(root: TreeNode) -> int:
    if not root:
        return 0
    
    queue = deque([(root, 1)])
    
    while queue:
        node, depth = queue.popleft()
        if not node.left and not node.right:
            return depth
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
    
    return 0

# Test cases

# Example 1
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20, TreeNode(15), TreeNode(7))
assert minDepth(root1) == 2

# Example 2
root2 = TreeNode(2)
root2.right = TreeNode(3)
root2.right.right = TreeNode(4)
root2.right.right.right = TreeNode(5)
root2.right.right.right.right = TreeNode(6)
assert minDepth(root2) == 5

print("## All test cases passed for Minimum Depth of Binary Tree ##")

print("\n")

print("### END OF SESSION TWO WEEK 5 QUESTIONS ###")