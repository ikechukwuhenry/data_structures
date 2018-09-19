import random
import unittest


class TreeNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


def insert(root, x):
    if root is None:
        return TreeNode(x)
    new_root = TreeNode(root.key)
    if root.key <= x:
        new_root.left = root.left
        new_root.right = insert(root.right, x)
    else:
        new_root.left = insert(root.left, x)
        new_root.right = root.right
    return new_root


def to_list(node):
    if node is None:
        return []
    return to_list(node.left) + [node.key] + to_list(node.right)


def inorder_walk(tree):
    if tree is not None:
        inorder_walk(tree.left)
        print(tree.key)
        inorder_walk(tree.right)


def pre_order_walk(tree):
    if tree is not None:
        print(tree.key)
        pre_order_walk(tree.left)
        pre_order_walk(tree.right)


def post_order_walk(tree):
    if tree is not None:
        post_order_walk(tree.left)
        post_order_walk(tree.right)
        print(tree.key)


def search_tree(tree, x):
    if tree is None or x == tree.key: return tree
    if x < tree.key: return search_tree(tree.left, x)
    return search_tree(tree.right, x)


def iterative_search(tree, x):
    while tree is not None and x != tree.key:
        if x < tree.key:
            tree = tree.left
        else:
            tree = tree.right
    return tree


def tree_minimum(tree):
    while tree.left is not None:
        tree = tree.left
    return tree


def tree_maximum(tree):
    while tree.right is not None:
        tree = tree.right
    return tree


def successor(node):
    if node.right is not None:
        return tree_minimum(node.right)


def predecessor(node):
    return tree_maximum(node.left)


class ProblemTestCase(unittest.TestCase):

    def test_case(self):
        t1 = insert(None, 41)
        t2 = insert(t1, 38)
        t3 = insert(t2, 31)
        t4 = insert(t3, 12)
        t5 = insert(t4, 19)
        t6 = insert(t5, 8)
        find = search_tree(t6, 41)
        print("searching")
        if find: print(find.key)
        print(find)
        find2 = iterative_search(t6, 0)
        print(find2)
        print("beginning of in order tree walk")
        inorder_walk(t6)
        print("end of inorder")
        print("beginning of pre order walk")
        pre_order_walk(t6)
        print("beginning of post order walk")
        post_order_walk(t6)
        print("tree minimum: ")
        min = tree_minimum(t6)
        print(min.key)
        print("tree maximum: ")
        max = tree_maximum(t6)
        print(max.key)
        print("successor")
        successorvalue = successor(t3)
        self.assertEqual(to_list(t1), [41])
        self.assertEqual(to_list(t2), [38, 41])
        self.assertEqual(to_list(t3), [31, 38, 41])
        self.assertEqual(to_list(t4), [12, 31, 38, 41])
        self.assertEqual(to_list(t5), [12, 19, 31, 38, 41])
        self.assertEqual(to_list(t6), [8, 12, 19, 31, 38, 41])


if __name__ == '__main__':
    unittest.main()