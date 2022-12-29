import sys
import random
n=int(sys.argv[1])
m=int(sys.argv[2])

f= open('workfile.txt', 'w')
f.write("-------------------------------------------------------------------------\n\n")
for w in range(n):
    param="T"+str(w)
    f.write(str(param))
    f.write("   ")
f.write("\n")
f.write("#########################################################################\n\n")

for e in range(m):
    for g in range(n):
        sample=random.randrange(0,50,2)
        f.write(str(sample))
        f.write("   ")
    f.write("\n")
f.close()
        
