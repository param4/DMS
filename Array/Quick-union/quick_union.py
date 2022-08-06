class QuickUnion:
    def __init__(self, total_nodes):
        self.node_arr = list(range(total_nodes))

    def find_root(self, child_node):
        parent_node = self.node_arr[child_node]
        if (child_node == parent_node):
            return child_node
        return self.find_root(parent_node)

    def union(self, left, right):
        left_root = self.find_root(left)
        right_root = self.find_root(right)
        self.node_arr[left_root] = right_root

    def connected(self, left, right):
        return self.find_root(left) == self.find_root(right)



quick_union = QuickUnion(10)
quick_union.union(4,3)
quick_union.union(3,8)
quick_union.union(6,5)
quick_union.union(9,4)
quick_union.union(2,1)
print(quick_union.connected(8,9))
print(quick_union.connected(5,4))
quick_union.union(5,0)
quick_union.union(7,2)
quick_union.union(6,1)
quick_union.union(7,3)
print(quick_union.node_arr)



