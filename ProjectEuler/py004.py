
"""
@A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

def FindLargestPalindromeNumber():
    test=0
    for i in range (999,99,-1):
        for j in range(i,99,-1):
            num =i*j
            xnum = str(num)
            #print(xnum[::-1])
            if str(num)==xnum[::-1] and int(num)>test:
                test=int(num)
                break

    return test