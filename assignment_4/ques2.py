import numpy as ny

arr=ny.array([1,2,3,4,5])

#1)
print(arr[::-1])

#2)
arr1 = ny.array([1, 2, 3, 4, 5, 1, 2, 1, 1, 1])

unique_elements, counts = ny.unique(arr1, return_counts=True)

most_frequent = unique_elements[ny.argmax(counts)]

indexes = ny.where(arr1 == most_frequent)[0]

print(f"Most frequent element: {most_frequent}")
print(f"Indexes: {indexes}")

arr2= ny.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3, ]) 
unique_element1, count =ny.unique(arr2, return_counts=True)
most_freq=unique_element1[ny.argmax(count)]
index=ny.where(arr2==most_freq)[0]

print("Most freq element ",most_freq)
print("Indexes ",index)