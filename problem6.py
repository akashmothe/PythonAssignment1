from collections import Counter

# def high_low_occurrence(l):
#     unique = list(set(l))
#     max_count = 0
#     min_count = 0
#     for i in unique:
#         x = l.count(i)
#         if x > max_count:
#             max_count = x


def high_low_occurrence(l):
    res = Counter(l)
    for i in res.elements():
        print(res[i])
    return Counter(l)

l = [7, 8, 4, 2, 4, 4, 1, 1, 7, 7, 2, 5]
print(high_low_occurrence(l))
