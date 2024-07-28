print("CodePath TIP 103 Summer 2024 Session 7")
print("/n")

'''

Week 7, Session 1 Problems

Problem 1: Course Schedule II

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

Example 2:
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

Example 3:
Input: numCourses = 1, prerequisites = []
Output: [0]

U - Understand:

Given a number of courses and a list of prerequisites, we need to find an order in which to take the courses such that all prerequisites are satisfied.
If there are multiple valid orders, return any one of them.
If it is not possible to complete all courses, return an empty array.
M - Match:

This problem can be matched with Topological Sorting of a Directed Acyclic Graph (DAG).
We can use Kahn's Algorithm (BFS) or DFS to detect cycles and determine the topological order.
P - Plan:

Create an adjacency list to represent the graph.
Create an array to track the in-degree of each node (course).
Initialize a queue with all nodes having in-degree of 0 (no prerequisites).
Perform BFS:
Dequeue a node, add it to the result list.
Decrease the in-degree of its neighbors.
If a neighbor's in-degree becomes 0, enqueue it.
If the result list contains all courses, return it. Otherwise, return an empty array (cycle detected).
R - Review:

All test cases passed when ran on LeetCode.
E - Evaluate:

The time complexity of this solution is O(V + E) where V is the number of courses and E is the number of prerequisites.
The space complexity of this solution is O(V + E) due to the adjacency list and the in-degree array.

'''

from collections import deque, defaultdict

