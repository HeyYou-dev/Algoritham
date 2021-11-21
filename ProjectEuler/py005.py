#step1: find prime all prime number till n
def FindPrimeNumber(n):
    primeCheck = [True if i!=1 and i!=0 else False for i in range(n)  ]
    primeList =[]
    p =2 
    while(p*p<n):
        if primeCheck[p]==True:
            for i in range(p*p,n,p):
                primeCheck[i]= False
        p+=1
    for i in range(n):
        if primeCheck[i]:
            primeList.append(i)

    return primeList



#step2: storing each prime number and their exponential count
def PrimeNumberExp(n):
    hashmap={}
    for i in FindPrimeNumber(n):
        j=1
        while (20>i**j):
            j=j+1    
        if i not in hashmap:
            hashmap[i]=j-1
    return hashmap


#step3: calculate key**value

def calculate(n):
    hashmap = PrimeNumberExp(n)
    mul = 1
    for key,value in hashmap.items():
        mul*=(key**value)

    print(mul)



calculate(20)