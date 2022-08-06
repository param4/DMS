class QuickUnionImproved:
    def __init__(self, total_nodes):
        self.node_arr = list(range(total_nodes))
        self.size_arr = [1]*total_nodes

    def find_root(self, child_node):
        parent_node = self.node_arr[child_node]
        if (child_node == parent_node):
            return child_node
        return self.find_root(parent_node)

    def connected(self, left, right):
        return self.find_root(left) == self.find_root(right)

    def union(self, left, right):
        left_root = self.find_root(left)
        right_root = self.find_root(right)

        if (left_root == right_root):
            return 
        
        if (self.size_arr[left_root] < self.size_arr[right_root]):
            self.node_arr[left_root] = right_root
            self.size_arr[right_root] += self.size_arr[left_root]
        else:
            self.node_arr[right_root] = left_root
            self.size_arr[left_root] += self.size_arr[right_root]


quick_union = QuickUnionImproved(10)
quick_union.union(4,3)
quick_union.union(3,8)
quick_union.union(6,5)
print(quick_union.size_arr)

quick_union.union(9,4)
quick_union.union(2,1)
print(quick_union.connected(8,9))
print(quick_union.connected(5,4))
print(quick_union.node_arr)