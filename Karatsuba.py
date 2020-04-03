def karatsuba(x1, x2):
    if len(x1)==1 and len(x2)==1:
        product = int(x1)*int(x2)
        return product
    else:
        x1, x2 = normalize_len(x1, x2)
        a = x1[:len(x1)//2]
        b = x1[len(x1)//2:]
        c = x2[:len(x2)//2]
        d = x2[len(x2)//2:]
        
        s1 = karatsuba(a,c)
        s2 = karatsuba(b,d)
        ab = str(int(a)+int(b))
        cd = str(int(c)+int(d))
        s3 = karatsuba(ab,cd)
        s4 = s3-s2-s1 #ad+bc
        
        product = s1*10**(len(a)*2) + s2 + s4*10**(len(a))
        
        return product

def normalize_len(x1, x2):
    if len(x1)>len(x2):
        if len(x1)% 2 == 0:
            x2 = x2.zfill(len(x1))
        else:
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
