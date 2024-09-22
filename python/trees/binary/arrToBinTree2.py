
class BinaryTreeNode:
    def __init__(self, data:any):
        self.data = data
        self.leftNode = None
        self.rightNode = None

class ArrayToBinaryTree:
    def __init__(self, array:list):
        self.array = array
        self.rootNode = None
    
    def left_child_index(index): 
        return 2 * index + 1
    
    def right_child_index(index):
        return 2 * index + 2
    
    def get_data(self, index):
        """Loops through the array to find the data at an index. If there is no data at that index, keep searching the array till you find the next data, else return None: meaning that the array holds no data from that index to the end of the array"""
        if(0 <= index < len(self.array)):
            for i in range(index, len(self.array)):
                if self.array[i]:
                    return self.array[i]     
        return None
    
    def assign_value_to_node(self, node:BinaryTreeNode, index):
        valueOfLeftNode = self.get_data(self.left_child_index(index))
        if(valueOfLeftNode):
            node.leftNode = BinaryTreeNode(valueOfLeftNode)
        valueOfRightNode = self.get_data(self.right_child_index(index))
        if(valueOfRightNode):
            node.rightNode = BinaryTreeNode(valueOfRightNode)
        

    def create_bin_tree(self):
        for i in self.array:
            value = self.array[i]
            if(value is not None):
                if(i == 0):
                    rootNode = self.rootNode = BinaryTreeNode(value)
                    self.assign_value_to_node(rootNode)
                    continue
                
                # LOOK FOR A BREADTH FIRST ALGORITHM TO CONTINUE INSERTING SO THAT YOU HAVE A BALANCED TREE!!!
                childNode = BinaryTreeNode(value)

                



 
