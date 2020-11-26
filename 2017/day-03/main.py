import numpy as np

n = 289326

# PART 1 ======================================================================

class Box:
    def __init__(self):
        self.box = np.array([[1]])
        self.current = 1

    def r_append(self):
        nrow = self.box.shape[0]
        new_col = np.arange(
            self.current + 1,
            self.current + 1 + nrow
        )[::-1].reshape(-1, 1)
        self.box = np.hstack([self.box, new_col])
        self.current += nrow

    def u_append(self):
        ncol = self.box.shape[1]
        new_row = np.arange(
            self.current + 1,
            self.current + 1 + ncol
        )[::-1].reshape(1, -1)
        self.box = np.vstack([new_row, self.box])
        self.current += ncol

    def l_append(self):
        nrow = self.box.shape[0]
        new_col = np.arange(
            self.current + 1,
            self.current + 1 + nrow
        ).reshape(-1, 1)
        self.box = np.hstack([new_col, self.box])
        self.current += nrow

    def d_append(self):
        ncol = self.box.shape[1]
        new_row = np.arange(
            self.current + 1,
            self.current + 1 + ncol
        ).reshape(1, -1)
        self.box = np.vstack([self.box, new_row])
        self.current += ncol

    def add_layer(self):
        self.r_append()
        self.u_append()
        self.l_append()
        self.d_append()

    def dist_to_n(self, n):
        r_o, c_o = np.where(self.box == 1)
        r, c = np.where(self.box == n)
        return (abs(r - r_o) + abs(c - c_o))[0]

    def __repr__(self):
        return str(self.box)


box = Box()
for _ in range(500):
    box.add_layer()

print(box.dist_to_n(n))

# PART 2 ======================================================================
class Box:
    def __init__(self):
        self.box = np.array([
            [5, 4, 2],
            [10, 1, 1],
            [11, 23, 25]
        ])

    def r_append(self):
        nrow = self.box.shape[0]
        new_col = np.zeros(nrow)

        # First (most southern element)
        new_col[-1] = self.box[-1, -1] + self.box[-2, -1]        

        for i in range(1, nrow - 1)[::-1]:
            new_col[i] = \
                self.box[i - 1, -1] + \
                self.box[i    , -1] + \
                self.box[i + 1, -1] + \
                new_col[i + 1]

        # Last (most northern element)
        new_col[0] = self.box[0, -1] + self.box[1, -1] + new_col[1]

        self.box = np.hstack([self.box, new_col.reshape(-1, 1)])

    def u_append(self):
        ncol = self.box.shape[1]
        new_row = np.zeros(ncol)
        
        # First (most eastern element)
        new_row[-1] = self.box[0, -1] + self.box[0, -2]

        for i in range(1, ncol - 1)[::-1]:
            new_row[i] = \
                self.box[0, i - 1] + \
                self.box[0, i    ] + \
                self.box[0, i + 1] + \
                new_row[i + 1]

        # Last (most western element)
        new_row[0] = self.box[0, 0] + self.box[0, 1] + new_row[1]

        self.box = np.vstack([new_row.reshape(1, -1), self.box])

    def l_append(self):
        nrow = self.box.shape[0]
        new_col = np.zeros(nrow)

        # First (most northern element)
        new_col[0] = self.box[0, 0] + self.box[1, 0]

        for i in range(1, nrow - 1):
            new_col[i] = \
                new_col[i - 1] + \
                self.box[i - 1, 0] + \
                self.box[i    , 0] + \
                self.box[i + 1, 0]

        # Last (most southern element)
        new_col[-1] = self.box[-1, 0] + self.box[-2, 0] + new_col[-2]

        self.box = np.hstack([new_col.reshape(-1, 1), self.box])

    def d_append(self):
        ncol = self.box.shape[1]
        new_row = np.zeros(ncol)
        
        # First (most eastern element)
        new_row[0] = self.box[-1, 0] + self.box[-1, 1]

        for i in range(1, ncol - 1):
            new_row[i] = \
                new_row[i - 1] + \
                self.box[-1, i - 1] + \
                self.box[-1, i    ] + \
                self.box[-1, i + 1]

        # Last (most western element)
        new_row[-1] = new_row[-2] + self.box[-1, -2] + self.box[-1, -1]

        self.box = np.vstack([self.box, new_row.reshape(1, -1)])

    def add_layer(self):
        self.r_append()
        self.u_append()
        self.l_append()
        self.d_append()

box = Box()
while np.all(box.box <= n):
    box.add_layer()

