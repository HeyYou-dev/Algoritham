"""
Problem:

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

"""
import math

#Get the factor of number 

def get_factors(number):

    listOfFactors=[]
    for item in range(1,int(math.sqrt(number))+1):
        if number%item==0:
            listOfFactors.append(item)
            listOfFactors.append(number//item)
    return listOfFactors


#check if givenNumber is having two factor or not 
def is_prime(number):
    return len(get_factors(number))==2


largestPrime =0
number = 600851475143 
AllFactors = get_factors(number)
print(AllFactors)
for factor in AllFactors:

    if is_prime(factor) and factor>largestPrime:

        largestPrime =factor



print(largestPrime)



