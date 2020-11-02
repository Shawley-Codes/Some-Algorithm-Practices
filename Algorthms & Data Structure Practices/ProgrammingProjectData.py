#Scott Hawley
#Data Structures and Algorithms
#4/19

"""
Programming Project: Serialize/Deserialize Binary Tree
"""

#Create a Binary Tree Node
class BtNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#in order traversal to print Binary Tree
def inorder(root):
    #check for empty value to end recursion
    if (not root):
        return
    #recursively print each value
    inorder(root.left)
    print(root.data,end = " ") #print data to same line
    inorder(root.right)

class BtSerializerDeserializer:
    """
    using recursion to traverse and serialize the tree
        what this means:
    append ? to where additional nodes could be placed
    the whole line becomes a string, and no longer is a Binary Tree
    a string will print the data in preorder form rather than inorder
    """
    def serialize(self, root):
        #created a local to be called recursively
        def recur(node):
            if node:
                vals.append(str(node.data))
                recur(node.left)
                recur(node.right)
            else:
                vals.append("?")
        #call the initial recursion after creating a temp list
        #then return a string
        vals = []
        recur(root)
        return ' '.join(vals)

    #should recreate the Binary Tree from a string
    def deserialize(self, data):
        #created a local function to be called recursively
        def recur():
            val = next(vals)
            if val == "?": #specific to this form of serialize
                return None
            #create a Binary Tree
            node = BtNode(int(val))
            node.left = recur()
            node.right = recur()
            return node #using return in local function after exploring
        #call the initial recursion after creating a list of data from the string
        vals = iter(data.split())
        deserializedNode = recur()
        return deserializedNode

    #use recursion to destroy tree, traverses tree first, then deletes
    #as a note, this does not seem to work
    def destroyRoot(self, root):
        if (root != None):
            self.destroyRoot(root.left)
            self.destroyRoot(root.right)
            del(root)

"""
Driver Code
"""
#create a tree
root = BtNode(15)
root.left = BtNode(22)
root.right = BtNode(3)
root.right.left = BtNode(14)
root.right.right = BtNode(5)

#in order traversal from left to root to right, space is to create new line
inorder(root)
print(" ")

#initialize
BTmanip = BtSerializerDeserializer()
BTmanip.deserialize(BTmanip.serialize(root))

#serialize and then print, cannot use in order
serialized = BTmanip.serialize(root)
BTmanip.destroyRoot(root)
print(serialized)


#deserialize creates a new Binary Tree
deserialized = BTmanip.deserialize(serialized)
inorder(deserialized)
