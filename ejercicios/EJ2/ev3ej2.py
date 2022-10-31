def determinant(self,i=0)  # i can be any of the matrix's rows
    assert isinstance(self,Matrix)
    n,m = self.dim()    # Q.dim() returns the size of the matrix Q
    assert n == m
    if (n,m) == (1,1):
        return self[0,0]
    det = 0
    for j in range(n):
        det += ((-1)**(i+j))*(self[i,j])*((self.minor(i,j)).determinant())
    return det

def ej2():
    i=3
    determinant(i)
