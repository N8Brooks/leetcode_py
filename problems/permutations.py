from itertools import permutations
from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    return [list(nums) for nums in permutations(nums)]
