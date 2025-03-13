class matrix:
    def __init__(self):
        self.matrix = []
        self.row = 0
        self.col = 0
        self.create_matrix()

    def create_matrix(self):
        self.row = int(input("Enter the number of rows: "))
        self.col = int(input("Enter the number of columns: "))
        for i in range(self.row):
            a = []
            for j in range(self.col):
                a.append(int(input()))
            self.matrix.append(a)
        print(self.matrix)