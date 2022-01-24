
def sort_by_column(arr,k):
    kth_column = [ele[k-1] for ele in arr]
    kth_col_sorted = sorted(kth_column)
    for i in range(len(kth_col_sorted)):
        arr[i][k-1] = kth_col_sorted[i]
    return arr


k = int(input("Enter the column number: "))
arr = [[39, 27, 11, 42], [10, 93, 91, 90], [54, 78, 56, 89], [24, 64, 20, 65]]
print(sort_by_column(arr,3))