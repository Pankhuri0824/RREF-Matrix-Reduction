import math

#Finding RREF Steps

#m=[]
matrix=[]

f=open("./rref.txt","r")
for line in f:
    a=line.split()
    row=[]
    for l in a:
        l=int(l) #making all entries as integers rathar than strings
        row.append(l)
    matrix.append(row)
#Input matrix achieved : print(matrix)

#Finding RREF Steps
rows=len(matrix) #number of rows in matrix
for i in matrix:
    a=len(i)
coloumns=a #number of coloumns in matrix


def swap (one,two): #swap row one with row 2 WORKS
    r1=[]
    r2=[]
    for i in matrix:
        if(i==matrix[one]):
            r1=matrix[one]
        elif(i==matrix[two]):
            r2=matrix[two]

    matrix[one]=r2
    matrix[two]=r1


def PivotOne(): #WORKS find the smallest non zero first entry and swap
    #ele=matrix[0][0]
    int=0
    for i in matrix:
        ele=matrix[0][0]
        if (i[0]!=0) and (i[0]<ele or ele==0):
            swap(0,int)
        int+=1

def findPivCol(row): #return col number of the pivot in the row
    int=0
    col=coloumns+1 # if no pivot exists return this value for avoiding calling finalCol since the row is already dealth with
    for i in matrix[row]:
        if i!=0:
            col=int
            break
        int+=1
    return col

def finalCol(piv,pivrow,pivcol):
    # for things in the pivcol to be 0, subtract the pivrow from other rows
    # piv=matrix[0][0]
    for i in range (0,rows):
        if(i==pivrow):
            pass
        else:
            fac=piv*matrix[i][pivcol] # some error
            for j in range (coloumns):
                a=matrix[i][j]
                a=a-fac*matrix[pivrow][j]
                matrix[i][j]=a

# for pivot cases:
# first entry 1 , first entry 0, first entry non zero non 1
# which can be simplified : we just need to find the smallest non zero first entry and swap
PivotOne() 
# now if pivot entry isn't 1, divide it and the entrie row by itself
div=matrix[0][0]
if(div!=0):
    for i in range(coloumns):
        matrix[0][i]=(matrix[0][i]/div)
#we now have a matrix with the pivot entry as one

# apply the finalCol on each row
for i in range (rows):
    piv=findPivCol(i)
    if(piv==coloumns+1):
        pass
    else:
        # now if pivot entry isn't 1, divide it and the entrie row by itself
        div=matrix[i][piv]
        for j in range(coloumns):
            matrix[i][j]=(matrix[i][j]/div)
        finalCol(matrix[i][piv],i,piv)

#swap rows in decreasing pivot position order
for i in range (rows):
    for j in range(i,rows):
        r=i
        if findPivCol(r)>findPivCol(j) and findPivCol(r)!=coloumns+1 and findPivCol(j)!=coloumns+1:
            swap(r,j)

#pivot matrix for printing
pivpos=[]
for i in range (rows):
    a=findPivCol(i)
    if (a==(coloumns+1)):
        a="Null"
    pivpos.append((i,a))

print("Pivot Positions:")
print(pivpos)

print("The Row Reduced Echelon Matrix is :")
for i in range (rows):
        print('  '.join(map(str, matrix[i])))
    
