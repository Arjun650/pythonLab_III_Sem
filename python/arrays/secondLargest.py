n = [1 , 6 , 33 , 6 , 3  , 78 ,3 ]

def secondLargens(n):
    for i in range(len(n)+1):
        if(n[i] > n[i+1]):
            temp = n[i]
            n[i] = n[i+1]
            n[i+1] = n[i]
    
secondLargens(n)
print(n)
