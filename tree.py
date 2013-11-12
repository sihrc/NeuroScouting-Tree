"""
NeuroScouting Interview Tree

Usage: python tree.py [starting value]

Description can be found in readme associated.

author: Chris Lee
created: 11/11/2013
"""

#Node Class
"""
Attributes:
	Parent (Parent Node)
	Right (Right Node)
	Left (Left Node)
	Value (Node value)
	leftOrRight ("right" or "left" whether node is a right child or left child, "none" for root)

Public Methods:
	isRoot() returns True (if node is root) else False
	isLeft() returns True (if node is left child) else False
	isRight() returns True (if node is right child) else False
"""
class Node:
	def __init__(self, parent, value, leftOrRight):
		self.parent = parent
		self.value = value
		self.right = False
		self.left = False
		self.leftOrRight = leftOrRight

	def isRoot(self):
		return self.parent == False

	def isLeft(self):
		return self.leftOrRight == "left"
	
	def isRight(self):
		return self.leftOrRight == "right"

#BinaryTree Class
"""
Attributes:
	root (root Node)
	startingValue (value of root node)
	curDepth (current depth of tree)
	maxDepth (maximum depth of tree)

Methods:
	build - returns none -> builds the tree based on an input builder function
"""
class BinaryTree:
	def __init__(self, startingValue = 1, maxDepth = 5):
		self.startingValue = startingValue
		self.curDepth = 0
		self.root = Node(False,startingValue,"None")
		self.maxDepth = maxDepth
	
	#builds the tree
	def build(self, builder):
		self.root = self.privateBuild(self.root, builder, 0)

	#private methods called only by the class itself
	def privateBuild(self, node, builder, depth):
		node.left = builder(node,"left") #grab values for nodes
		node.right = builder(node,"right")
		if depth < self.maxDepth:
			node.left = self.privateBuild(node.left, builder, depth + 1) #recurse
			node.right = self.privateBuild(node.right, builder, depth + 1)
		return node


#BinaryTreePrinter Class
"""
Attributes:
	binaryTree (binaryTree)
	maxDepth (maximum depth of tree)
	
Public Methods:
	printOut - takes in filepath returns none - outputs the tree printed in the file specified at the filepath
"""
class BinaryTreePrinter:
	def __init__(self, binaryTree = BinaryTree()):
		self.binaryTree = binaryTree
		self.maxDepth = binaryTree.maxDepth

	#writes the tree to file
	def printOut(self,filepath):
		nodes = self.getNodes()

	#get character width of printed tree
	def getTreeWidth(self, nodeDict):
		return sum([len(str(node.value)) for node in nodeDict[self.maxDepth]])

	#gets all nodes in the tree
	def getNodes(self):
		return self.privateGetNodes(self.root, dict(), 0)
	
	def privateGetNodes(self,node,nodes,depth):
		nodes[depth] = nodes.get(depth,[]) + [node]
		nodes = self.privateGetNodes(node.left, nodes, depth + 1) if node.left else nodes
		nodes = self.privateGetNodes(node.right, nodes, depth + 1) if node.right else nodes
		return nodes


#Builder Function
"""
Required by the BinaryTree class
Defining the builder function for this tree (or the tree's rules, so to speak)
Here is where the values of nodes are determined based on whether the node is a left or right node.
Returns node given the parent node and whether it's a left or right node
"""
def nextNode(parent, leftOrRight):
	value = parent.value
	if not parent.isRoot():
		if (leftOrRight == "right" and parent.isLeft()):
			value += parent.parent.right.value
		if (leftOrRight == "left" and parent.isRight()):
			value += parent.parent.left.value
	return Node(parent, value, leftOrRight)


if __name__ == "__main__":
	#startingValue = raw_input("Input a numerical value for the root node:")
	#print "Entered:", startingValue

	#treeDepth = raw_input("How deep should I go?: ")
	#print "Outputting", treeDepth, "levels"

	#Create the Tree
	tree = BinaryTree()#startingValue = startingValue, maxDepth = treeDepth)
	tree.build(nextNode)
	
	treePrinter = BinaryTreePrinter(tree)
	treePrinter.printOut("./printedTree")


