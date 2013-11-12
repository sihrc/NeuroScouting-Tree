"""
NeuroScouting Interview Tree

Usage: python tree.py [starting value]

Description can be found in readme associated.

author: Chris Lee
created: 11/11/2013
"""

#Node Class
"""
Parent (Parent Node)
Right (Right Node)
Left (Left Node)
Value (Node value)
"""
class Node:
	def __init__(self, parent, value):
		self.parent = parent
		self.value = value
		self.right = None
		self.left = None

	def setRight(self, rightNode):
		#Set the right child
		self.right = rightNode

	def setLeft(self, leftNode):
		#Set the left child
		self.left = leftNode

#BinaryTree Class
"""
startingValue (value of root node)
curDepth (current depth of tree)
root (root Node)
"""
class BinaryTree:
	def __init__(self, startingValue = 1):
		self.startingValue = startingValue
		self.curDepth = 0
		self.root = Node(False,startingValue)
			
	def buildStep(self):
		#Builds next level
		raise NotImplementedError, "Not yet implemented - working out recursion with nodes"
			



if __name__ == "__main__":
	startingValue = raw_input("Input a numerical value for the root node:")
	#print "Entered:", startingValue

	treeDepth = raw_input("How deep should I go?: ")
	#print "Outputting", treeDepth, "levels"

	#Create the Tree
	tree = BinaryTree(startingValue = startingValue)
	print tree.root.value
