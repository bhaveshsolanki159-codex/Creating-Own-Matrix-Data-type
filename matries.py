class matrix:
    def __init__(self):
        self.matrix = []
        self.row = 0
        self.col = 0
        self.choose_operation()

    
    def choose_operation(self):
        print("Choose an operation:")
        print('''1. addition\n2. subtraction\n3. multiplication\n4. division\n5. transpose\n6. determinant\n7. inverse\n8. rank\n9. power\n10. exit\nEnter your choice: ''')
        choice = int(input())

        if choice == 1:
            no_of_matrix = int(input("Enter the number of matrices: "))
            self.create_matrix()
            self.addition(no_of_matrix)
        elif choice == 2:
            no_of_matrix = int(input("Enter the number of matrices: "))
            self.create_matrix()
            self.subtraction(no_of_matrix)
        elif choice == 3:
            no_of_matrix = int(input("Enter the number of matrices: "))
            self.create_matrix()
            self.multiplication(no_of_matrix)
        elif choice == 4:
            no_of_matrix = int(input("Enter the number of matrices: "))
            self.create_matrix()
            self.division(no_of_matrix)
        elif choice == 5:
            self.create_single_matrix()
            self.transpose()
        elif choice == 6:
            self.create_single_matrix()
            self.determinant()
        elif choice == 7:
            self.create_single_matrix()
            self.inverse()
        elif choice == 8:
            self.create_single_matrix()
            self.rank()
        elif choice == 9:
            self.create_single_matrix()
            self.power()
        elif choice == 10:
            print("Exiting the program...")
            exit()
        else:
            print("Invalid choice!")
            self.choose_operation()
    
    def create_matrix(self):
        try:
            no_of_matrix = int(input("Enter the number of matrices: "))
            for x in range(no_of_matrix):
                self.row = int(input("Enter the number of rows: "))  # n
                self.col = int(input("Enter the number of columns: "))  # m
                sample = []
                for i in range(self.row):
                    a = []
                    for j in range(self.col):
                        a.append(int(input(f"Enter element [{i}][{j}]: ")))
                    sample.append(a)
                self.matrix.append(sample)
            print(self.matrix)
        except ValueError:
            print("Invalid input! Please enter integers only.")
            self.create_matrix()
                
    def create_single_matrix(self):
        try:
            self.row = int(input("Enter the number of rows: "))  # n
            self.col = int(input("Enter the number of columns: "))  # m
            for i in range(self.row):
                a = []
                for j in range(self.col):
                    a.append(int(input(f"Enter element [{i}][{j}]: ")))
                self.matrix.append(a)
            print(self.matrix)
        except ValueError:
            print("Invalid input! Please enter integers only.")
            self.create_single_matrix()
    
    def addition(self, no_of_matrix):
        sample = self.matrix
        try:
            new_matrix = [[0,0],[0,0]] 
            for j in range(self.col):
                for i in range(self.row):
                    for y in range(no_of_matrix):
                        new_matrix[i][j] += sample[y][i][j]
                    # new_matrix.append(new_matrix[i][j])

            self.matrix = new_matrix
            print(self.matrix)
        except:
            print("Invalid logic")
        

    def subtraction(self, no_of_matrix):
        sample = self.matrix
        try:
            new_matrix = [[0,0],[0,0]] 
            for j in range(self.col):
                for i in range(self.row):
                    for y in range(no_of_matrix):
                        new_matrix[i][j] -= sample[y][i][j]
                    # new_matrix.append(new_matrix[i][j])

            self.matrix = new_matrix
            print(self.matrix)
        except:
            print("Invalid logic")

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


X = matrix()
