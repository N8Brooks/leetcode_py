from problems.accounts_merge import accounts_merge


def test_example_1() -> None:
    actual = sorted(
        accounts_merge(
            [
                ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                ["John", "johnsmith@mail.com", "john00@mail.com"],
                ["Mary", "mary@mail.com"],
                ["John", "johnnybravo@mail.com"],
            ]
        )
    )
    expected = sorted(
        [
            ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
            ["Mary", "mary@mail.com"],
            ["John", "johnnybravo@mail.com"],
        ]
    )
    assert actual == expected


def test_example_2() -> None:
    actual = sorted(
        accounts_merge(
            [
                ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"],
                ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
                ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
                ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
                ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"],
            ]
        )
    )
    expected = sorted(
        [
            ["Ethan", "Ethan0@m.co", "Ethan4@m.co", "Ethan5@m.co"],
            ["Gabe", "Gabe0@m.co", "Gabe1@m.co", "Gabe3@m.co"],
            ["Hanzo", "Hanzo0@m.co", "Hanzo1@m.co", "Hanzo3@m.co"],
            ["Kevin", "Kevin0@m.co", "Kevin3@m.co", "Kevin5@m.co"],
            ["Fern", "Fern0@m.co", "Fern1@m.co", "Fern5@m.co"],
        ]
    )
    assert actual == expected


def test_one_account() -> None:
    actual = sorted(
        accounts_merge(
            [
                ["David", "David0@m.co", "David4@m.co", "David3@m.co"],
                ["David", "David5@m.co", "David5@m.co", "David0@m.co"],
                ["David", "David1@m.co", "David4@m.co", "David0@m.co"],
                ["David", "David0@m.co", "David1@m.co", "David3@m.co"],
                ["David", "David4@m.co", "David1@m.co", "David3@m.co"],
            ]
        )
    )
    expected = sorted(
        [
            [
                "David",
                "David0@m.co",
                "David1@m.co",
                "David3@m.co",
                "David4@m.co",
                "David5@m.co",
            ]
        ]
    )
    assert actual == expected


def test_many() -> None:
    actual = sorted(
        accounts_merge(
            [
                ["Alex", "Alex5@m.co", "Alex4@m.co", "Alex0@m.co"],
                ["Ethan", "Ethan3@m.co", "Ethan3@m.co", "Ethan0@m.co"],
                ["Kevin", "Kevin4@m.co", "Kevin2@m.co", "Kevin2@m.co"],
                ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe2@m.co"],
                ["Gabe", "Gabe3@m.co", "Gabe4@m.co", "Gabe2@m.co"],
            ]
        )
    )
    expected = sorted(
        [
            ["Alex", "Alex0@m.co", "Alex4@m.co", "Alex5@m.co"],
            ["Ethan", "Ethan0@m.co", "Ethan3@m.co"],
            ["Gabe", "Gabe0@m.co", "Gabe2@m.co", "Gabe3@m.co", "Gabe4@m.co"],
            ["Kevin", "Kevin2@m.co", "Kevin4@m.co"],
        ]
    )
    assert actual == expected
