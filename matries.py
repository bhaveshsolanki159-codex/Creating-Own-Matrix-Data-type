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
            self.create_matrix(choice)
            self.addition()
        elif choice == 2:
            self.create_matrix(choice)
            self.subtraction()
        elif choice == 3:
            self.create_matrix(choice)
            self.multiplication()
        elif choice == 4:
            self.create_matrix(choice)
            self.division()
        elif choice == 5:
            self.create_single_matrix()
            self.transpose()
        elif choice == 6:
            self.determinant()
        elif choice == 7:
            self.inverse()
        elif choice == 8:
            self.rank()
        elif choice == 9:
            self.power()
        elif choice == 10:
            print("Exiting the program...")
            exit()
        else:
            print("Invalid choice!")
            self.choose_operation()
    
    def create_matrix(self, choice):
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
            self.create_matrix(choice)
                
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
    
    def addition(self):
        # Implement addition logic here
        pass

    def subtraction(self):
        # Implement subtraction logic here
        pass

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
