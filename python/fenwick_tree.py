class FenwickTree:
    def __init__(self, arr):
        self.size = len(arr) + 1
        self.nodes = [0] * self.size

        for i, a in enumerate(arr):
            self.add(i, a)

    def sum(self, indx):
        res = 0

        indx += 1

        while indx > 0:
            res += self.nodes[indx]

            indx -= indx & -indx

        return res

    def add(self, indx, delt):
        indx += 1

        while indx < self.size:
            self.nodes[indx] += delt

            indx += indx & -indx


A = FenwickTree([1, 2, 3, 4])

A.add(0, 9)

print(A.sum(2))

print(A.nodes)
