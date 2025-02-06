import numpy as ny

gfg=ny.array([[4,1,9],[12,3,1],[4,5,6]])

# #1
# print(ny.sum(gfg))

# #2
print("element wise sum is ")
print(ny.sum(gfg,axis=1))

#3
print("column wise sum is ")
print(ny.sum(gfg,axis=0))