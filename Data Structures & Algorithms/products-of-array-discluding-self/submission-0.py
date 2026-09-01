class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        _cummulative_product = 1
        _has_zero = False
        _has_multiple_zero = False
        _zero_idx = -1
        for idx, num in enumerate(nums):
            if num != 0:
                _cummulative_product *= num
            else:
                if _has_zero:
                    _has_multiple_zero = True
                _has_zero = True
                _zero_idx = idx
        
        _out_list = [0] * len(nums)
        if _has_multiple_zero:
            return _out_list
        
        if _has_zero:
            _out_list[_zero_idx] = _cummulative_product
            return _out_list
        
        for idx, num in enumerate(nums):
            _out_list[idx] = _cummulative_product//num
        return _out_list


