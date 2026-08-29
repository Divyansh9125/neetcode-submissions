class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bruteforce:
        ## 1. compute the frequency of each of the element
        ## 2. sort the elements in decreasing order by their freq
        ## 3. return the frist k elements from this sorted list

        # computing the freq of each of the element in nums
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] = freq[num] + 1
        
        pairs = [[num, freq[num]] for num in freq.keys()]

        pairs_sorted = sorted(pairs, key=lambda x: x[1], reverse=True)

        output = []
        for i in range(0, k):
            output.append(pairs_sorted[i][0])
        return output