def dif(A,n):
    D=[]
    for i in [0..len(A)-1]:
        for j in [0..len(A)-1]:
            if i!=j:
                D.append(mod(A[i]-A[j],n))
    R=[a for a in D]
    R.sort()
    return(R)

def code(i,j,k,p,m,t,a):
    D=[]
    for  l in [0..m-1]:
        D.append(crt(l-l,p^(1-k)*a^(40*i+j+t*l),m,p^2))
        D.sort()
    return(D)
    
def todos(p,m,t,a):
    H=[]
    for i in [0..p-1]:
        for j in [0..t-1]:
            H.append(dif(code(i,j,1,p,m,t,a),m*p^2))
    print(H)