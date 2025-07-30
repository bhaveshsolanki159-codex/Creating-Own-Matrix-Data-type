

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
        # Implement multiplication logic here
        pass

    def division(self):
        # Implement division logic here
        pass

    def transpose(self):
        # Implement transpose logic here
        pass

    def determinant(self):
        # Implement determinant logic here
        pass

    def inverse(self):
        # Implement inverse logic here
        pass

    def rank(self):
        # Implement rank logic here
        pass

    def power(self):
        # Implement power logic here
        pass


X = Matrix()


