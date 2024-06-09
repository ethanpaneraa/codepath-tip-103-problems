print('Ethan Pineda')
print('\n')

# Definition for singly-linked list.
class ListNode:
    def __init__(self) -> None:
        self.val = 0
        self.head = None
        self.next = None

'''
Week 2, Session 2, June 12th 2024 Problems 1 & 2 Solutions

Problem: Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Example 1: 
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2: 
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]

U - Understand: 

- What happens if the input linked-list is empty?
- What happens if the input linked-list has only one node?
- What happens if the input linked-list has two nodes?

M - Match: 

- I think its best to use a two-pointer approach to solve this problem
- And I think based on other linked-list problems that I've solved before, I'll probably need to use a temp node to help me keep track of the head of the linked-list

P - Plan:

- create a temp node to keep track of the head of the linked-list
- iterate through the entire linked-list
- since i know that the first node is considered odd that means that the second one is even
- so i can just rearrange the linked-list by moving the odd nodes to the front and the even nodes to the back
- return the temp node

R - Review:

- I was able to solve the problem in O(1) extra space complexity and O(n) time complexity

'''

print('** Problem 1: Odd Even Linked List **')

def odd_even_list(linked_list: ListNode) -> ListNode:

    if not linked_list:
        return None
    
    # this will hold the final modified linked-list
    temp_head = linked_list

    # define new linked-lists to hold the odd and even nodes
    even_linked_list = ListNode()
    odd_linked_list = ListNode()

    # this will hold the head of the even linked-list
    even_linked_list_head = even_linked_list

    # flag to keep track of whether the current node is odd or even
    is_even = False

    # iterate through the linked-list
    while linked_list:
        # if the current node is even
        if is_even:
            # add the current node to the even linked-list
            even_linked_list.next = linked_list
            # move the even linked-list pointer to the next node
            even_linked_list = even_linked_list.next
        else:
            # otherwise, we're at a odd node so add it to the odd linked-list
            odd_linked_list.next = linked_list
            # move the odd linked-list pointer to the next node
            odd_linked_list = odd_linked_list.next
        # flip the flag
        is_even = not is_even
        
        # move the linked-list pointer to the next node
        linked_list = linked_list.next

    # set the next node of the odd linked-list to the head of the even linked-list
    even_linked_list.next = None

    # set the next node of the temp node to the head of the odd linked-list
    odd_linked_list.next = even_linked_list_head.next

    return temp_head
    

# Test Cases
print('** Problem 1: Odd Even Linked List Test Cases **')

odd_even_list_test_cases = [
    [1,2,3,4,5],                # [1,3,5,2,4]
    [2,1,3,5,6,4,7],            # [2,3,6,7,1,5,4]
    [1,2,3,4,5,6,7,8,9,10],     # [1,3,5,7,9,2,4,6,8,10]
    [2,1,3,5,6,4,7,8,9,10],     # [2,3,6,7,1,5,4,8,9,10]
    [1,2,3,4,5,6,7,8,9,10,11],  # [1,3,5,7,9,11,2,4,6,8,10]
    [2,1,3,5,6,4,7,8,9,10,11]   # [2,3,6,7,1,5,4,8,9,10,11]
]

def convert_to_linked_list(arr):
    head = ListNode()
    temp = head

    for i in arr:
        temp.next = ListNode()
        temp = temp.next
        temp.val = i
    
    return head.next

def print_linked_list(head):
    array = []
    temp = head
    while temp:
        array.append(temp.val)
        temp = temp.next
    return array

for test_case in odd_even_list_test_cases:
    print("Input: ", test_case)
    print("Output: ", 
          print_linked_list(odd_even_list(convert_to_linked_list(test_case)))
          )


print('\n')
print('** END OF PROBLEM 1 FOR WEEK 2, SESSION 1 **')

print('** START OF PROBLEM 2 FOR WEEK 2, SESSION 1 **')
print('\n')
print('** Problem 2: Swap Nodes in Pairs **')

'''

Given the head of a linked list, rotate the list to the right by k places.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

The list goes from 
[1,2,3,4,5] -> [5,1,2,3,4] -> [4,5,1,2,3]


Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]

U - Understand:

- What happens if the input linked-list is empty?
- What happens if the input linked-list has only one node?
- What happens if the input linked-list has two nodes?
- what happens if k is greater than the length of the linked-list?

M - Match:

- I think its best to use a two-pointer approach to solve this problem
- And I think based on other linked-list problems that I've solved before, I'll probably need to use a temp node to help me keep track of the head of the linked-list

P - Plan:

- create a temp node to keep track of the head of the linked-list
- 

R - Review:

- All test cases when ran on LeetCode

E - Evaluate:

- Time Complexity: O(n)
- Space Complexity: O(1)

'''

