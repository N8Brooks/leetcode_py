from typing import Generator, List


def max_areas(height: List[int]) -> Generator[int, None, None]:
    i = 0
    j = len(height) - 1
    while i < j:
        if height[i] < height[j]:
            yield (j - i) * height[i]
            i += 1
        else:
            yield (j - i) * height[j]
            j -= 1


def max_area(height: List[int]) -> int:
    return max(max_areas(height), default=0)
