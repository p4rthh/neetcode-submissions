class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        di = dict()
        for i in nums:
            if i not in di.keys():
                di[i] = 1
            else:
                di[i] += 1
        k_freq = [item[0] for item in sorted(di.items(), key=lambda item: item[1], reverse=True)[:k]]
        return k_freq