#Don't go Outside in Odd day
a=0
b=0

for i in [1,2,3,4,5,6,7,8,9,10,12,13,14,15]:
    if int(i)%2==0:
        a+=1
    else:
        b+=1
print('no.of even number--->',a)
print('no.of odd number--->',b)
