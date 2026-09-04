class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) in [0,1]:
            return len(nums)
        _sorted_nums = sorted(nums)
        _seq_length = 1
        _dups = 0
        _max_seq_length = 1
        print(_sorted_nums)
        for idx in range(1, len(_sorted_nums)):
            _is_greater = _sorted_nums[idx] == (_sorted_nums[idx-1]+1)
            _is_equal = _sorted_nums[idx] == (_sorted_nums[idx-1])
            _cond = _is_equal or _is_greater
            # print(f'current: {_sorted_nums[idx]}, prev: {_sorted_nums[idx-1]}, cond: {_cond}')
            if _cond:
                if _is_equal:
                    _dups += 1
                _seq_length += 1
                # print(f'seq_length: {_seq_length}, dups: {_dups}')
            else:
                if (_seq_length - _dups) > _max_seq_length:
                    _max_seq_length = _seq_length - _dups
                    # print(f'max seq_length: {_max_seq_length}')
                _seq_length = 1
                _dups = 0
        # print(f'loop exited')
        if (_seq_length - _dups) > _max_seq_length:
                _max_seq_length = _seq_length - _dups
        return _max_seq_length