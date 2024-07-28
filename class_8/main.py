print("CodePath TIP 103 Summer 2024 Session 8")
print("\n")

'''

Week 8, Session 1 Problems

Problem 1: Number of Good Paths

Given a tree (i.e., a connected, undirected graph with no cycles) consisting of n nodes numbered from 0 to n - 1 and exactly n - 1 edges.

You are given a 0-indexed integer array vals of length n where vals[i] denotes the value of the ith node. You are also given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.

A good path is a simple path that satisfies the following conditions:

The starting node and the ending node have the same value.
All nodes between the starting node and the ending node have values less than or equal to the starting node (i.e., the starting node's value should be the maximum value along the path).
Return the number of distinct good paths.

Note that a path and its reverse are counted as the same path. For example, 0 -> 1 is considered to be the same as 1 -> 0. A single node is also considered as a valid path.

Example 1:
Input: vals = [1,3,2,1,3], edges = [[0,1],[0,2],[2,3],[2,4]]
Output: 6

Example 2:
Input: vals = [1,1,2,2,3], edges = [[0,1],[1,2],[2,3],[2,4]]
Output: 7

U - Understand:

Given a tree with n nodes and n-1 edges, find the number of distinct good paths.
Each node has a value given by the vals array.
A good path starts and ends at nodes with the same value, and all intermediate nodes have values less than or equal to the starting/ending node.
Paths and their reverses are counted as the same path.

M - Match:

We can use a combination of Depth-First Search (DFS) and Union-Find to efficiently count the number of good paths.
Union-Find helps in dynamically merging sets of nodes while maintaining path conditions.

P - Plan:

Create a graph representation from the given edges.
Initialize a Union-Find data structure to manage connected components.
Sort nodes by their values and process nodes in ascending order.
For each node, union the node with its neighbors if the neighbor's value is less than or equal to the node's value.
Count the number of nodes in each connected component with the same value and use combinations to count the number of good paths.
Add single node paths for each node (each node is a trivial good path).

R - Review:

Ensure all nodes and edges are processed correctly.
Verify path counting using combinatorial logic.

E - Evaluate:

Time complexity: O(n log n) for sorting + O(n) for union-find operations.
Space complexity: O(n) for graph and union-find structures.
'''

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.count = [1] * n  # count the size of each connected component

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
                self.count[rootX] += self.count[rootY]
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
                self.count[rootY] += self.count[rootX]
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
                self.count[rootX] += self.count[rootY]

    def get_count(self, x):
        return self.count[self.find(x)]

def number_of_good_paths(vals, edges):
    n = len(vals)
    uf = UnionFind(n)
    node_by_value = sorted(range(n), key=lambda x: vals[x])
    
    value_to_nodes = {}
    for idx in node_by_value:
        if vals[idx] not in value_to_nodes:
            value_to_nodes[vals[idx]] = []
        value_to_nodes[vals[idx]].append(idx)
    
    graph = [[] for _ in range(n)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    result = 0
    
    for value in sorted(value_to_nodes.keys()):
        for node in value_to_nodes[value]:
            for neighbor in graph[node]:
                if vals[neighbor] <= vals[node]:
                    uf.union(node, neighbor)
        component_count = {}
        for node in value_to_nodes[value]:
            root = uf.find(node)
            if root not in component_count:
                component_count[root] = 0
            component_count[root] += 1
        for count in component_count.values():
            result += (count * (count + 1)) // 2

    return result

    

## Test Cases

vals_test_cases = [
([1,3,2,1,3], [[0,1],[0,2],[2,3],[2,4]], 6),
([1,1,2,2,3], [[0,1],[1,2],[2,3],[2,4]], 7)
]

for vals, edges, expected in vals_test_cases:
    output = number_of_good_paths(vals, edges)
    assert output == expected, f"For {vals} and {edges}, expected {expected} but got {output}"

print("## All test cases passed for Number of Good Paths ##")

'''

Problem 2: Network Becomes Idle

Given a network of n servers labeled from 0 to n-1 and a 2D integer array edges where edges[i] = [ui, vi] indicates a message channel between servers ui and vi, along with a 0-indexed integer array patience of length n, determine the earliest second starting from which the network becomes idle. Server 0 is the master server, and the rest are data servers that send messages to the master server and wait for replies. Messages move optimally between servers, and each data server will resend its message if it hasn't received a reply within its patience period. The network is considered idle when there are no messages passing between servers or arriving at servers.

Examples:
Example 1:

Input: edges = [[0,1],[1,2]], patience = [0,2,1]
Output: 8
Example 2:

Input: edges = [[0,1],[0,2],[1,2]], patience = [0,10,10]
Output: 3
U - Understand:

Each data server sends a message to the master server and waits for a reply.
If the reply takes longer than the server's patience period, the server will resend the message.
The goal is to determine the earliest second when the network becomes idle (no more messages passing or arriving).
M - Match:

We can match this problem to a shortest path problem in a graph and use Breadth-First Search (BFS) to determine the shortest path from the master server to all other servers.
P - Plan:

Represent the network as a graph.
Use BFS to compute the shortest path from the master server (node 0) to all other nodes.
Calculate the time it takes for each server's message to reach the master server and back.
Determine when each server stops resending messages and compute the idle time for the network.
R - Review:

This approach ensures we correctly compute the shortest paths and handle message resending efficiently.
E - Evaluate:

The time complexity of the solution is O(n + m) where n is the number of servers and m is the number of edges (for BFS).
The space complexity is O(n + m) for storing the graph and BFS queue.

'''

def network_becomes_idle(edges, patience):
    from collections import deque, defaultdict

    n = len(patience)
    graph = defaultdict(list)
    
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # Step 1: Perform BFS to find the shortest path from node 0 to all other nodes
    dist = [-1] * n
    dist[0] = 0
    queue = deque([0])
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)
    
    # Step 2: Calculate the time when each server stops resending messages
    max_time = 0
    
    for i in range(1, n):
        round_trip_time = dist[i] * 2
        if round_trip_time <= patience[i]:
            idle_time = round_trip_time
        else:
            resend_count = (round_trip_time - 1) // patience[i]
            idle_time = resend_count * patience[i] + round_trip_time
        
        max_time = max(max_time, idle_time)
    
    return max_time + 1 

