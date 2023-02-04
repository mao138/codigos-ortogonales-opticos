def moreno(q,m):
    P.<x>=PolynomialRing(GF(q))
    K.<a>=GF(q^m, name='a')
    f=K.modulus()
    L=[]
    for g in [1..m-1]:
        T=[]
        for p in P.monics( of_degree = g):
            T.append(p)
        L.append(T)
    R=[]
    for k in [0..m-2]:
        n=len(L[k])
        e=Integer(n/q)
        for j in [0..e-1]:
            X=[]
            for i in [0..q-1]:
                X.append(log(L[k][q*j+i](a),a))
                X.sort()
            R.append(X)
    return R
