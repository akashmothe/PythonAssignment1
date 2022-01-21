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
    max_count = (0,0)
    min_count = ()
    for key,val in res.items():
        if val > max_count[-1]:
            max_count = (key,val)
        # if val < min_count[-1]:
        #     min_count = (key, val)
    return max_count

l = [7, 8, 4, 2, 4, 4, 1, 1, 7, 7, 2, 5]
print(high_low_occurrence(l))
