import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dat1m = "testing/dist1m_mov15.csv"
dat2m = "testing/dist2m_mov15.csv"
dat3m = "testing/dist3m_mov15.csv"
dat4m = "testing/dist4m_mov15.csv"
dat5m = "testing/dist5m_mov15.csv"
dat6m = "testing/dist6m_mov15.csv"
dat7m = "testing/dist7m_mov15.csv"
dat8m = "testing/dist8m_mov15.csv"
dat9m = "testing/dist9m_mov15.csv"
# dat10m = "testing/dist10m.csv"
df1 = pd.read_csv(dat1m)
data1 = df1.to_numpy()
df2 = pd.read_csv(dat2m)
data2 = df2.to_numpy()
df3 = pd.read_csv(dat3m)
data3 = df3.to_numpy()
df4 = pd.read_csv(dat4m)
data4 = df4.to_numpy()
df5 = pd.read_csv(dat5m)
data5 = df5.to_numpy()
df6 = pd.read_csv(dat6m)
data6 = df6.to_numpy()
df7 = pd.read_csv(dat7m)
data7 = df7.to_numpy()
df8 = pd.read_csv(dat8m)
data8 = df8.to_numpy()
df9 = pd.read_csv(dat9m)
data9 = df9.to_numpy()
# df10 = pd.read_csv(dat10m)
# data10 = df10.to_numpy()

z_dists = []
z_dists.append(data1[:,2])
z_dists.append(data2[:,2])
z_dists.append(data3[:,2])
z_dists.append(data4[:,2])
z_dists.append(data5[:,2])
z_dists.append(data6[:,2])
z_dists.append(data7[:,2])
z_dists.append(data8[:,2])
z_dists.append(data9[:,2])
# z_dists.append(data10[:,2])

means = []
for i in range(len(z_dists)):
    means.append(np.mean(z_dists[i]) - (i+1)*100)

plt.plot(means) # plotting mean errors
plt.ylabel("Estimation error (cm)")
plt.xlabel("Distance to marker (m)")
plt.title("Mean error as distance increases")


# plotting all z-axis estimations

# plt.plot(z_dists[0], color="blue", label="1m distance")
# plt.plot(z_dists[1], color="red", label="2m distance")
# plt.plot(z_dists[2], color="green", label="3m distance")
# plt.plot(z_dists[3], color="yellow", label="4m distance")
# plt.plot(z_dists[4], color="black", label="5m distance")
# plt.plot(z_dists[5], color="orange", label="6m distance")
# plt.plot(z_dists[6], color="navy", label="7m distance")
# plt.plot(z_dists[7], color="violet", label="8m distance")
# plt.plot(z_dists[8], color="maroon", label="9m distance")
# # plt.plot(z_dists[9], color="grey", label="10m distance")
# # plt.ylim(570,720)
# plt.ylabel("z-distance (cm)")
# plt.xlabel("Points")
# plt.legend()
# plt.title("Pose estimation as distance increases")

plt.show()


