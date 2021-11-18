class Solution:

    def __init__(self) -> None:
        self.sum = 0
        self.list = [0,1]
    
    def generateFibonacciList(self,num)->list:

        fibo = self.list

        while fibo[-1]<num:
            
            fibo.append(fibo[-1]+fibo[-2])

        del fibo[-1]

        self.list=fibo

        return self.list

    def findSumEvenElement(self)->int:
        
        test=filter(lambda x: x%2==0, self.list)
        

        return sum(list(test))

    #TODO using recursion
    # def fibonacciSum(self,num)->int:
        
    #     if num==0 or num ==1:
    #         return num
        
    #     else:
    #         a=self.fibonacciSum(num-1)+self.fibonacciSum(num-2)
    #         return (a if a%2==0 else 0)


if __name__ == '__main__':
    sol = Solution()
    print(sol.generateFibonacciList(4000000))   
    print(sol.findSumEvenElement())   