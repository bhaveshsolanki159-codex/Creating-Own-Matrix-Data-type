class Vector:
    def __init__(self):
        self.vectors = []
        self.size = 0
        self.choose_operation()

    def choose_operation(self):
        print("\nChoose a Vector operation:")
        print("""1. addition
        2. subtraction
        3. dot product
        4. scalar multiplication
        5. magnitude
        6. exit
        Enter your choice:""")
        choice = int(input())

        if choice == 1:
            self.create_vectors(2)
            self.addition()
        elif choice == 2:
            self.create_vectors(2)
            self.subtraction()
        elif choice == 3:
            self.create_vectors(2)
            self.dot_product()
        elif choice == 4:
            self.create_vectors(1)
            self.scalar_multiplication()
        elif choice == 5:
            self.create_vectors(1)
            self.magnitude()
        elif choice == 6:
            print("Exiting Vector Program...")
            exit()
        else:
            print("Invalid choice!")
            self.choose_operation()

    def create_vectors(self, n):
        try:
            self.vectors = []
            self.size = int(input("Enter vector size: "))

            for i in range(n):
                print(f"Enter elements for Vector {i+1}:")
                vec = [int(input(f"Element[{j}]: ")) for j in range(self.size)]
                self.vectors.append(vec)

        except ValueError:
            print("Invalid input! Enter integers only.")
            self.create_vectors(n)

    def addition(self):
        v1, v2 = self.vectors
        result = [v1[i] + v2[i] for i in range(self.size)]

        print("Vector Addition Result:")
        print(result)

    def subtraction(self):
        v1, v2 = self.vectors
        result = [v1[i] - v2[i] for i in range(self.size)]

        print("Vector Subtraction Result:")
        print(result)

    def dot_product(self):
        v1, v2 = self.vectors
        result = 0

        for i in range(self.size):
            result += v1[i] * v2[i]

        print("Dot Product:", result)

    def scalar_multiplication(self):
        scalar = int(input("Enter scalar value: "))
        vec = self.vectors[0]

        result = [scalar * x for x in vec]

        print("Scalar Multiplication Result:")
        print(result)

    def magnitude(self):
        vec = self.vectors[0]
        mag = 0

        for x in vec:
            mag += x * x

        print("Magnitude of Vector:", mag ** 0.5)
