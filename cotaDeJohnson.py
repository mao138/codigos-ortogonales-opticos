def Johnson(n,w,l):
    if n>=w>l>=1:
        c=((n-l)/(w-l)).floor()
        for i in range(1,l):
            c=c*(n-(l-i))/(w-(l-i)).floor()
        d=(c/w).floor()
        print(d)
    else:
        print('Los valores de n, w y l deben cumplir n>=w>l>=1')