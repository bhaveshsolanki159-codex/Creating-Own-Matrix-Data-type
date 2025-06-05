x = 2 

n = 2
m = 2

matries = list(range(x))
try:
    for y in range(x):
        
        sample = []
        for i in range (n):
            a =[]
            for j in range (m):
                a.append(int(input()))
            sample.append(a)
        matries[y] = sample
        print(matries[y])
except:
    print("not valid")
print(matries)

try:
    new_matrix = [[0,0],[0,0]] 
    for j in range(m):
        for i in range(n):
            for y in range(x):
                new_matrix[i][j] += matries[y][i][j]
            # new_matrix.append(new_matrix[i][j])

    print(new_matrix)
except:
    print("Invalid logic")





# class customer:
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender

# def greet(c1):
#     if c1.gender == "male":
#         print("Welcome Mr.", c1.name)
#     else:
#         print("Welcome Ms.", c1.name)

# cust = customer("Harry", "male")
# greet(cust)

