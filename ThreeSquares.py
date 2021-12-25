import math

seq = set(eval(input()))
k = 0

maxset = max(seq)

#print("Max = " + str(maxset))

sums = set()

#print("i from 1 to " + str(int(maxset**0.5)))
for i in range(1, int(maxset**0.5)):
    #print("j from " + str(i) + " to " + str(int((maxset - i*i)**0.5)))
    for j in range(i, int((maxset - i*i)**0.5) + 1):
        #print("k from " + str(j) + " to " + str(int((maxset - i*i - j*j)**0.5)))
        for k in range(j, int((maxset - i*i - j*j)**0.5) + 1):
            #print("k = " + str(k))
            sums.add(i*i + j*j + k*k)
            #print("sum of " + str(i) + " " + str(j) + " " + str(k) + " = "  + str(i*i + j*j + k*k))

c = seq.intersection(sums)
        
print(len(c))

#for i in seq:
#    for j in sums:
#        if (i == j):
#            k = k + 1
            
#print(k)