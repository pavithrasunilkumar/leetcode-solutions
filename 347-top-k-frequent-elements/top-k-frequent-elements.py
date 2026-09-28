class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1

        bucket=[[]for _ in range(len(nums)+1)]
        for num,count in freq.items():
            bucket[count].append(num)

        ans = []

        for count in range(len(bucket) - 1, 0, -1):
            for num in bucket[count]:
                ans.append(num)

                if len(ans) == k:
                    return ans
        