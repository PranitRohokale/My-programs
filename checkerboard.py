import numpy as np

def checkerboard(n):
    if n%2!=0:
        return
    array=np.zeros((n,n),dtype=int)
    for i in range(1-n,n,2):
        array+=np.eye(n,k=i,dtype=int)
    return array

print(checkerboard(int(input("Enter the even no of Rows : "))))

