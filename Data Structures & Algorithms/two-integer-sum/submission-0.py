class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h_map = {}
        for idx, num in enumerate(nums):
            if num not in h_map:
                h_map[num] = [idx]
            else:
                h_map[num].append(idx)
        
        for idx, num in enumerate(nums):
            if (target - num) == num:
                if len(h_map[num]) > 1:
                    return h_map[num][0:2]
            else:
                if target - num in h_map:
                    return [idx, h_map[target - num][0]]
                