## Test Cases

edges_test_cases = [
([[0,1],[1,2]], [0,2,1], 8),
([[0,1],[0,2],[1,2]], [0,10,10], 3)
]

for edges, patience, expected in edges_test_cases:
    output = network_becomes_idle(edges, patience)
    assert output == expected, f"For {edges} and {patience}, expected {expected} but got {output}"

print("## All test cases passed for Network Becomes Idle ##")


print("### ALL PROBLEMS FOR WEEK 8 SESSION 1 PASSED ###")


'''

Week 8, Session 2 Problems

Problem 1: Largest Number

U - Understand:

Given a list of non-negative integers, we need to arrange them such that they form the largest number possible. The result should be returned as a string.

Examples:
Example 1:

Input: nums = [10, 2]
Output: "210"
Example 2:

Input: nums = [3, 30, 34, 5, 9]
Output: "9534330"

M - Match:

This problem can be matched to sorting with a custom comparator. We need to compare concatenated results to decide the order of elements.

P - Plan:

Convert the integers to strings to facilitate concatenation and comparison.
Sort the strings using a custom comparator that compares concatenated results.
Concatenate the sorted strings to form the largest number.
Handle the edge case where the largest number is "0".

R - Review:

Ensure the custom comparator sorts the strings correctly by comparing concatenated results.
Check for edge cases, such as all elements being zeros.

E - Evaluate:
Time complexity: O(n log n) due to sorting.
Space complexity: O(n) for storing the string representations of the numbers.

'''

def largest_number(nums):
    nums = [str(num) for num in nums]
    nums.sort(key=lambda x: x * 10, reverse=True)
    return str(int("".join(nums)))

## Test Cases

nums_test_cases = [
([10, 2], "210"),
([3, 30, 34, 5, 9], "9534330")
]

for nums, expected in nums_test_cases:
    output = largest_number(nums)
    assert output == expected, f"For {nums}, expected {expected} but got {output}"

print("## All test cases passed for Largest Number ##")

'''

Problem 2: Rabbits In The Forest

There is a forest with an unknown number of rabbits. We asked n rabbits "How many rabbits have the same color as you?" and collected the answers in an integer array answers where answers[i] is the answer of the ith rabbit.

Given the array answers, return the minimum number of rabbits that could be in the forest.

Examples:
Example 1:

Input: answers = [1, 1, 2]
Output: 5
Example 2:

Input: answers = [10, 10, 10]
Output: 11

M - Match:

This problem can be matched to a counting problem where we need to group the answers and calculate the total number of rabbits based on the groups.

P - Plan:

Count the occurrences of each answer.
For each unique answer, calculate the minimum number of rabbits that could give that answer.
Sum up the calculated numbers for all unique answers.

R - Review:

Ensure that the counting logic correctly handles the groups of rabbits.
Verify that the calculation correctly handles each group size.

E - Evaluate:

Time complexity: O(n) for counting and calculating.
Space complexity: O(n) for storing the counts.


'''

def num_rabbits(answers):
    from collections import Counter

    count = Counter(answers)
    result = 0

    for key, value in count.items():
        result += (value + key) // (key + 1) * (key + 1)

    return result

## Test Cases

answers_test_cases = [
([1, 1, 2], 5),
([10, 10, 10], 11)
]

for answers, expected in answers_test_cases:
    output = num_rabbits(answers)
    assert output == expected, f"For {answers}, expected {expected} but got {output}"

print("## All test cases passed for Rabbits In The Forest ##")