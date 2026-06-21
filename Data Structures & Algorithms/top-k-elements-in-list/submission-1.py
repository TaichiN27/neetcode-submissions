class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # mapで{num: count}の形で整理する
        count = {}

        for key in nums:
            count[key] = count.get(key, 0) + 1
            
            

        # count(value)大きい順で並び替え

        sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)

        # 上からk番目までのkey(=num)をListで取得

        result = []

        for i in range(k):
            result.append(sorted_items[i][0])

        return result
        