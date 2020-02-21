#!/usr/bin/env python
# coding: utf-8

# # Python code for searching for the 8 puzzle solution



import sys
import os

# Node class - kind of doubly linked list
#   Variables:
#       grid - stores the node config in column method. 
#       blank - stores the position of blank element. Useful for quick comparison of grids.
#       parent- stores the parent node. 
#   Methods:
#       setGrid - sets the Grid of a node.
#       findBlank - finds the blank space of a grid. 

class node:
    def __init__(self, parent, parent_index, grid):
        global index_ctr
        self.grid = grid
        self.blank = self.findBlank(self)
        self.index = index_ctr
        index_ctr+=1
        # self.up = None
        # self.down = None
        # self.left = None
        # self.right = None
        self.parent = parent
        self.parent_index = parent_index
        #
        #print(self.blank)
    
    def setGrid(self, grid):
        self.grid = grid
        return 

    @staticmethod
    def findBlank(self):
        index = None
        for i in range(0,9):
            #print(self.grid[i])
            if self.grid[i]==0:
                index = i
        #print(index)        
        return index        
def isGoal(currNode):
    if(currNode.blank == 8):
        if(currNode.grid == list([1, 4, 7, 2, 5, 8, 3, 6, 0])):
            return 1
        else:
            return 0    
    else:
        return 0        


