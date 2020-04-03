def karatsuba(x1, x2):
    """This function multiplies two integers using the karatsuba algorithm"""
    x1 = str(x1)
    x2 = str(x2)
    
    if len(x1)==1 and len(x2)==1: #base case
        product = int(x1)*int(x2)
        return product
    
    else: #recursive solution
        x1, x2 = normalize_len(x1, x2)
        i = len(x1)//2

        a = int(x1[:i])
        b = int(x1[i:])
        c = int(x2[:i])
        d = int(x2[i:])
        
        s1 = karatsuba(a,c)
        s2 = karatsuba(b,d)
        s3 = karatsuba(a+b,c+d)
        s4 = s3-s2-s1 #ad+bc

        s1 = int(str(s1)+"0"*2*i)
        s4 = int(str(s4)+"0"*i)
        product = s1 + s2 + s4
        
        return product

def normalize_len(x1, x2):
    '''This function equalizes the length of x1 and x2,
        and turns odd lenghts into even through 0 padding'''
    if len(x1)>len(x2):
        if len(x1)% 2 == 0: #even
            x2 = x2.zfill(len(x1))
        else: #odd
            x2 = x2.zfill(len(x1)+1)
            x1 = x1.zfill(len(x1)+1)

    else:
        if len(x2)% 2 == 0:
            x1 = x1.zfill(len(x2))
        else:
            x1 = x1.zfill(len(x2)+1)
            x2 = x2.zfill(len(x2)+1)
    return x1, x2
        
x1 = input("First number: ")
x2 = input("Second number: ")
print(karatsuba(x1, x2))
