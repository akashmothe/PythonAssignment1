from collections import Counter

# def high_low_occurrence(l):
#     res = Counter(l)
#     max_count = (0,0)
#     min_count = ()
#     for key,val in res.items():
#         if val > max_count[-1]:
#             max_count = (key,val)
#     return max_count

def high_low_occurrence(l):
    res = Counter(l)
    return res.most_common(1)

l = [7, 8, 4, 2, 4, 4, 1, 1, 7, 7, 2, 5]
print(high_low_occurrence(l))
