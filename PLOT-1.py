# AUTHOR:- KUSH SHAH
import matplotlib.pyplot as plt

def relu(x):
    return max(0, x)

x = list(range(-5, 6))
y = [relu(i) for i in x]
plt.plot(x, y)
plt.show()