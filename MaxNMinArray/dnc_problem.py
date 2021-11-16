class MinMax(object):
    def __init__(self,Min=0,Max=0):
        self.Min = Min
        self.Max = Max
        
def getMinMax(arr:list,size:int)->MinMax:
    minmaxobj = MinMax()
    
    #if there is only one element in the list
    if arr and size==1:
        minmaxobj.Max=arr[0]
        minmaxobj.Min = arr[0]
        return minmaxobj
    
    #@if element is more than two
    if arr[0]>=arr[1]:
        minmaxobj.Max=arr[0]
        minmaxobj.Min = arr[1]
    else:
        minmaxobj.Max=arr[1]
        minmaxobj.Min = arr[0]
    
    for i in range(2,len(arr)):
        if arr[i]<minmaxobj.Min:
            minmaxobj.Min = arr[i]
        elif arr[i]>minmaxobj.Max:
            minmaxobj.Max = arr[i]
    
    return minmaxobj

if __name__=='__main__':
    arr = [1000, 11, 445, 1, 330, 3000]
    arr_size = len(arr)
    MinMax=getMinMax(arr,arr_size)
    print("Minimum Element is {0}".format(MinMax.Min))
    print("Maximum Element is {0}".format(MinMax.Max))
    
