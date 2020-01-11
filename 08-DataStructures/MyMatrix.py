import random


class matrix():

    @staticmethod
    def create(x,y):
        return[[0 for _ in range(y)] for _ in range(x)]

    @staticmethod
    def print(matrix):
        for row in matrix:
            print(row)
            
    @staticmethod
    def create_unit(x):
        m = matrix.create(x, x)
        for i in range(len(m)):
            m[i][i] = 1
        return m

    @staticmethod
    def fill_random(matrix, m, n):
        return [[random.randint(m, n) for _ in range(len(matrix[i]))] for i in range(len(matrix))]
    #[[random.randint(m, n) for _ in range(len(matrix[i]))] for i in range(len(matrix))] 
    # tworzy losowa liczbe z przedziłu (m,n)  ["i" to ile tego bedzie], ile w jednej liscie jest elementów a potem ilosc tych list


    @staticmethod
    def transpose(matrix):
        return[[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

n = matrix.create(3,5)
i = matrix.fill_random(n, 1, 9)
j = matrix.transpose(i)
matrix.print(j)
    

#m = matrix.create(4,3)
#matrix.print(m)


#j = matrix.create_unit(5)
#matrix.print(j)

#n = matrix.create(3,5)
#i = matrix.fill_random(n, 5, 9)
#matrix.print(i)




            
