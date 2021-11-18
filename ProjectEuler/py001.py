class Solution:

    def __init__(self) -> None:
        self.sum = 0
    
    def sumFinder(self,num)-> int:
        return sum([ item for item in range(1,num) if (item%3==0 or item%5==0)])        

if __name__ == '__main__':
    sol = Solution()
    print(sol.sumFinder(1000))