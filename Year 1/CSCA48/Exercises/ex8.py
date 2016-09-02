class BTNode(object):
    """A node in a binary tree."""

    def __init__(self, value, left=None, right=None):
        """(BTNode, int, BTNode, BTNode) -> NoneType
        Initialize this node to store value and have children left and right,
        as well as depth 0.
        """
        self.value = value
        self.left = left
        self.right = right
        self.depth = 0  # the depth of this node in a tree

    def __str__(self):
        return self._str_helper("")

    def _str_helper(self, indentation=""):
        """(BTNode, str) -> str
        Return a "sideways" representation of the subtree rooted at this node,
        with right subtrees above parents above left subtrees and each node on
        its own line, preceded by as many TAB characters as the node's depth.
        """
        ret = ""

        if(self.right is not None):
            ret += self.right._str_helper(indentation + "\t") + "\n"
        ret += indentation + str(self.value) + "\n"
        if(self.left is not None):
            ret += self.left._str_helper(indentation + "\t") + "\n"
        return ret

    def set_depth(self, new_val):
        '''(BTNode, int) -> NoneType
        Set the .depth parameter of all BTNodes in the tree rooted to the
        calling Node, starting at the provided value
        '''
        # Perform the change on the right node and left node (if they exist)
        # prior to doing so on the calling node
        if self.right:
            self.right.set_depth(new_val + 1)
        if self.left:
            self.left.set_depth(new_val + 1)
        self.depth = new_val

    def leaves_and_internals(self, is_root=True):
        '''(BTNode) -> tuple of sets
        Return a tuple contain two sets, one containing the values of all
        leaf nodes rooted to the calling node, the other containing the values
        of all internal nodes rooted the calling node.
        '''
        internals = set()
        leafs = set()
        # Base case
        # If the node is a leaf or the root
        if not self.left and not self.right:
            # Node is a leaf node
            return (set([self.value]), internals)
        else:
            # Node is an internal node
            if self.left:
                l_content = self.left.leaves_and_internals(False)
                internals.update(l_content[1])
                leafs.update(l_content[0])
            if self.right:
                r_content = self.right.leaves_and_internals(False)
                internals.update(r_content[1])
                leafs.update(r_content[0])
            if not is_root:
                internals.add(self.value)
            return (leafs, internals)

    def sum_to_deepest(self):
        '''(BTNode) -> int
        Returns the sum of all values on the path from this node to the
        deepest leaf node. If there are multiple leaves at the deepest level,
        return the maximum sum of those paths.
        '''
        return self.sum_to_deepest_helper()[1]

    def sum_to_deepest_helper(self):
        '''(BTNode) -> list of int
        Returns a list containing the distance from the calling node to its
        furthest leaf and the summation of all node values between the
        two nodes. In the event where there are more than one node with
        the maximum distance from the calling node, the path with the higher
        summation value will have its details returned
        '''
        ret = [0, 0]
        # Base case: calling node has no children
        if not self.left and not self.right:
            return [0, self.value]
        if self.left:
            ret = self.left.sum_to_deepest_helper()
        if self.right:
            r = self.right.sum_to_deepest_helper()
            if r[0] > ret[0] or r[1] > ret[1]:
                return [r[0] + 1, r[1] + self.value]
        return [ret[0] + 1, ret[1] + self.value]

if(__name__ == "__main__"):
    # just a simple tree to practice on
    my_tree = BTNode(10, BTNode(3, BTNode(5), BTNode(2)),
                     BTNode(7, BTNode(4, BTNode(9)), BTNode(6)))
    print(my_tree)
