import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

xpoints = np.array([0, 6])
ypoints = np.array([0,14, 250])

#plt.plot(xpoints, ypoints, color="#23A763")
#plt.scatter(xpoints, ypoints, color="blue")
#plt.pie([5, 4, 3, 2, 1])
#plt.show()

fig, ax = plt.subplots()
dias = ['L', 'M', 'X', 'J', 'V', 'S', 'D']
temperaturas = {'Madrid':[28.5, 30.5, 31, 30, 28, 27.5, 30.5], 'Barcelona':[24.5, 25.5, 26.5, 25, 26.5, 24.5, 25]}
ax.plot(dias, temperaturas['Madrid'], color = 'tab:purple', marker="o")
ax.plot(dias, temperaturas['Barcelona'], color = 'tab:green', marker="o")
ax.set_title("Temperatura España")
ax.set_xlabel("Dias")
ax.set_ylabel("Temperatura")
plt.show()