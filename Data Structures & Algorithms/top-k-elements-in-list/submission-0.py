class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = {}
        res = []
        min_freq = 0

        for num in nums:
            store[num] = store.get(num, 0) + 1

        buckets = [[] for i in range(len(nums))]
        for num in store:
            buckets[store[num]-1].append(num)

        i = len(nums) - 1
        while len(res) < k:
            for num in buckets[i]:
                res.append(num)
            i -= 1


        return res

            

        