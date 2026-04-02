def add_binary(a, b):
    '''
    Given two strings perform binary addition and return the result as a string
    '''
    c=0
    d=0
    z=0
    x=""
    a=a.lstrip("0b")
    b=b.lstrip("0b")
    for i in range(len(a)):
        if a[i]=="1":
            c+= 2**((len(a))-i-1)
    for j in range(len(b)):
        if b[j]=="1":
            d+= 2**((len(b))-j-1)
    z= c+d
    while z>0:
        if z%2 ==1:
            x+="1"
            z-=1
            z=z/2
        else:
            x+="0"
            z=z/2
    x= x[::-1]
    return "0b"+x