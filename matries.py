

class Matrix:
    def __init__(self):
        self.matrices = [] #for list of matrices
        self.col = 0
        self.row = 0
        self.choose_operation()

    
    def choose_operation(self):
        print("Choose an operation:")
        print('''1. addition\n2. subtraction\n3. multiplication\n4. division\n5. transpose\n6. determinant\n7. inverse\n8. rank\n9. power\n10. exit\nEnter your choice: ''')
        choice = int(input())

        if choice == 1:
            n = int(input("Enter the number of matrices: "))
            self.create_matrices(n)
            self.addition(n)
        elif choice == 2:
            n = int(input("Enter the number of matrices: "))
            self.create_matrices(n)
            self.subtraction(n)
        elif choice == 3:
            n = int(input("Enter the number of matrices: "))
            self.create_matrices(1)
            self.multiplication()
        elif choice == 4:
            n = int(input("Enter the number of matrices: "))
            self.create_matrices(1)
            self.division()
        elif choice == 5:
            self.create_matrices(1)
            self.transpose()
        elif choice == 6:
            self.create_matrices(1)
            self.determinant()
        elif choice == 7:
            self.create_matrices(1)
            self.inverse()
        elif choice == 8:
            self.create_matrices(1)
            self.rank()
        elif choice == 9:
            self.create_matrices(1)
            self.power()
        elif choice == 10:
            print("Exiting the program...")
            exit()
        else:
            print("Invalid choice!")
            self.choose_operation()
    
    def create_matrices(self, n):
        try:
            self.matrices = []
            print("Enter the number of rows and columns for all matrices (they must be the same for addition/subtraction):")
            self.row = int(input("Rows: "))
            self.col = int(input("Columns: "))
            for k in range(n):
                print(f"Enter elements for Matrix {k+1}:")
                self.matrices.append(self.get_matrix_input(self.row, self.col))
        except ValueError:
            print("Invalid input! Please enter integers only.")
            self.create_matrices(n)
                
    def get_matrix_input(self, row, col):
        try:
            return [[int(input(f"Element[{i}][{j}]: ")) for j in range(col)] for i in range(row)]
        except ValueError:
            print("Invalid input! Please enter integers only.")
            return self.get_matrix_input(row, col)
        
    def addition(self, n):
        sample = self.matrices
        result = [[sample[0][i][j] for j in range(self.col)] for i in range(self.row)]

        for m in range(1, n):
            for i in range(self.row):
                for j in range(self.col):
                    result[i][j] += sample[m][i][j]

        print("Result of addition:")
        for row in result:
            print(row)
        self.matrices = result

        

    def subtraction(self, n):
        sample = self.matrices
        result = [[sample[0][i][j] for j in range(self.col)] for i in range(self.row)]

        for m in range(1, n):
            for i in range(self.row):
                for j in range(self.col):
                    result[i][j] -= sample[m][i][j]

        print("Result of subtraction:")
        for row in result:
            print(row)
        self.matrices = result


    def multiplication(self):
        print("Enter second matrix details for multiplication:")
        r2 = int(input("Rows: "))
        c2 = int(input("Columns: "))

        if self.col != r2:
            print("Matrix multiplication not possible!")
            return

        mat1 = self.matrices[0]
        mat2 = self.get_matrix_input(r2, c2)

        result = [[0 for _ in range(c2)] for _ in range(self.row)]

        for i in range(self.row):
            for j in range(c2):
                for k in range(self.col):
                    result[i][j] += mat1[i][k] * mat2[k][j]

        print("Result of multiplication:")
        for row in result:
            print(row)


    def division(self):
        print("Division means multiplying with inverse of second matrix")

        if self.row != self.col:
            print("Inverse not possible for non-square matrix")
            return

        inv = self.inverse(return_matrix=True)
        if inv is None:
            return

        mat = self.matrices[0]
        result = [[0 for _ in range(self.col)] for _ in range(self.row)]

        for i in range(self.row):
            for j in range(self.col):
                for k in range(self.col):
                    result[i][j] += mat[i][k] * inv[k][j]

        print("Result of division:")
        for row in result:
            print(row)


    def transpose(self):
        mat = self.matrices[0]
        result = [[mat[j][i] for j in range(self.row)] for i in range(self.col)]

        print("Transpose of matrix:")
        for row in result:
            print(row)


    def determinant(self, mat=None):
        if mat is None:
            mat = self.matrices[0]

        if self.row != self.col:
            print("Determinant only defined for square matrices")
            return

        if len(mat) == 1:
            return mat[0][0]

        if len(mat) == 2:
            det = mat[0][0]*mat[1][1] - mat[0][1]*mat[1][0]
            print("Determinant:", det)
            return det

        det = 0
        for c in range(len(mat)):
            sub = [row[:c] + row[c+1:] for row in mat[1:]]
            det += ((-1)**c) * mat[0][c] * self.determinant(sub)

        print("Determinant:", det)
        return det


    def inverse(self, return_matrix=False):
        mat = self.matrices[0]

        det = self.determinant(mat)
        if det == 0:
            print("Inverse not possible (determinant is 0)")
            return None

        n = len(mat)
        cofactors = []

        for i in range(n):
            cofactor_row = []
            for j in range(n):
                sub = [row[:j] + row[j+1:] for k, row in enumerate(mat) if k != i]
                cofactor_row.append(((-1)**(i+j)) * self.determinant(sub))
            cofactors.append(cofactor_row)

        adjoint = [[cofactors[j][i] for j in range(n)] for i in range(n)]
        inverse = [[adjoint[i][j]/det for j in range(n)] for i in range(n)]

        if return_matrix:
            return inverse

        print("Inverse matrix:")
        for row in inverse:
            print(row)


    def rank(self):
        mat = [row[:] for row in self.matrices[0]]
        rank = 0

        for r in range(self.row):
            if any(mat[r]):
                rank += 1
                for i in range(r+1, self.row):
                    if mat[i][r] != 0:
                        factor = mat[i][r] / mat[r][r]
                        for j in range(self.col):
                            mat[i][j] -= factor * mat[r][j]

        print("Rank of matrix:", rank)


    def power(self):
        if self.row != self.col:
            print("Power only defined for square matrices")
            return

        p = int(input("Enter power: "))
        result = self.matrices[0]

        for _ in range(p-1):
            temp = [[0]*self.col for _ in range(self.row)]
            for i in range(self.row):
                for j in range(self.col):
                    for k in range(self.col):
                        temp[i][j] += result[i][k] * self.matrices[0][k][j]
            result = temp

        print(f"Matrix raised to power {p}:")
        for row in result:
            print(row)



