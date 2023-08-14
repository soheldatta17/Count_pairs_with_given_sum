class Solution:
    def getPairsCount(self, arr, n, k):
        dict = {}
        count = 0
        arr=sorted(arr)
        for i in range(n):
            if(arr[i]>k):
                break
            if k - arr[i] in dict:
                count += dict[k - arr[i]]
            if arr[i] in dict:
                dict[arr[i]] += 1
            else:
                dict[arr[i]] = 1
        return count