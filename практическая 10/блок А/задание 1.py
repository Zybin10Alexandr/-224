u = open(r'D:\Users\Zybin-A.M_Y-224_vvod1.txt')


f = open(r'D:\Users\Zybin-A.M_Y-224_vivod1.txt', 'w+')
R = u.readlines()
D = u.readlines(5)
Q = u.readlines(5)
A = u.readlines(5)
a = [[int(x) for x in D],[int(x) for x in Q],[int(x) for x in A]]
  
    
def F():    
    b = []
    c = []
    for i in range(len(a)):
        for j in range(len(a[i])):  
            a[j][i]=a[i][j]         

    for w in a:
        f.write(str(w))
F()
f.close()