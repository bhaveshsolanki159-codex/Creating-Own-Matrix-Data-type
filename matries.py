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
            no_of_matrix = int(input("Enter the no of matries: "))
            for i in range(no_of_matrix):
                self.create_matrix()
            self.addition()
        elif choice == 2:
            self.subtraction()
        elif choice == 3:
            self.multiplication()
        elif choice == 4:
            self.division()
        elif choice == 5:
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
    
    def create_matrix(self):
        self.row = int(input("Enter the number of rows: "))
        self.col = int(input("Enter the number of columns: "))
        for i in range(self.row):
            a = []
            for j in range(self.col):
                a.append(int(input()))
            self.matrix.append(a)
        print(self.matrix)
    
    def addition(self):
        pass

        


X = matrix()

