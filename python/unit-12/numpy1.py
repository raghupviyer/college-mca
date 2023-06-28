import numpy as np

distance = [10, 15, 17, 26]
time = [0.3, 0.47, 0.55, 1.2]

try:
  speed = distance/time
  print(speed)
except:
  print('error')
finally:
  distance = np.array(distance)
  time = np.array(time)
  speed =  distance/time
  print(speed)

arr=np.arange(0,11)
print(arr[:-1])
print(arr)

arr = np.arange(0,9)
print(arr)
print(arr.reshape(3,3))
print(arr.reshape(3,3).sum())
print(arr.reshape(3,3).sum(axis=0))

arr = np.arange(10)
print(arr.reshape(2, -3))
print("---")
arr = np.arange(9).reshape(3,3)
print(arr)
print('---')
print(arr[:, [2,0,1]])