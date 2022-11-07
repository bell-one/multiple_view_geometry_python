import json
import numpy as np
import cv2

## Read label datas
path_label = "0003_M217M218_F_A_02482_02962_0000000.json"
data = json.load(open(path_label))

## Read 2d, 3d keypoints
keypoints2d = data['annotations'][0]['keypoints']
np_keypoints2d = np.array(keypoints2d)
np_keypoints2d = np_keypoints2d.reshape(-1, 3)
xy2d = np_keypoints2d[:, :2]

keypoints3d = data['annotations'][0]['keypoints3d']
np_keypoints3d = np.array(keypoints3d)
np_keypoints3d = np_keypoints3d.reshape(-1, 6)
xyz3d = np_keypoints3d[:, :3]

## write 3d point clouds
# f = open("xyz3d.txt", 'w')
# for xyz in xyz3d:
#     f.write('%.2f %.2f  %.2f\n' % (xyz[0], xyz[1], xyz[2]))
# f.close()

## read cam params
intrinsic = data['videos'][0]['parameters']['intrinsic']
extrinsic = data['videos'][0]['parameters']['extrinsic']

fx, fy, cx, cy = intrinsic[0], intrinsic[1], intrinsic[2], intrinsic[3]
rx, ry, rz, tx, ty, tz = extrinsic[0], extrinsic[1], extrinsic[2], extrinsic[3], extrinsic[4], extrinsic[5]
intrinsic_mat = np.array([[fx, 0, cx], [0, fy, cy], [0, 0, 1]], dtype=np.float64)

## Read Images
path_image = "0003_M217M218_F_A_02482_02962_0000000.jpg"
img = cv2.imread(path_image)

## draw 2d label red
for xy in xy2d:
    img = cv2.circle(img, (xy[0], xy[1]), 10, (0, 0, 255), 5)

r_mat, _ = cv2.Rodrigues(np.array(extrinsic[:3]))
rt_mat = np.concatenate((r_mat, np.array([extrinsic[3:]]).T), axis=1)
## draw 3d label blue
for xyz in xyz3d:

    a = r_mat[0][0] * xyz[0] + r_mat[0][1] * xyz[1] + r_mat[0][2] * xyz[2] + tx
    b = r_mat[1][0] * xyz[0] + r_mat[1][1] * xyz[1] + r_mat[1][2] * xyz[2] + ty
    c = r_mat[2][0] * xyz[0] + r_mat[2][1] * xyz[1] + r_mat[2][2] * xyz[2] + tz

    x = fx * a / c + cx
    y = fy * b / c + cy

    xy = [x, y]
    img = cv2.circle(img, (int(xy[0]), int(xy[1])), 10, (255, 0, 0), 5)

## check images
cv2.imshow('original', img)
cv2.imwrite('original2.jpg', img)
cv2.waitKey(0)


pass


