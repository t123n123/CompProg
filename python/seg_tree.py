class SegTree:
    def __init__(self, arr):
        self.size = len(arr) * 4
        self.last = len(arr) - 1
        self.nodes = [0] * self.size

        self.build_tree(arr=arr)

    def build_tree(self, arr, node=1, left=0, right=None):
        if right == None:
            right = self.last
        if left == right:
            self.nodes[node] = arr[left]
        else:
            mid = (left + right) // 2

            self.build_tree(arr, node * 2, left, mid)
            self.build_tree(arr, node * 2 + 1, mid + 1, right)

            self.nodes[node] = self.nodes[node * 2] + self.nodes[node * 2 + 1]

    def get_sum(self, range_l, range_r, node=1, node_l=0, node_r=None):
        if node_r == None:
            node_r = self.last
        if range_l > range_r:
            return 0
        if range_l == node_l and range_r == node_r:
            return self.nodes[node]

        mid = (node_l + node_r) // 2

        return self.get_sum(
            range_l, min(range_r, mid), node * 2, node_l, mid
        ) + self.get_sum(max(range_l, mid + 1), range_r, node * 2 + 1, mid + 1, node_r)

    def update(self, pos, new_val, node=1, node_l=0, node_r=None):
        if node_r == None:
            node_r = self.last
        if node_l == node_r:
            self.nodes[node] = new_val
        else:
            mid = (node_l + node_r) // 2

            if pos <= mid:
                self.update(pos, new_val, node * 2, node_l, mid)
            else:
                self.update(pos, new_val, node * 2 + 1, mid + 1, node_r, pos, new_val)

            self.nodes[node] = self.nodes[node * 2] + self.nodes[node * 2 + 1]


A = SegTree([1, 2, 3, 4])

A.update(0, 10)

print(A.get_sum(0, 2))

print(A.nodes)
