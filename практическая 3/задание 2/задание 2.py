n=int(input())
n=n%(60*24)
h=n//60
n=n%60
print(h,n)