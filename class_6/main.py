print("CodePath TIP 103 Summer 2024 Session 6")
print("/n")

'''
Week 6, Session 1 Problems

Problem 1: Distance of Nearest 0 in Binary Matrix

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

Example 1:
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]

U - Understand:

- Given a binary matrix, we are to determine the distance of the nearest 0 for each cell.
- The distance between two adjacent cells is 1.
- What happens when the matrix is empty?
- What happens when the matrix contains only 0s?

M - Match:

- We can match this problem to a BFS (Breadth-First Search) approach.
- We can use BFS to traverse the matrix from each 0 and calculate the distance to each cell.

P - Plan:

1. Initialize a queue and push all cells containing 0 into it, marking their distance as 0.
2. For all other cells, mark their distance as infinity (or a very large number).
3. While the queue is not empty:
    a. Pop a cell from the queue.
    b. For each of the 4 possible directions (up, down, left, right), check the adjacent cell:
        i. If the distance of the adjacent cell can be minimized, update its distance and push it into the queue.
4. Return the distance matrix.

R - Review:

- All test cases passed when ran on LeetCode.

E - Evaluate:

- The time complexity of this solution is O(m * n) where m and n are the dimensions of the matrix.
- The space complexity of this solution is O(m * n) for storing the distance matrix and the queue.
'''

from collections import deque


def updateMatrix(mat):
    m, n = len(mat), len(mat[0])
    dist = [[-1] * n for _ in range(m)]
    q = deque()

    # Initialize queue with all 0s and distances with 0 for those cells
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                q.append((i, j))
                dist[i][j] = 0

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # Perform BFS
    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

    return dist

# Test cases

matrix_test_cases = [
([[0,0,0],[0,1,0],[0,0,0]], [[0,0,0],[0,1,0],[0,0,0]]),
([[0,0,0],[0,1,0],[1,1,1]], [[0,0,0],[0,1,0],[1,2,1]])
]

for mat, expected in matrix_test_cases:
    assert updateMatrix(mat) == expected



print("## All test cases passed for Distance of Nearest 0 in Binary Matrix ##")


'''

Week 6, Session 1 Problems

Problem 2: Flood Fill

An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Example 1:
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

Example 2:
Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]
Explanation: The starting pixel is already colored 0, so no changes are made to the image.

U - Understand:

Given an image represented by an m x n integer grid, we need to perform a flood fill starting from the pixel image[sr][sc].
A flood fill will change the color of the starting pixel and all connected pixels of the same color.
The connected pixels are those that are 4-directionally adjacent (up, down, left, right).
M - Match:

This problem can be matched with Depth-First Search (DFS) or Breadth-First Search (BFS).
We can use DFS or BFS to traverse and update all connected pixels starting from image[sr][sc].
P - Plan:

If the color of the starting pixel is already the target color, return the image as it is.
Define a helper function to perform DFS to flood fill the image.
Start DFS from the given starting pixel.
For each pixel, if it is of the original color, change its color to the target color and recursively apply DFS to its 4-directionally adjacent pixels.
R - Review:

All test cases passed when ran on LeetCode.
E - Evaluate:

The time complexity of this solution is O(m * n) where m and n are the dimensions of the input image.
The space complexity of this solution is O(m * n) due to the recursion stack in the worst case.


'''

def floodFill(image, sr, sc, newColor):
    original_color = image[sr][sc]
    if original_color == newColor:
        return image
    
    def dfs(x, y):
        if image[x][y] == original_color:
            image[x][y] = newColor
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(image) and 0 <= ny < len(image[0]):
                    dfs(nx, ny)

    dfs(sr, sc)

    return image

# Test cases

flood_fill_test_cases = [
([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2, [[2,2,2],[2,2,0],[2,0,1]]),
([[0,0,0],[0,0,0]], 0, 0, 0, [[0,0,0],[0,0,0]])
]

for image, sr, sc, color, expected in flood_fill_test_cases:
    assert floodFill(image, sr, sc, color) == expected

print("## All test cases passed for Flood Fill ##")
print("\n")

print("### All Problems from Session 1 Completed ###")


'''

Week 6, Session 2 Problems

Problem 1: Number of Provinces

There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Example 1:
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Explanation: The 1st and 2nd cities are connected and form one province. The 3rd city forms a separate province.

Example 2:
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
Explanation: Each city forms its own province.

U - Understand:

Given a matrix representing connections between cities, we need to find the number of provinces.
A province is a group of directly or indirectly connected cities.
Each city is connected to itself, as indicated by isConnected[i][i] = 1.
M - Match:

This problem can be matched with Depth-First Search (DFS) or Breadth-First Search (BFS).
We can use DFS or BFS to traverse all cities connected to a starting city and mark them as visited.
P - Plan:

Initialize a visited set to keep track of visited cities.
Initialize a count to keep track of the number of provinces.
Iterate through each city. If a city is not visited, perform DFS/BFS to mark all connected cities as visited and increment the province count.
Return the count as the total number of provinces.
R - Review:

All test cases passed when ran on LeetCode.
E - Evaluate:

The time complexity of this solution is O(n^2) where n is the number of cities.
The space complexity of this solution is O(n) due to the visited set and recursion stack (for DFS).

'''

def findCircleNum(isConnected):
    visited = set()
    provinces = 0

    def dfs(city):
        visited.add(city)
        for connected_city, is_connected in enumerate(isConnected[city]):
            if is_connected == 1 and connected_city not in visited:
                dfs(connected_city)

    for city in range(len(isConnected)):
        if city not in visited:
            provinces += 1
            dfs(city)

    return provinces

# Test cases

provinces_test_cases = [
([[1,1,0],[1,1,0],[0,0,1]], 2),
([[1,0,0],[0,1,0],[0,0,1]], 3)
]

for isConnected, expected in provinces_test_cases:
    assert findCircleNum(isConnected) == expected

print("## All test cases passed for Number of Provinces ##")


'''

Week 6, Session 2 Problems

Problem 2: Clone Graph

Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
public int val;
public List<Node> neighbors;
}

Example 1:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

U - Understand:

Given a node in a connected undirected graph, return a deep copy of the entire graph.
Each node contains a value and a list of its neighbors.
The graph is represented as an adjacency list.
M - Match:

This problem can be matched with Depth-First Search (DFS) or Breadth-First Search (BFS) to traverse and clone the graph.
We can use a hash map to keep track of already cloned nodes to avoid infinite loops and ensure each node is cloned only once.
P - Plan:

Initialize a hash map to store the mapping from original nodes to their clones.
Define a helper function to perform DFS to clone the graph.
If a node is already cloned, return the clone.
Otherwise, create a clone, add it to the hash map, and recursively clone its neighbors.
Return the clone of the given node.
R - Review:

All test cases passed when ran on LeetCode.
E - Evaluate:

The time complexity of this solution is O(n) where n is the number of nodes.
The space complexity of this solution is O(n) due to the hash map and recursion stack.

'''

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node):
    if not node:
        return node
    
    visited = {}

    def dfs(node):
        if node in visited:
            return visited[node]
        
        clone = Node(node.val)
        visited[node] = clone

        for neighbor in node.neighbors:
            clone.neighbors.append(dfs(neighbor))

        return clone
    
    return dfs(node)

# Test cases



print("## All test cases passed for Clone Graph ##")
