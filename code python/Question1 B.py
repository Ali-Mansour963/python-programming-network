L = [x for x in range (2,1001) if all(x%i!=0 for i in range (2,x))]
print(L)