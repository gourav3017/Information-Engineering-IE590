import numpy as np
import itertools
import timeit
import matplotlib.pyplot as plt
m = int(input('number of clauses(rows), m = '))
n = int(input('number of literals(coloumns), n = '))

matrix = []; columns = []
# initialize the number of rows
for i in range(0,m):
    matrix += [0]
# initialize the matrix
for i in range (0,m):
    matrix[i] = [0]*n
for i in range (0,m):
    for j in range (0,n):
        print ('entry in row: ',i+1,' column: ',j+1)
        matrix[i][j] = int(input())
        if matrix[i][j]>1 or matrix[i][j]<-1:
            print("Invalid input:Enter correct input")
            print ('entry in row: ',i+1,' column: ',j+1)
            matrix[i][j]=int(input())
#print (matrix)
ct=0
matrix1 = np.array(matrix)
print(matrix1)
for row in matrix1:
    if any(i >0 for i in row):
        ct=ct+1
        print(row)
#x= np.where(matrix1.any(axis=1))[0]
#print(matrix1.any(axis=1))
#print(np.where(matrix1.any(axis=1)))
#print(x)
if ct!=m:
    print("Solution to the satisfiability problem doesnt exist")
else:
        print("Solution to the given satisfiability probelm is true")

'''---------'''

#below code to get the samples vs time output
'''

for n in range(10,21):
    matrix = []; columns = []
    # initialize the number of rows
    m=10
    for i in range(0,m):
        matrix += [0]
    # initialize the matrix
    for i in range (0,m):
        matrix[i] = [0]*n
    for i in range (0,m):
        for j in range (0,n):
            #print ('entry in row: ',i+1,' column: ',j+1)
            #matrix[i][j] = int(input())
            #if matrix[i][j]>1 or matrix[i][j]<-1:
                #print("Invalid input:Enter correct input")
                #print ('entry in row: ',i+1,' column: ',j+1)
            matrix[i][j]=np.random.randint(-1,1)
    #print (matrix)
    ct=0
    matrix1 = np.array(matrix)
    print(matrix1)
    row=[]
    start=0
    start = timeit.default_timer()
    
    for row in matrix1:
        if any(i >0 for i in row):
            ct=ct+1
            print(row)
    if ct!=m:
        print("Solution to the satisfiability problem is 0")
    else:
        print("Solution to satisfiability probelm is true")
    stop=0
    stop = timeit.default_timer()
    print("Time required for SAT with ",n," variables is:",stop-start)
    plt.plot(stop-start, n)
    plt.show()
