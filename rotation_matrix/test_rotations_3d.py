from matplotlib import pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d.proj3d import proj_transform

## https://gist.github.com/WetHat/1d6cd0f7309535311a539b42cccca89c
class Arrow3D(FancyArrowPatch):

    def __init__(self, xyz, xyz2, *args, **kwargs):
        super().__init__((0, 0), (0, 0), *args, **kwargs)
        self._xyz = (xyz[0], xyz[1], xyz[2])
        self._xyz2 = (xyz2[0], xyz2[1], xyz2[2])

    def draw(self, renderer):
        x1, y1, z1 = self._xyz
        x2, y2, z2 = self._xyz2

        xs, ys, zs = proj_transform((x1, x2), (y1, y2), (z1, z2), self.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        super().draw(renderer)

    def do_3d_projection(self, renderer=None):
        x1, y1, z1 = self._xyz
        x2, y2, z2 = self._xyz2

        xs, ys, zs = proj_transform((x1, x2), (y1, y2), (z1, z2), self.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))

        return np.min(zs)

fig = plt.figure(figsize=(5, 5))


def get_x_rotmat(angle):
    angle = angle / 180 * np.pi
    sin = np.sin(angle)
    cos = np.cos(angle)
    return np.array([[1, 0, 0], [0, cos, -sin], [0, sin, cos]])


def get_y_rotmat(angle):
    angle = angle / 180 * np.pi
    sin = np.sin(angle)
    cos = np.cos(angle)
    return np.array([[cos, 0, sin], [0, 1, 0], [-sin, 0, cos]])


def get_z_rotmat(angle):
    angle = angle / 180 * np.pi
    sin = np.sin(angle)
    cos = np.cos(angle)
    return np.array([[cos, -sin, 0], [sin, cos, 0], [0, 0, 1]])

def get_3d_rotmat_xyz(angle_x, angle_y, angle_z):
    return get_z_rotmat(angle_z) @ get_y_rotmat(angle_y) @ get_x_rotmat(angle_x)

def get_3d_rotmat_zyx(angle_z, angle_y, angle_x):
    return get_x_rotmat(angle_x) @ get_y_rotmat(angle_y) @ get_z_rotmat(angle_z)


ax3d = fig.add_subplot(111, projection="3d")

min, max = -5, 5

axis = np.array([[min, 0, 0], [max, 0, 0], [0, min, 0], [0, max, 0], [0, 0, min], [0, 0, max]])

axis_x = Arrow3D(axis[0], axis[1])
axis_y = Arrow3D(axis[2], axis[3])
axis_z = Arrow3D(axis[4], axis[5])
ax3d.add_artist(axis_x)
ax3d.add_artist(axis_y)
ax3d.add_artist(axis_z)

ax3d.set_xlim(min, max)
ax3d.set_ylim(min, max)
ax3d.set_zlim(min, max)


point3d = np.array([2, 0, 2])
ax3d.scatter(point3d[0], point3d[1], point3d[2])

rotation3d = get_3d_rotmat_xyz(0, 30, 0)
transposed_3d = rotation3d @ np.transpose(point3d)
ax3d.scatter(transposed_3d[0], transposed_3d[1], transposed_3d[2])

axis = np.array([[min, 0, 0], [max, 0, 0], [0, min, 0], [0, max, 0], [0, 0, min], [0, 0, max]])
rotated_axis = rotation3d @ np.transpose(axis)
rotated_axis = np.transpose(rotated_axis)
axis_x = Arrow3D(rotated_axis[0], rotated_axis[1])
axis_y = Arrow3D(rotated_axis[2], rotated_axis[3])
axis_z = Arrow3D(rotated_axis[4], rotated_axis[5])
ax3d.add_artist(axis_x)
ax3d.add_artist(axis_y)
ax3d.add_artist(axis_z)


arrow = Arrow3D(point3d, transposed_3d)
ax3d.add_artist(arrow)

plt.show()

