array = [4, 2, 9, 1, 5, 6]

mapped_array = [x * 2 for x in array]

ascending_order = sorted(mapped_array)

descending_order = sorted(mapped_array, reverse=True)

print("Original Array:", array)
print("Mapped Array:", mapped_array)
print("Ascending Order:", ascending_order)
print("Descending Order:", descending_order)
