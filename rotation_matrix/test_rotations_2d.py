from matplotlib import pyplot as plt
import numpy as np


def get_2d_rotmat(angle):
    angle = angle / 180 * np.pi
    sin = np.sin(angle)
    cos = np.cos(angle)
    return np.array([[cos, -sin], [sin, cos]])

fig = plt.figure(figsize=(5, 5))
ax2d = fig.add_subplot(111)
point2d = np.array([5, 0])
ax2d.scatter(point2d[0], point2d[1])

rotation2d = get_2d_rotmat(45) # angle with degree
transposed_2d = rotation2d @ np.transpose(point2d)
ax2d.scatter(transposed_2d[0], transposed_2d[1])
plt.axis([0, 10, 0, 10])


plt.annotate('', xy=transposed_2d, xytext=point2d, arrowprops=dict(facecolor='black'))




plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.show()