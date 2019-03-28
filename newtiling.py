import numpy as np
import datetime

def slv(n,x,y,xd,yd):    
    if n==1:
        bound = 2**n-1
        coord=[]
        if x < bound/2+xd and y < bound/2+yd:
            arr[2**(n-1)-1+xd][2**(n-1)+yd] = f[0]
            arr[2**(n-1)+xd][2**(n-1)-1+yd] = f[0]
            arr[2**(n-1)+xd][2**(n-1)+yd] = f[0]
            f[0]+=1
        if x < bound/2+xd and y > bound/2+yd:
            arr[2**(n-1)-1+xd][2**(n-1)-1+yd] = f[0]
            arr[2**(n-1)+xd][2**(n-1)-1+yd] = f[0]
            arr[2**(n-1)+xd][2**(n-1)+yd] = f[0]
            f[0]+=1
        if x > bound/2+xd and y> bound/2+yd:
            arr[2**(n-1)-1+xd][2**(n-1)-1+yd] = f[0]
            arr[2**(n-1)-1+xd][2**(n-1)+yd] = f[0]
            arr[2**(n-1)+xd][2**(n-1)-1+yd] = f[0]
            f[0]+=1
        if x > bound/2+xd and y < bound/2+yd:
            arr[2**(n-1)-1+xd][2**(n-1)-1+yd] = f[0]
            arr[2**(n-1)-1+xd][2**(n-1)+yd] = f[0]
            arr[2**(n-1)+xd][2**(n-1)+yd] = f[0]
            f[0]+=1
            
    if n>1:
        bound = 2**n-1
        coord=[]
        if x < bound/2+xd and y < bound/2+yd:
            arr[2**(n-1)-1+xd][2**(n-1)+yd] = f[0]
            arr[2**(n-1)+xd][2**(n-1)-1+yd] = f[0]
            arr[2**(n-1)+xd][2**(n-1)+yd] = f[0]
            coord.append((x,y))
            coord.append((2**(n-1)-1+xd, 2**(n-1)+yd))
            coord.append((2**(n-1)+xd, 2**(n-1)-1+yd))
            coord.append((2**(n-1)+xd, 2**(n-1)+yd))
            f[0]+=1
        if x < bound/2+xd and y > bound/2+yd:
            arr[2**(n-1)-1+xd][2**(n-1)-1+yd] = f[0]
            arr[2**(n-1)+xd][2**(n-1)-1+yd] = f[0]
            arr[2**(n-1)+xd][2**(n-1)+yd] = f[0]
            coord.append((2**(n-1)-1+xd, 2**(n-1)-1+yd))
            coord.append((x,y))
            coord.append((2**(n-1)+xd,2**(n-1)-1+yd))
            coord.append((2**(n-1)+xd, 2**(n-1)+yd))
            f[0]+=1
        if x > bound/2+xd and y> bound/2+yd:
            arr[2**(n-1)-1+xd][2**(n-1)-1+yd] = f[0]
            arr[2**(n-1)-1+xd][2**(n-1)+yd] = f[0]
            arr[2**(n-1)+xd][2**(n-1)-1+yd] = f[0]
            coord.append((2**(n-1)-1+xd, 2**(n-1)-1+yd))
            coord.append((2**(n-1)-1+xd, 2**(n-1)+yd))
            coord.append((2**(n-1)+xd, 2**(n-1)-1+yd))
            coord.append((x,y))
            f[0]+=1
        if x > bound/2+xd and y < bound/2+yd:
            arr[2**(n-1)-1+xd][2**(n-1)-1+yd] = f[0]
            arr[2**(n-1)-1+xd][2**(n-1)+yd] = f[0]
            arr[2**(n-1)+xd][2**(n-1)+yd] = f[0]
            coord.append((2**(n-1)-1+xd, 2**(n-1)-1+yd))
            coord.append((2**(n-1)-1+xd, 2**(n-1)+yd))
            coord.append((x,y))
            coord.append((2**(n-1)+xd, 2**(n-1)+yd))
            f[0]+=1
        slv(n-1,coord[0][0],coord[0][1],xd,yd)
        slv(n-1,coord[1][0],coord[1][1],xd,yd+2**(n-1))
        slv(n-1,coord[2][0],coord[2][1],xd+2**(n-1),yd)
        slv(n-1,coord[3][0],coord[3][1],xd+2**(n-1),yd+2**(n-1))

arr = np.array([])
inp = int(input("Enter n : "))
x,y = [int(i) for i in input("please enter the coord : ").split(",")]

n=2**inp
arr.resize(n,n)
arr[x][y]=1
f=[2]
now = datetime.datetime.now()
slv(inp,x,y,0,0)
print (datetime.datetime.now()-now)
print (arr)
