"""
NeuroScouting Interview Tree

Usage: python tree2.py [starting value]

Description can be found in readme associated.
Interpretation 2 - node's sibling means any node on the same depth
author: Chris Lee
created: 11/11/2013
"""

#Because I already used a tree, I don't feel like using a tree again.
#Even though the tree takes in a general function to build the node.
#SKELETON TREES

def getNextLine(prev):
	newLine = []
	newLine.append(1)
	for i in range(len(prev) - 1):
		newLine += [prev[i] + prev[i + 1]]*2
	newLine.append(1)
	return newLine

"""
Stolen from binaryTree Printer in tree.py
edited to use list of lists
"""
def printOut(filepath, lines):
	lines = [[str(val) for val in line] for line in lines]
	maxWidth = getTreeWidth(lines)
	with open(filepath,'wb') as f:
		for line in lines:
			f.write(getLine(line, maxWidth))

def getLine(line, maxWidth):
	numSpaces = len(line) + 1
	spacing = maxWidth/numSpaces
	lineBuilder = ""
	for value in line:
		extra = (len(value) - 1)/2
		lineBuilder += (spacing - extra) * " " + value + (len(value) - 1 - extra) * " "
	lineBuilder += "\n"
	return lineBuilder
def getLine(line, ):

#get character width of printed tree
def getTreeWidth(lines):
	return sum([len(val) + 4 for val in lines[-1]])

if __name__ == "__main__":
	maxDepth = int(raw_input("How deep?"))
	lines = []
	lines.append([1])
	lines.append([1,1])
	for i in range(1,maxDepth):
		lines.append(getNextLine(lines[i]))
	printOut("./printedTree2.txt",lines)



