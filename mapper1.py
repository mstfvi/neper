def mapper1(s):
    N1=0
    N2=0
    s1 = 0
    s2 = 0
    for i in (range(len(s))):
        if s1<1:
            s1 += s[i]
            N1 += 1
        if s2<1:
            s2 += 1-s[i]
            N2 += 1
    return ((N1+N2)/2,1)
