
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


data = pd.read_csv("gadi.csv")
sekmes = np.array(data)
print(data.info())

xpoints = sekmes[:,0]
ypoints = sekmes[:,1]


plt.subplot(2,1,1)
plt.plot(xpoints, ypoints, marker = 'X')
plt.title("dzimsanagads pirmais")
# plt.show()

xpoints = sekmes[:,3]
ypoints = sekmes[:,2]

plt.subplot(2,1,2)
plt.plot(xpoints, ypoints, color = 'r', ls = ':')
plt.title("dzimsanagads otrais")

plt.suptitle("cik visiem gadi")
plt.show()