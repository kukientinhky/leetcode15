def main():
    nums = [-1,0,1,2,-1,-4]
    nums.sort()
    ans = []
    for i in range(0, len(nums)):
        low, high = i + 1, len(nums) - 1
        while low < high:
            kq = []
            s = nums[i] + nums[low] + nums[high]
            if (s > 0): 
                high -= 1
            elif (s < 0):
                low += 1
            else:
                kq.append(nums[i])
                kq.append(nums[low])
                kq.append(nums[high])
                if kq not in ans:
                    ans.append(kq)
                lastLowOccurrence, lastHighOccurrence = nums[low], nums[high]
                while low < high and nums[low] == lastLowOccurrence:
                    low += 1  
                while low < high and nums[high] == lastHighOccurrence:
                    high -= 1
    print(ans)
if __name__ == "__main__":
    main()