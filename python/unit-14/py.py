import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

x = [0,1,2]
y = [100, 200, 300]

plt.plot(x, y)
plt.title('Basic Line Plot with title')
plt.xlabel('X label')
plt.ylabel('Y Label')

# plt.show()

plt.plot(x,y)
plt.xlim(0,2)
plt.ylim(100,300)
plt.title('Customer data')
plt.xlabel('Experience')
plt.ylabel('salary')
# plt.show()

x = np.linspace(-1, 1, 50)
y1 = x**4 + 1
y2 = 4**x + 1

plt.figure(num = 3, figsize= (8, 5))
p1 = plt.plot(x, y1)
p2 = plt.plot(x, y2, 
         color = 'green',
         linewidth=1.0,
         linestyle='-'
         )
plt.legend([p1, p2], ['Line 1', 'Line 2'])
plt.show()

x=[5,7,8]
y=[10,11,12]

plt.scatter(x, y)
plt.show()

plt.bar(x, y)
plt.xlabel('fruits')
plt.ylabel('count')
plt.title('Count of fruits')
plt.show()
plt.barh(x, y)
plt.show()

# histogram

mu = 200
sigma = 15
x = mu + sigma * np.random.randn(50000)

num_bins = 40
n, bins, patches = plt.hist(x, num_bins, facecolor='red', alpha= 0.5 )