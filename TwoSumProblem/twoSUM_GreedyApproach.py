class Solution:

    def twoSum(self, nums, target):
        temp = []

        # Sort the arrary first
        nums.sort()
        print(nums)
        # Getting forward and backward index
        forward = 0
        backward = len(nums)-1  # Last index of nums

        while (forward < backward):
            sum = nums[forward]+nums[backward]
            if sum == target:
                a = list([forward, backward])
                temp.append(a)
                if (nums[a[0]] == nums[forward+1]):
                    forward += 1
                    continue

                elif (nums[a[1]] == nums[backward-1]):
                    backward -= 1
                    continue
                else:
                    forward += 1
                    backward -= 1
            elif sum < target:
                forward += 1
            else:
                backward -= 1

        return temp


nums = [0, 0, 1, -2, 3, -3]
target = 3
solution = Solution()
print("Target {}".format(3))
print(solution.twoSum(nums, target))
