# the array stores the information. We are not creating any new nodes, we are just trying the access the array from a binary tree approach so that search operations are optimised. We want to traverse the array in a binary tree way
binary_tree_array = ["R", "A", "B", "C", "D", "E", "F", None, None, None, None, None, None, "G"]

def left_child_index(index: int):
    return 2 * index + 1

def right_child_index(index:int):
    return 2 * index + 2

def pre_order_tree_traversal(index: int):
    if index >= len(binary_tree_array) or binary_tree_array[index] is None:
        return []
    return [binary_tree_array[index]] + pre_order_tree_traversal(left_child_index(index)) + pre_order_tree_traversal(right_child_index(index))

def in_order_tree_traversal(index:int):
    if index >= len(binary_tree_array) or binary_tree_array[index] is None:
        return []
    return in_order_tree_traversal(left_child_index(index)) + [binary_tree_array[index]] + in_order_tree_traversal(right_child_index(index)) 

def post_order_tree_traversal(index: int):
    if index >= len(binary_tree_array) or binary_tree_array[index] is None:
        return []
    return post_order_tree_traversal(left_child_index(index)) + post_order_tree_traversal(right_child_index(index)) + [binary_tree_array[index]]



print("pre order traversal")
print(pre_order_tree_traversal(0))

print("In order traversal")
print(in_order_tree_traversal(0))

print("post order traversal")
print(post_order_tree_traversal(0))



