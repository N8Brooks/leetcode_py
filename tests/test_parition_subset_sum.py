from problems.partition_subset_sum import can_partition


def test_example_1() -> None:
    assert can_partition([1, 5, 11, 5]) is True


def test_example_2() -> None:
    assert can_partition([1, 2, 3, 5]) is False


def test_small() -> None:
    assert can_partition([1, 2, 5]) is False
