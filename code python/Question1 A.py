L1 = ['HTTP','HTTPS','FTP','DNS']
L2 = [80,443,20,53]
d = {k:v for (k,v) in zip (L1,L2)}
print(d)