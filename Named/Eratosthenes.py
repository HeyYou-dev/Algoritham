
def SieveOfEratosthenes(n):
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

    return primeList,len(primeList)
if __name__ == '__main__':
    num = 600
    print(SieveOfEratosthenes(num))