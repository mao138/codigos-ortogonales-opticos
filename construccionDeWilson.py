def Wilson(p,c):
    w=(p-1)/c
    b=(p-1) % c
    if b==0:
        P=Primes()
        if p in P:
            F.<a>=GF(p)
            t=F.multiplicative_generator()
            g=t^c
            Q=[]
            for i in [1..w]:
                Q.append(g^i)
            T=Set(Q)
            V=[]
            for i in [0..c-1]:
                U=[]
                for j in T:
                    U.append(j*t^i)
                V.append(U)
            print(V)
        else:
            print("p no es primo")
    else:
        print("c no divide a p-1")
