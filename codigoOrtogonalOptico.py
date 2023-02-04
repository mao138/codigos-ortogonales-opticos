def COO(T,n,a,c):
    for X in T:
        for Y in T:
            if X==Y:
                for t in Set(Integers(n)).difference({0}):
                    C=Set([y+t for y in Y ])
                    if len(C.intersection(X))>a:
                        return 0
            else:
                for t in Integers(n):
                    C=Set([y+t for y in Y ])
                    if len(C.intersection(X))>c:
                        return 0
        return 1#