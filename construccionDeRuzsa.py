def Ruzsa(p,r):
    A=[]
    for i in [1..p-1]:
        A.append(mod(p*i-(p-1)*r^i,p*(p-1)))
    print(A)