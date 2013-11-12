NeuroScouting-Tree
==================
##Prompt
Build a tree of integers which has the following properties:
- The root node has value 1.
- Each node in the tree has two children.
- The value for the children nodes is determined as follows:
-- If it's the left children, its value will be the sum of the parent's value and the parent's left sibling value. If the parent has no left sibling, then the child's value is the same as its parent.
-- If it's the right children, its value will be the sum of the parent's value and the parent's right sibling value. If the parent has no right sibling, then the child's value is the same as its parent.

The program should be able to accept an input value to determine how many levels of this tree it should generate. How the program receives the input value is up to you (for example it could be in the command line, reading a file, with some GUI, anything really). The program should build the tree and then print it out. Again, how you print it is completely up to you (it could print to a file, on the console, on a window, anything!).
 
##High-Level
(For more specific documentation, see the comments in code.)
Both scripts require inputs of integers when prompted. 

tree.py 

	This script contains 3 classes: Node, BinaryTree, and BinaryTreePrinter.
	Node defines the the class for each node in the tree. 
	BinaryTree defines the class that builds trees from a root node given a builder function. 
	The builder function in BinaryTree allows the BinaryTree to determine how to calculate the values for
	the node based on its parent.
	BinaryTreePrinter prints a BinaryTree. 

tree2.py

	This script uses a simple algorithm to calculate subsequent depths of values
	in the required binary tree. The algorithm adds a "1" at the ends of a new line,
	reads the previous line, adds the sum of every (i,i+1) element in the previous line
	twice in the new line.
	prints out the tree using a similar printer as tree.py
