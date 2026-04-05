from chi2dist.chi2distance import chi_square_distance

# Test with equal length arrays
arr1 = ['A', 'A', 'B', 'B', 'C', 'D']
arr2 = ['A', 'B', 'B', 'C', 'C', 'C']

distance = chi_square_distance(arr1, arr2)
print(f"Distance between equal length arrays: {distance}")

print("\n")
arr3 = ['A', 'A', 'B', 'B', 'C']
arr4 = ['A', 'B', 'B', 'C', 'C', 'C']

distance = chi_square_distance(arr3, arr4)
print(f"Distance between unequal length arrays: {distance}")

