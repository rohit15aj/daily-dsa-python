class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        
        
        pair_xors = {u ^ v for u in unique_nums for v in unique_nums}
        
       
        triplet_xors = {p ^ w for p in pair_xors for w in unique_nums}
        
        return len(triplet_xors)