def rotate_right(head, k):

    if not head:
        return None
    
    temp_head = head

    # if you find the length of the linked-list and k is greater than the length of the linked-list

    # find the length of the linked-list

    length = 1

    temp = head

    # find the length of the linked-list
    while temp.next != None:
        length += 1
        temp = temp.next

    # if k is greater than the length of the linked-list
    k = k % length
    k = length - k
    
    # make the linked-list circular
    temp.next = head

    # find the node that will be the new head of the linked-list
    while k > 0:
        temp = temp.next
        k -= 1

    # once you find the new head of the linked-list
    # set the temp_head to the next node of the new head
    temp_head = temp.next
    temp.next = None

    # return the new head of the linked-list
    return temp_head


# Test Cases
print('** Problem 2: Rotate Right Test Cases **')

rotate_right_test_cases = [
    [[1,2,3,4,5], 2], # [4,5,1,2,3]
    [[0,1,2], 4],     # [2,0,1]
    [[1,2,3,4,5], 5], # [1,2,3,4,5]
    [[1,2,3,4,5], 10], # [1,2,3,4,5]
    [[1,2,3,4,5], 0], # [1,2,3,4,5]
    [[1,2,3,4,5], 1]  # [5,1,2,3,4]
]

for test_case in rotate_right_test_cases:
    print("Input: ", test_case)
    print("Output: ", 
          print_linked_list(rotate_right(convert_to_linked_list(test_case[0]), test_case[1]))
          )
    
print('\n')

print('** END OF PROBLEM 2 FOR WEEK 2, SESSION 1 **')

print('** END OF WEEK 2, SESSION 1 **')

print('\n')

print('** START OF WEEK 2, SESSION 2 **')

print('\n')

print('** Problem 1: Shifting Letters **')

'''  

You are given a string s of lowercase English letters and an integer array shifts of the same length.

Call the shift() of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a').

For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.
Now for each shifts[i] = x, we want to shift the first i + 1 letters of s, x times.

Return the final string after all such shifts to s are applied-

Example 1:
Input: s = "abc", shifts = [3,5,9]
Output: "rpl"

Explanation: We start with "abc".
After shifting the first 1 letters of s by 3, we have "dbc".
After shifting the first 2 letters of s by 5, we have "igc".
After shifting the first 3 letters of s by 9, we have "rpl", the answer.


Input: s = "aaa", shifts = [1,2,3]
Output: "gfd"


U - Understand:

- What happens if the input string is empty?
- What happens if the input string has only one character?

M - Match:

- This is an array problem
- I think I can use the ord() function to get the ASCII value of a character

P - Plan:

- iterate through the shifts array
- for each shift, iterate through the string
- get the ASCII value of the character
- add the shift to the ASCII value
- get the remainder of the ASCII value divided by 26
- get the character from the remainder
- add the character to the result string
- return the result string

R - Review:

- All test cases when ran on LeetCode

E - Evaluate:

- Time Complexity: O(n)
- Space Complexity: O(1)


'''

def shift_letter(letter, shift):
    # explanation: 
    # ord(letter) - ord('a') gets the position of the letter in the alphabet
    # add the shift to the position of the letter in the alphabet
    # get the remainder of the position of the letter in the alphabet divided by 26
    # get the character from the remainder
    return chr((ord(letter) - ord('a') + shift) % 26 + ord('a'))

def shifting_letters(s, shifts):

    result = ""
    n = len(s)
    # iterate through the shifts array in reverse
    # in order to get the total shift for each character
    for i in range(n - 1, -1, -1):
        # if i is not the last element in the array
        # add the current shift to the next shift
        if i < n - 1:
            shifts[i] += shifts[i + 1]

    # apply the shifts to the string
    for i in range(n):
        result += shift_letter(s[i], shifts[i])


    return result


# Test Cases

print('** Problem 1: Shifting Letters Test Cases **')

