class QuickFind:
    def __init__(self, total_nodes):
        self.nodes_arr = [i for i in range(total_nodes)]

    def union(self, left, right):
        if self.nodes_arr[left] != self.nodes_arr[right]:
            for ind in range(len(self.nodes_arr)):
                if (self.nodes_arr[ind] == self.nodes_arr[left]):
                    self.nodes_arr[ind] = self.nodes_arr[right]

    def connected(self, left, right): 
        return self.nodes_arr[left] == self.nodes_arr[right]

    def find(self, node):
        for i in range(len(self.nodes_arr) - 1,-1, -1):
            a



total_nodes = input("Enter Total no. of nodes: ")
quick_find_instance = QuickFind(total_nodes=total_nodes)
quick_find_instance.union(0,1)
quick_find_instance.union(2,3)
quick_find_instance.union(1,3)
print(quick_find_instance.connected(0,4))