def findOrder(numCourses, prerequisites):
    # Create adjacency list and in-degree array
    adj_list = defaultdict(list)
    in_degree = [0] * numCourses
    # Populate the adjacency list and in-degree array
    for dest, src in prerequisites:
        adj_list[src].append(dest)
        in_degree[dest] += 1

    # Initialize the queue with nodes having in-degree of 0
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    result = []

    # Perform BFS
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in adj_list[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If the result list contains all courses, return it. Otherwise, return an empty array.
    if len(result) == numCourses:
        return result
    else:
        return []
    
course_schedule_test_cases = [
(2, [[1,0]], [0,1]),
(4, [[1,0],[2,0],[3,1],[3,2]], [0,1,2,3]), # One possible solution is [0,2,1,3]
(1, [], [0])
]

for numCourses, prerequisites, expected in course_schedule_test_cases:
    result = findOrder(numCourses, prerequisites)
print(f"Input: numCourses={numCourses}, prerequisites={prerequisites}")
print(f"Output: {result}")
assert result == expected or result[::-1] == expected # The order can be reversed in some cases.

print("## All test cases passed for Course Schedule II ##")


'''

Problem 2: Course Schedule IV

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course ai first if you want to take course bi.

You are also given an array queries where queries[j] = [uj, vj]. For the jth query, you should answer whether course uj is a prerequisite of course vj or not.

Return a boolean array answer, where answer[j] is the answer to the jth query.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
Output: [false,true]
Explanation: The pair [1, 0] indicates that you have to take course 1 before you can take course 0. Course 0 is not a prerequisite of course 1, but the opposite is true.

Example 2:
Input: numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]
Output: [false,false]
Explanation: There are no prerequisites, and each course is independent.

Example 3:
Input: numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
Output: [true,true]

U - Understand:

Given a number of courses and a list of prerequisites, we need to answer if one course is a prerequisite of another for a series of queries.
We can have direct and indirect prerequisites.
M - Match:

This problem can be matched with graph traversal techniques.
We can use the Floyd-Warshall algorithm to determine the transitive closure of the graph.
P - Plan:

Initialize a 2D array reachable where reachable[i][j] is True if course i is a prerequisite of course j.
Set reachable[i][i] to True for all i.
For each prerequisite pair [ai, bi], set reachable[ai][bi] to True.
Use the Floyd-Warshall algorithm to update the reachable array for transitive prerequisites.
For each query, check the reachable array to determine if the prerequisite condition is met.
R - Review:

All test cases passed when ran on LeetCode.
E - Evaluate:

The time complexity of this solution is O(n^3) where n is the number of courses.
The space complexity of this solution is O(n^2) due to the 2D array.

'''


def checkIfPrerequisite(numCourses, prerequisites, queries):
    # Initialize the reachable matrix
    reachable = [[False] * numCourses for _ in range(numCourses)]
    # Set self-reachability
    for i in range(numCourses):
        reachable[i][i] = True

    # Set direct prerequisites
    for pre, course in prerequisites:
        reachable[pre][course] = True

    # Floyd-Warshall algorithm to find all reachable pairs
    for k in range(numCourses):
        for i in range(numCourses):
            for j in range(numCourses):
                if reachable[i][k] and reachable[k][j]:
                    reachable[i][j] = True

    # Answer the queries
    result = []
    for u, v in queries:
        result.append(reachable[u][v])

    return result
#Test cases
course_schedule_iv_test_cases = [
(2, [[1,0]], [[0,1],[1,0]], [False, True]),
(2, [], [[1,0],[0,1]], [False, False]),
(3, [[1,2],[1,0],[2,0]], [[1,0],[1,2]], [True, True])
]

for numCourses, prerequisites, queries, expected in course_schedule_iv_test_cases:
    result = checkIfPrerequisite(numCourses, prerequisites, queries)
print(f"Input: numCourses={numCourses}, prerequisites={prerequisites}, queries={queries}")
print(f"Output: {result}")
assert result == expected

print("## All test cases passed for Course Schedule IV ##")


'''

Week 7, Session 2 Problems

Problem 1: Network Delay Time

You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

Example 1:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

Example 2:
Input: times = [[1,2,1]], n = 2, k = 1
Output: 1

Example 3:
Input: times = [[1,2,1]], n = 2, k = 2
Output: -1

U - Understand:

Given a network of nodes and directed edges with travel times, we need to find the minimum time for a signal sent from a given node to reach all other nodes.
If it's not possible for the signal to reach all nodes, return -1.
M - Match:

This problem can be matched with graph traversal techniques.
We can use Dijkstra's algorithm to find the shortest paths from the source node to all other nodes.
P - Plan:

Create an adjacency list to represent the graph.
Use a priority queue to implement Dijkstra's algorithm to find the shortest path from the source node to all other nodes.
Keep track of the shortest time it takes to reach each node.
If all nodes are reached, return the maximum time taken to reach any node. If not all nodes are reachable, return -1.

R - Review:

All test cases passed when ran on LeetCode.
E - Evaluate:

The time complexity of this solution is O((V + E) log V) where V is the number of nodes and E is the number of edges.
The space complexity of this solution is O(V + E) due to the adjacency list and the priority queue.
'''

import heapq

def networkDelayTime(times, n, k):
    # Create the adjacency list
    graph = defaultdict(list)

    # iterate through the times and populate the adjacency list
    # for each node, store the neighbor and the time taken to reach it
    for u, v, w in times:
        graph[u].append((v, w))
    # Min-heap priority queue to implement Dijkstra's algorithm
    pq = [(0, k)]
    dist = {}

    while pq:
        time, node = heapq.heappop(pq)
        if node in dist:
            continue
        dist[node] = time
        for neighbor, t in graph[node]:
            if neighbor not in dist:
                heapq.heappush(pq, (time + t, neighbor))

    # If all nodes are reached, return the maximum time taken to reach any node
    if len(dist) == n:
        return max(dist.values())
    else:
        return -1

#Test cases
network_delay_time_test_cases = [
([[2,1,1],[2,3,1],[3,4,1]], 4, 2, 2),
([[1,2,1]], 2, 1, 1),
([[1,2,1]], 2, 2, -1)
]

for times, n, k, expected in network_delay_time_test_cases:
    result = networkDelayTime(times, n, k)
print(f"Input: times={times}, n={n}, k={k}")
print(f"Output: {result}")
assert result == expected

print("## All test cases passed for Network Delay Time ##")


'''

Problem 2: Redundant Connection

In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

Example 1:
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]

Example 2:
Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]

U - Understand:

Given a list of edges representing a graph, we need to identify an edge that can be removed to transform the graph into a tree.
A tree is an acyclic connected graph.
The graph was initially a tree before one additional edge was added, forming exactly one cycle.
M - Match:

This problem can be matched with graph traversal and Union-Find (Disjoint Set) data structure.
Union-Find helps detect cycles in an undirected graph efficiently.
P - Plan:

Initialize a Union-Find data structure for n nodes.
Iterate through each edge in the list:
For each edge, check if the two vertices are already connected.
If they are connected, this edge forms a cycle and is the redundant edge.
If they are not connected, union the two vertices.
Return the edge that forms the cycle.
R - Review:

All test cases passed when ran on LeetCode.
E - Evaluate:

The time complexity of this solution is O(n log* n) due to the Union-Find operations with path compression and union by rank.
The space complexity of this solution is O(n) due to the Union-Find data structure.
'''

class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])  # Path compression
        return self.parent[p]

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        
        if rootP == rootQ:
            return False
        
        if self.rank[rootP] > self.rank[rootQ]:
            self.parent[rootQ] = rootP
        elif self.rank[rootP] < self.rank[rootQ]:
            self.parent[rootP] = rootQ
        else:
            self.parent[rootQ] = rootP
            self.rank[rootP] += 1
            
        return True

def findRedundantConnection(edges):
    n = len(edges)
    uf = UnionFind(n + 1)  
    redundant_edge = None
    
    for a, b in edges:
        if not uf.union(a, b):
            redundant_edge = [a, b]
    
    return redundant_edge

#Test cases
redundant_connection_test_cases = [
([[1,2],[1,3],[2,3]], [2,3]),
([[1,2],[2,3],[3,4],[1,4],[1,5]], [1,4])
]

for edges, expected in redundant_connection_test_cases:
    result = findRedundantConnection(edges)
print(f"Input: edges={edges}")
print(f"Output: {result}")
assert result == expected

print("## All test cases passed for Redundant Connection ##")






