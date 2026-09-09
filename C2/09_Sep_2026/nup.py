import numpy as np
# arr=np.array([1,2,3,4,5,6,7,8,9])
# print("Array",arr)

# arr1= np.array([[1,2,3,4],[5,6,7,8]])
# print("2d Array ",arr1)

# print(type(arr).__name__)
# print(type(arr1).__name__)


import time
size= 10110101
print(size)

py_list=list(range(size))
nump_arr=np.arange(size)

print(f"The array size {size}")
print()

start = time.time()
res_py= [x+1 for x in py_list]
time_python = time.time()- start
print(f"the total time : {time_python:.5f} Second")

start = time.time()
res_nump=nump_arr + 1
time_num =time.time()-start
print(f"total time : {time_num:.5f} second ")
