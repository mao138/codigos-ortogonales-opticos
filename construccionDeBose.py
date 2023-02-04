def Bose(q):
    F.<a>=FiniteField(q^2)
    B=[]
    for i in [1..q]:
        B.append(discrete_log(a+i,a))
    print(B)