shifting_letters_test_cases = [
    ["abc", [3,5,9]], # "rpl"
    ["aaa", [1,2,3]], # "gfd"
    ["abc", [1,2,3]], # "fde"
    ["abc", [1,2,3,4]], # "hfg"
    ["abc", [1,2,3,4,5]], # "hij"
    ["abc", [1,2,3,4,5,6]], # "hij"
    ["abc", [1,2,3,4,5,6,7]], # "hij"
    ["abc", [1,2,3,4,5,6,7,8]], # "hij"
    ["abc", [1,2,3,4,5,6,7,8,9]], # "hij"
    ["abc", [1,2,3,4,5,6,7,8,9,10]], # "hij"
    ["abc", [1,2,3,4,5,6,7,8,9,10,11]], # "hij"
    ["abc", [1,2,3,4,5,6,7,8,9,10,11,12]], # "hij"
    ["abc", [1,2,3,4,5,6,7,8,9,10,11,12,13]], # "hij"
    ["abc", [1,2,3,4,5,6,7,8,9,10,11,12,13,14]], # "hij"
    ["abc", [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]], # "hij"
    ["abc", [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]], # "hij"
    ["abc", [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]], # "hij"
    ["abc", [1,2,3,4,5,6,]]# "hij

]

for test_case in shifting_letters_test_cases:
    print("Input: ", test_case)
    print("Output: ", shifting_letters(test_case[0], test_case[1]))

print('\n')

print('** END OF PROBLEM 1 FOR WEEK 2, SESSION 2 **')


print('** START OF PROBLEM 2 FOR WEEK 2, SESSION 2 **')

print('\n')

print('** Problem 2: Set Matrix Zeros **')

'''

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Example 1: 
matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2: 
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

U - Understand:

- What happens if the input matrix is empty?
- What happens if the input matrix has only one row?
- What happens if the input matrix has only one column?

M - Match:

- This is a matrix problem
- I should be able to do this using constant space

P - Plan:

- I want to keep track of the rows and columns that have zeros in them
- I can do this by using the first row and column of the matrix


'''

def setZeros(matrix):

    # get the number of rows and columns in the matrix
    rows = len(matrix)
    cols = len(matrix[0])

    # keep track of whether the first row and column have zeros
    first_row_has_zero = False
    first_col_has_zero = False

    # check if the first row has a zero
    for i in range(cols):
        if matrix[0][i] == 0:
            first_row_has_zero = True
            break

    # check if the first column has a zero
    for i in range(rows):
        if matrix[i][0] == 0:
            first_col_has_zero = True
            break

    # iterate through the matrix and set the first row and column to zero if there is a zero
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # iterate through the matrix and set the zeros
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # set the first row to zero if the first row has a zero
    if first_row_has_zero:
        for i in range(cols):
            matrix[0][i] = 0

    # set the first column to zero if the first column has a zero
    if first_col_has_zero:
        for i in range(rows):
            matrix[i][0] = 0

    return matrix

# Test Cases

print('** Problem 2: Set Matrix Zeros Test Cases **')

set_zeros_test_cases = [
    [[1,1,1],[1,0,1],[1,1,1]], # [[1,0,1],[0,0,0],[1,0,1]]
    [[0,1,2,0],[3,4,5,2],[1,3,1,5]], # [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
    [[1,2,3],[4,5,6],[7,8,9]], # [[1,2,3],[4,5,6],[7,8,9]]
    [[1,2,3],[4,0,6],[7,8,9]], # [[1,0,3],[0,0,0],[7,0,9]]
    [[1,2,3],[0,5,6],[7,8,9]], # [[0,2,3],[0,0,0],[0,8,9]]
    [[1,2,3],[4,5,0],[7,8,9]], # [[1,2,0],[0,0,0],[7,8,0]]
    [[1,2,3],[4,5,6],[0,8,9]], # [[0,2,3],[0,5,6],[0,0,0]]
    [[0,2,3],[4,5,6],[7,8,9]], # [[0,0,0],[0,5,6],[0,8,9]]
    [[1,2,3],[4,5,6],[7,0,9]], # [[1,0,3],[4,0,6],[0,0,0]]
    [[1,2,3],[4,5,6],[7,8,0]], # [[1,2,0],[4,5,0],[0,0,0]]
    [[0,2,3],[4,5,6],[7,8,9]], # [[0,0,0],[0,5,6],[0,8,9]]
    [[1,2,3],[4,0,6],[7,8,9]], # [[1,0,3],[0,0,0],[7,0,9]]
    [[1,2,3]], # [[1,2,3]]

]

for test_case in set_zeros_test_cases:
    print("Input: ", test_case)
    print("Output: ", setZeros(test_case))

print('\n')

print('** END OF PROBLEM 2 FOR WEEK 2, SESSION 2 **')

print('** END OF WEEK 2, SESSION 2 **')

print('\n')

print('** END OF WEEK 2 **')