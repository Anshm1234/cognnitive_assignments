import numpy as ny
#2(a)
# array=ny.array([10,52,62,16,16,54,453])

# #1
# sorted_array=ny.sort(array)
# print(sorted_array)

# #2
# indices_sorted=ny.argsort(array)
# print(indices_sorted)

# #3
# print("4 smallest elements are ",sorted_array[0:4])

# #4
# print("5 largest elements are ",sorted_array[-4:])


#2(b)
array=ny.array([1.0,1.2,2.2,2.0,3.0,2.0])

#1
integer_elements=array[array==array.astype(int)]
print(integer_elements)

#2
float_values=ny.array[array!=array.astype(int)]
print(float_values)