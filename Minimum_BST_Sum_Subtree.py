"""
SAMPLE INPUT
1
38
13 5 23 N 17 N N 16 N N N

-----------------------------
What is Binary Tree?
Binary Tree is a form of a tree whose nodes cannot have more than two children.
Each node of the binary tree has two pointers associated with it, one points to the left child,
and the other points to the right child of the node.
It is an unordered tree having no fixed organized structure for the arrangement of nodes.

"""

#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''

class Solution:
    def minSubtreeSumBST(self, target, root):
        res = float(inf)
        def traverse(node):
            nonlocal res
            if not node:
                return float(inf), float(-inf), 0, 0
            left = traverse(node.left)
            right = traverse(node.right)
            if not left or not right:
                return
            leftMin, leftMax, leftSum, leftSumNode = left[0], left[1], left[2], left[3]
            rightMin, rightMax, rightSum, rightSumNode = right[0], right[1], right[2], right[3]
            if node.data > leftMax and node.data < rightMin:
                nodeMax = max(rightMax,node.data)
                nodeMin = min(leftMin, node.data)
                nodeSum = leftSum + rightSum + node.data
                if nodeSum == target:
                    res = min(res, leftSumNode + rightSumNode + 1)
                return nodeMin, nodeMax, nodeSum, leftSumNode + rightSumNode + 1
        traverse(root)
        return res if res != float(inf) else -1

#{ 
 # Driver Code Starts.

#Initial Template for Python 3
from collections import defaultdict
from collections import deque
from sys import stdin, stdout
from math import inf
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

if __name__ == '__main__':
    test_cases = int(input())
    for _ in range (test_cases):
        target = int(input())
        N = input()
        root = buildTree(N)
        res = Solution().minSubtreeSumBST(target, root)
        print(res)
        
# } Driver Code Ends