from collections import Counter


# def high_low_occurrence(l):
#     res = Counter(l)
#     return res.most_common(1    )

def high_low_occurrence(l):
    max_ele = 0
    max_frequency = 0
    min_ele = 0
    min_frequency = 0
    # frequency = []
    for i in l:
        if i > max_ele and l.count(i) > max_frequency:
            max_ele = i
            max_frequency = l.count(i)
        min_ele = i
        min_frequency = l.count(i)
        if i < min_ele and l.count(i) < min_frequency:
            min_ele = i
            min_frequency = l.count(i)
    print(f"Highest occurring element {max_ele} occurs {max_frequency} times.")
    print(f"Lowest occurring element {min_ele} occurs {min_frequency} times.")

l = [7, 8, 4, 2, 4, 4, 1, 1, 7, 7, 2, 5]
high_low_occurrence(l)
