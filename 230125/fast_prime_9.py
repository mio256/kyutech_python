import math

def is_prime(num):
    if num < 2:
        return False
    elif num in [2,3]:
        return True
    elif num % 2 == 0:
        return False
    elif num % 3 == 0:
        return False
    
    sqrtNum = math.floor(math.sqrt(num))
    for i in range(5, sqrtNum + 1, 2):
        if num % i == 0:
            return False
    
    return True

cnt=0
i=0
while cnt<1400:
    if is_prime(i):
        if str(i)[-1]=='9':
            cnt+=1
    i+=1
print(i-1)
