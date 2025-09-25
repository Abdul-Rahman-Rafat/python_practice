#1# set is mutable but its elements must be immutable due to its elements must be hashable 
#2#due to it's hashable so it complexity is o(1)

#3# code
import time

N = 1_00_000
nums = list(range(N))
nums_set = set(nums)

start = time.time()
for i in range(N):
    i in nums
end = time.time()
print("List time:",round((end - start) ,1), "s")

start = time.time()
for i in range(N):
    i in nums_set
end = time.time()
print("Set time:", round((end - start),1), "s")
