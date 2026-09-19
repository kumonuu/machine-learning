import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5,6,7,8,9,10])
y = np.array([2,4,6,8,10,12,14,16,18,20])

# slope = np.sum((x - np.mean(x)) * (y - np.mean(y))) / np.sum((x - np.mean(x)) ** 2)
# print(slope)

# intercept = np.mean(y) - (slope * np.mean(x))
# print(intercept)


# plt.figure(figsize=(5,5))
# plt.title("regression plot")

# plt.xlabel("x")
# plt.ylabel("mx + c")
# plt.plot(x,(slope * x) + intercept,label="line")
# plt.scatter(x,y,label="scatter")
# plt.legend()

# plt.show()

# using regression

from sklearn.linear_model import LinearRegression
import seaborn

lr = LinearRegression()
x = x.reshape(10,1)
print(x)
print(x.shape)

lr_fit = lr.fit(x,y)
coefficient = lr_fit.coef_[0]
intercept = lr_fit.intercept_
print(coefficient)
print(intercept)

seaborn.regplot(x=x,y=y)

plt.show()