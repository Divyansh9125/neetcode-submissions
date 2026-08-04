class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniques = []
        for num in nums:
            if num in uniques:
                return True
            else:
                uniques.append(num)
        return False
        