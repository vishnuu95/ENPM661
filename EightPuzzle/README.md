# 8 puzzle Challenge
The challenge is to find the path to the goal, given an initial grid state.

Here, breadth first search technique is used to search for the solution. 

* A node is represented as a object of a Class.
* The node has instance variables in it which store the index of the node, grid information, parent node, parent node index, position of the blank as well. 
* The class has two methods  setGrid and findBlank which are used to set a node's grid and finding the blank of the node. 

A sample solution image is shown is also present in the repository. 
![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")

## To run:
Python 3 is used to run the above code. 
* Open terminal and switch to the EightPuzzle folder
* Run the following command
```
python3 search8puzzle.py
```
* You will be prompted to enter the start grid. 
* Enter the grid column wise. 
* Enter '147258036' for 
1 2 0
4 5 3
7 8 6
```
Enter the grid in a coloumn wise format: 147258036
```
* You should see the program run and a 'Program Ended.. ' message. 
* 3 Files are generated namely "Nodes.txt" , "NodesInfo.txt"  and "nodePath.txt"
* Copy the "nodePath.txt" file onto the GivenFiles Folder and run plot_path.py
```
python3 plot_path.py
```
###


