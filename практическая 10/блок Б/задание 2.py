T = open(r'D:\Users\Zybin-A.M_Y-224_vvod2.txt')

f = open(r'D:\Users\Zybin-A.M_Y-224_vivod2.txt', 'w+')

D = T.readlines(5)
Q = T.readlines(5)
A = T.readlines(5)
a = [[int(x) for x in D],[int(x) for x in Q],[int(x) for x in A]]




def F():
  
    L = []
    for i in range(len(a)):    
        L.append(a[i][i])
    f.write(str(L))
    f.write(str(sum(L)))
    summ = 0
    for i in L:
        summ += i
    f.write(str(summ))
    for i in range(len(a)):
        if i+1 % 2 == 0:
            for j in range(len(a[i])):
                a[i][j]  /= summ
    f.write(str(a))
F()
f.close()