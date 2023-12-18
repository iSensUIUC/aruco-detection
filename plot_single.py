import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dynamic_data = "testing/dist6m_mov15.csv"
static_data = "testing/dist6m.csv"
df = pd.read_csv(dynamic_data)
data_dyn = df.to_numpy()
df2 = pd.read_csv(static_data)
data_stat = df2.to_numpy()

x = data_stat[:,0]
y = data_stat[:,1]
z = data_stat[:,2]
z2 = data_stat[:,2]


# plotting z-axis measurements for stationary and moving test

# plt.subplot(121)
# plt.plot(z2, color="blue", label="Stationary camera")
# # plt.plot(z2, color="red")
# plt.ylim(570,720)
# plt.ylabel("z-distance (cm)")
# plt.xlabel("Points")
# plt.legend()
# plt.title("Z-displacement = 150 cm")
# plt.subplot(122)
# plt.plot(z, color="red", label="Moving Camera")
# # plt.plot(z2, color="red")
# plt.ylim(570,720)
# plt.ylabel("z-distance (cm)")
# plt.xlabel("Points")
# plt.legend()
# plt.title("Z-displacement = 150 cm")


# plotting 3D plot of recording measurements

fig = plt.figure(figsize = (10, 7))
ax = plt.axes(projection ="3d")
ax.scatter3D(x, y, z, color = "green")
ax.scatter3D(10, 10, 600, color = "red")
ax.set_zlim(0,750)
ax.set_xlim(-300,300)
ax.set_ylim(-300,300)
 
# show plot
plt.show()


