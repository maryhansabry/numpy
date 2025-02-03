# numpy
import numpy as np
# 1 a)
a=np.array([[1,2,3]])
b=np.array([[10, 20, 30], [40, 50, 60]])
print (a+b)
# b)
a=np.array([[1, 2], [3, 4]])
b=np.array([[10], [20]])
print(a*b)
# 2. Indexing and Slicing (High Dimensional Arrays)
arr = np.arange(1, 25).reshape(2, 3, 4)
print(arr)
# a) Extract the second slice along axis 0.
print(arr[1,:,:])#or arr[1]
# b) Extract all rows and the last column for all slices.
print(arr[:,:,3])
print("================================================================")
# c) Reverse the order of slices along axis 0.
print(arr[1::-1])
# d) Set all even elements in the array to -1.
arr[arr%2==0]=-1
print (arr)
print("================================================================")
# 3. np.repeat
# a) Given `arr = np.array([1, 2, 3, 4, 5, 6])`, create a new array where every odd element is repeated twice.
arr = np.array([1, 2, 3, 4, 5, 6])
print(np.repeat(arr[arr%2==1], 2))
# b) Given `arr = np.array([1, 2, 3, 4, 5, 6])`, create a new array where elements are repeated based on their value
print(np.repeat(arr,arr))
# 4. Normalizing
# a) Normalize a 1D array `arr = np.array([10, 20, 30])` to have values between 0 and 1.
arr = np.array([10, 20, 30])
arr=(arr-arr.min())/(arr.max()-arr.min())
print(arr)

# 5) b) Given a 4x4 matrix, replace all elements on the main diagonal with 0 without using a loop.
a=np.arange(0,16).reshape(4,4)
np.fill_diagonal(a,0)
print(a)     