#!/usr/bin/env python
# coding: utf-8

# # Python code for searching for the 8 puzzle solution



import sys
import os
from queue import  Queue

# Node class - kind of doubly linked list
#   Variables:
#       grid - stores the node config in column method. 
#       blank - stores the position of blank element. Useful for quick comparison of grids.
#       parent- stores the parent node. 
#   Methods:
#       setGrid - sets the Grid of a node.
#       findBlank - finds the blank space of a grid. 
global counter, states, index_ctr, path
states = []
path = []
counter = 1

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
        

def findPath(currNode):
    global states
    while(currNode != None):
        states.insert(0, currNode.grid)
        path.insert(0,[currNode.index, currNode.parent_index])
        currNode = currNode.parent
    return states,path    
    
def checkDuplicate(currNode):
    global register, counter
    counter += 1
    print (counter)
    #print (register) 
    for i in register:
        if(i.blank == currNode.blank):
            if(i.grid == currNode.grid):
                #print("True")     
                return True
    return False 

def addPossibleChildren(currNode):
    possible = { # up - 1, right - 2, down - 3, left - 4.
        0 : [2, 3],          #(1,1)
        1 : [1, 2, 3],        #(2,1)
        2 : [1, 2],         #(3,1)
        3 : [2, 3, 4],        #(1,2)
        4 : [1, 2, 3, 4],    #(2,2)
        5 : [1, 2, 4],      #(3,2)
        6 : [3, 4],         #(1,3)
        7 : [1, 3, 4],      #(2,3)
        8 : [1, 4]          #(3,3)
    }
    children = []
    #print ("possible: " + str(len(possible.get(currNode.blank))))
    for i in possible.get(currNode.blank):
        if (i == 1):
            #print("1")
            upGrid = currNode.grid[:]                   # store a copy of the grid to be updated and changed 
            blank = currNode.blank                      # store the blank location of current grid in a seperate variable
            temp = upGrid[currNode.blank - 1]           # store the element above blank in temp
            upGrid[currNode.blank - 1] = 0              # change the up element to 0 
            upGrid[currNode.blank] = temp               # change the blank element with the up element
            newNode = node(currNode, currNode.index, upGrid)
            #print(newNode.grid)
            if (not checkDuplicate(newNode)):
                if(solvable(newNode)):
                    children.append(newNode)
                    

        if (i == 2):
            #print ("2")
            rightGrid = currNode.grid[:]                # store a copy of the grid to be updated and changed 
            blank = currNode.blank                      # store the blank location in a seperate variable
            temp = rightGrid[currNode.blank + 3]        # store the element above blank in temp
            rightGrid[currNode.blank + 3] = 0           # change the right element to 0
            rightGrid[currNode.blank] = temp            # change the blank element with the right element
            newNode = node(currNode, currNode.index, rightGrid)
            #print(newNode.grid)
            if (not checkDuplicate(newNode)):
                if(solvable(newNode)):
                    children.append(newNode)
                    
        if (i == 3):
            #print ("3")
            downGrid = currNode.grid[:]                 # store a copy of the grid to be updated and changed 
            blank = currNode.blank                      # store the blank location in a seperate variable
            temp = downGrid[currNode.blank + 1]         # store the element above blank in temp
            downGrid[currNode.blank + 1] = 0            # change the down element to 0
            downGrid[currNode.blank] = temp             # change the blank element with the down element
            newNode = node(currNode, currNode.index, downGrid)
            #print(newNode.grid)
            if (not checkDuplicate(newNode)):
                if(solvable(newNode)):
                    children.append(newNode)
                    

        if (i == 4):
            #print ("4")
            leftGrid = currNode.grid[:]                 # store a copy of the grid to be updated and changed          
            blank = currNode.blank                      # store the blank location in a seperate variable
            temp = leftGrid[currNode.blank - 3]         # store the element above blank in temp
            leftGrid[currNode.blank - 3] = 0            # change the left element to 0 
            leftGrid[currNode.blank] = temp             # change the blank element with the left element   
            newNode = node(currNode, currNode.index, leftGrid)
            #print(newNode.grid)
            if (not checkDuplicate(newNode)):
                if(solvable(newNode)):
                    children.append(newNode)
                    
    #print("children: " + str(len(children)))
    global register           
    register = register + children
    #exit(-1)
    return children

def solvable(currNode):
    row_grid = [currNode.grid[0],currNode.grid[3],currNode.grid[6],currNode.grid[1],currNode.grid[4], currNode.grid[7],currNode.grid[2],currNode.grid[5],currNode.grid[8]]
    inv = 0
    for i in range(8):
        for j in range(i+1,9):
            if(row_grid[i] and row_grid[j] and (row_grid[i] > row_grid[j])):
                inv+=1

    if(inv%2 == 0):
        return True
    else:
        print("False")
        return False    

def write_states(states):
    f = open("nodePath.txt","w")
    for i in states:
        for j in range(len(i)):  
            f.write(str(i[j]) + " ")
        f.write("\n")    
    f.close()

def write_nodes(register):
    f = open("Nodes.txt","w")
    for i in register:
        for j in range(len(i.grid)):
            f.write(str(i.grid[j]) + ' ')
        f.write("\n")    
    f.close()

def write_path(path):
    f = open("NodesInfo.txt","w")
    for i in range(len(path)):
        f.write(str(path.pop())+"\n")
    f.close()    

def solve(que):
    while(1):
        if(not que.qsize()):
            print ("No solution possible. Exiting code.")
            return
        a = que.get()    
        if(isGoal(a)):
            states, path = findPath(a)
            break
        else:
            children = addPossibleChildren(a)
            for i in children:
                que.put(i)

            
        
    return states          
# While currnode ! = None
#Check if curr is goal : if yes , add currnode to stack gen function and return, else iterate all possible child 
# Possible child : Check based on location, Non previously present node
# Assign self with possible childs based on action. 
# If iterated through all childs return 
      
if __name__=="__main__":
    initNode = input("Enter the grid in a coloumn wise format: " )
    initNode = [int(i) for i in initNode]
    print ("You entered: " + str(initNode))
    print ("Searching.... ")   
    index_ctr = 0
    curr = node(None,0,initNode)
    register = [curr] 
    que = Queue()
    que.put(curr)
    if(isGoal(curr)):
        states.insert(0,curr.grid)
        states.insert(0,curr.grid)
        path.append([0,0])
    elif(not solvable(curr)):
        states.insert(0,curr.grid)
        path.append([0,0])
    else:        
        states = solve(que)

    print("Program Ended.. ")
    write_states(states)            # writes curr to goal state
    write_nodes(register)           # writes all nodes to visited nodes to one file
    write_path(path)                # writes curr node index and parent node index
