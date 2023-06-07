#347. Top K Frequent Elements
#Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order
#Example 1:                             #Example 2:
#Input: nums = [1,1,1,2,2,3], k = 2     #Input: nums = [1], k = 1
#Output: [1,2]                          #Output: [1]

from heapq import heappop, heappush, heappushpop


def Kfrecuent(nums,k): # Stoled from Leetcode/anCoderr
    freq_table = {}
    for i in nums:
        freq_table[i] = freq_table.get(i, 0) + 1
    heap = []
    for i in freq_table.keys():
            heappushpop(heap, (freq_table[i], i))
            heappush(heap, (freq_table[i], i))
    ans = []
    while k > 0:
        k -= 1
        ans.append(heappop(heap)[1])
    return ans

nums = [1,1,1,2,2,3]
k=2
print(Kfrecuent(nums, k))