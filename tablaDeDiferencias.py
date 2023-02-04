def trianglesetm(X,Y,n):
    k=len(X);
    m = matrix(QQ, k, k, lambda i, j:mod(Y[j]-X[i],n));
    return(m)