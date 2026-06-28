class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        ans = []

        for n in nums:
            count[n] = count.get(n, 0) + 1

        sorted_num = sorted(count.items(), key = lambda x: x[1], reverse= True)
        ans = []

        for num, freq in sorted_num[:k]:
            ans.append(num)
        
        return ans

        
        